import sys
import os
from datetime import datetime
import serial
import yaml
from pathlib import Path

# Pyside6 modules
from PySide6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit, QTabWidget, QWidget, QVBoxLayout, QPushButton, QStatusBar, QLabel, QSplitter, QFileDialog, QMessageBox)
from PySide6.QtGui import (QAction, QIcon, QTextCursor)
from PySide6.QtCore import (QThread, Signal, QObject, QSize, Qt)

# modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from mod.ui.UiObjects.SelectionDialog import SelectionDialog
from mod.utils.SerialWorker.SerialWorker import SerialWorker
from mod.utils.logger.logger import Logger

# 设置脚本目录和数据文件路径
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "output.csv")

data_log = Logger(
    filename=data_path,
    fieldnames=["timestamp", "message"],
)


class ConfigSignals(QObject):
    """信号类"""
    file_loaded = Signal(str)
    file_saved = Signal(str)
    modified = Signal(bool)

class ParaReader(QMainWindow):
    """主界面类"""
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.config_data = None
        self.is_modified = False
        self.signals = ConfigSignals()

        self.thread = None        
        self.worker = None
        self.port_seeker = None
        data_log = None
        
        self.init_ui()
        self.init_menu()

    def init_ui(self):
        """初始化"""
        self.setWindowTitle("Para Reader-RS232 ver_0.1.2b")
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowOpacity(0.96)
        
        # 创建主部件
        """信息输出"""
        self.output_showcase = QPlainTextEdit()
        self.output_showcase.setReadOnly(True) # 只读
        self.output_showcase.setLineWrapMode(QPlainTextEdit.NoWrap) # 关闭自动换行
        output_font = self.output_showcase.font()
        output_font.setFamily("Consolas")  # 等宽字体
        output_font.setPointSize(10) # 字体大小
        self.output_showcase.setFont(output_font) # 设置字体
        
        """控制面板标签组"""
        self.control_panel = QTabWidget()
        self.init_control_panel()
        self.control_panel.setTabPosition(QTabWidget.North) # 标签UI位置
        self.control_panel.setMovable(False) # 禁止拖动标签
        self.control_panel.setTabsClosable(False) # 禁止关闭标签
        
        # 使用分割器布局
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.addWidget(self.output_showcase)
        main_splitter.addWidget(self.control_panel)
        main_splitter.setSizes([600, 400])
        
        self.setCentralWidget(main_splitter)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        """日志"""
        self.log_panel = QPlainTextEdit()
        self.init_log_panel()

    def init_menu(self):
        """初始化菜单系统"""
        menubar = self.menuBar()

        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        self.add_key_action = QAction("添加键", self)
        self.delete_key_action = QAction("删除键", self)
        edit_menu.addActions([
            self.add_key_action, 
            self.delete_key_action
            ])

        # 配置文件菜单
        cfg_menu = menubar.addMenu("配置文件")
        self.open_cfg_action = QAction("打开", self)
        self.save_cfg_action = QAction("保存", self)
        self.cfg_save_as_action = QAction("另存为", self)
        cfg_menu.addActions([
            self.open_cfg_action, 
            self.save_cfg_action, 
            self.cfg_save_as_action
            ])

    def init_control_panel(self):
        """初始化控制面板"""
        self.init_operations_tab()
        self.init_cfg_tab()
        self.init_logs_tab()

    def init_operations_tab(self):
        """初始化操作面板"""
        operations_tab = QWidget()
        operations_tab_layout = QVBoxLayout()
        
        self.listener_trigger_button = QPushButton("开始监听")
        self.listener_trigger_button.clicked.connect(self.listener_toggle)
        self.export_data_button = QPushButton("导出数据")
        self.export_data_button.clicked.connect(self.replace_csv)
        self.clear_data_button = QPushButton("清除数据")

        operations_tab_layout.addWidget(self.listener_trigger_button)
        operations_tab_layout.addWidget(self.export_data_button)
        operations_tab_layout.addWidget(self.clear_data_button)
        operations_tab.setLayout(operations_tab_layout)

        self.control_panel.addTab(operations_tab, "操作面板")

    def listener_toggle(self):
        """切换按钮状态"""
        try:
            if not self.worker:
                self.start_listener()
                self.listener_trigger_button.setText("停止监听")
                return
            if self.worker.running:
                self.stop_listener()
                self.listener_trigger_button.setText("开始监听")
            else:
                self.start_listener()
                self.listener_trigger_button.setText("停止监听")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"操作失败: {str(e)}")
            self.log_message(f"操作失败: {str(e)}", level="FATAL")

    def init_cfg_tab(self):
        """初始化配置面板"""
        cfg_tab = QWidget()
        cfg_tab_layout = QVBoxLayout()

        cfg_tab.setLayout(cfg_tab_layout)

        self.control_panel.addTab(cfg_tab, "配置面板")
        
    
    def init_logs_tab(self):
        """初始化日志面板"""
        log_tab = QWidget()
        log_tab_layout = QVBoxLayout()
        
        log_tab.setLayout(log_tab_layout)
        
        self.control_panel.addTab(log_tab, "日志面板")

    def init_log_panel(self):
        """初始化日志面板"""
        self.log_panel.setReadOnly(True) # 只读
        self.output_showcase.setLineWrapMode(QPlainTextEdit.NoWrap) # 关闭自动换行
        self.log_panel.setMaximumHeight(150) # 设置最大高度
        self.log_panel.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1E1E1E;
                color: #D4D4D4;
                font-family: Consolas;
                font-size: 10pt;
                border-top: 1px solid #3C3C3C;
            }
        """)
        
        log_container = QWidget()                 # 创建日志容器
        log_layout = QVBoxLayout()
        log_layout.setContentsMargins(0, 0, 0, 0)
        log_layout.addWidget(QLabel("操作日志:"))
        log_layout.addWidget(self.log_panel)
        log_container.setLayout(log_layout)
        
        splitter = QSplitter(Qt.Vertical)         # 调整主布局
        splitter.addWidget(self.centralWidget())  # 原有主界面
        splitter.addWidget(log_container)
        splitter.setSizes([500, 150])
        self.setCentralWidget(splitter)

    def log_message(self, message: str, level: str = "INFO"):
        """记录日志信息"""
        color_map = {
            "INFO": "#569CD6",
            "WARNING": "#DCDCAA",
            "FATAL": "#D16969",
            "SUCCESS": "#4EC9B0"
        }
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        html = f"""
        <span style="color:{color_map.get(level, '#FFFFFF')};">
            [{timestamp}] {message}
        </span>
        """
        
        cursor = self.log_panel.textCursor()        # 使用HTML格式追加日志
        cursor.movePosition(QTextCursor.End)
        cursor.insertHtml(html + "<br>")
        self.log_panel.setTextCursor(cursor)
        self.log_panel.ensureCursorVisible()

# 监听器相关方法
    def start_listener(self):
        """开始监听"""
        if self.thread and self.thread.isRunning():
            return

        # 创建线程和工作对象
        self.thread = QThread()
        self.port_seeker = SerialWorker()
        available_ports = self.port_seeker.port_seek()
        if not available_ports:
            return
        port_selection = SelectionDialog.get_selection(
                available_ports,
                multi_select=False
                )[0]
        self.worker = SerialWorker(port_selection, 9600)
        self.worker.moveToThread(self.thread)

        # 连接信号
        self.worker.data_received.connect(self.handle_data)
        self.worker.status_updated.connect(self.update_status)
        self.worker.error_occurred.connect(self.handle_error)
        self.thread.started.connect(self.worker.start_monitoring)
        self.thread.finished.connect(self.worker.deleteLater)

        # 启动线程
        self.thread.start()

    def stop_listener(self):
        """停止监听"""
        if not self.worker:
            return
        if self.worker and self.thread.isRunning():
            self.worker.stop()  # 触发停止标志
            self.thread.quit()
            self.thread.wait()

    def handle_data(self, raw_data):
        """处理接收到的数据"""
        try:# 转换为字符串（ASCII解码）
            decoded_data = raw_data.decode('ascii').strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] RX: {decoded_data}")
            try:
                data_log.logger_record({
                    "timestamp": timestamp,
                    "message": decoded_data
                })
            except Exception as e:
                self.handle_error(e)
        except UnicodeDecodeError:
            # 二进制数据处理
            hex_data = raw_data.hex().upper()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] HEX: {hex_data}")
            try:
                data_log.logger_record({
                    "timestamp": timestamp,
                    "message": decoded_data
                })
            except Exception as e:
                self.handle_error(e)

    def update_status(self, message):
        """更新状态信息"""
        self.log_message(f"{message}", level="INFO")

    def handle_error(self, error):
        """处理错误"""
        self.log_message(f"{str(error)}", level="WARNING")
        self.stop_listener()

    def closeEvent(self, event):
        """窗口关闭时清理资源"""
        self.log_message("程序即将关闭...", level="INFO")
        self.stop_listener()
        event.accept()

    def replace_csv(self):
        """重新导出数据为CSV文件"""
        if self.worker and self.thread.isRunning():
            QMessageBox.warning(self, "提示", "请先停止监听后再导出数据。")
            return
        data_log.close()
        self.log_message(f"导出数据为CSV文件", level="INFO")
        script_dir = os.path.dirname(os.path.abspath(__file__))

        file_new_name = datetime.now().strftime("%Y%m%d-%H%M%S") + "-output.csv"
        new_filename_path = os.path.join(script_dir, file_new_name)
        data_log.replace_csv(new_filename=new_filename_path)

# UI相关模块

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParaReader()
    window.show()
    sys.exit(app.exec())