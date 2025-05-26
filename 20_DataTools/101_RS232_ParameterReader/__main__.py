import sys
from datetime import datetime
import yaml
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
                              QFileDialog, QMessageBox, QSplitter, QTabWidget, QMenuBar,
                              QStatusBar, QInputDialog, QPlainTextEdit, QWidget, QVBoxLayout,
                              QLabel, QHBoxLayout, QLineEdit, QCheckBox, QRadioButton, QComboBox,
                              QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton)
from PySide6.QtGui import (QAction, QIcon, QTextCursor)
from PySide6.QtCore import (Qt, Signal, QObject, QSize)

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
        
        self.init_ui()
        self.init_menu()
        self.connect_signals()

# 初始化UI界面
    def init_ui(self):
        """初始化"""
        self.setWindowTitle("Para Reader-RS232 ver_0.1.1b")
        icon = QIcon()
        icon.addFile(u"./mod/ui/icon/biotech.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
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

        """树形视图"""
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("配置结构")
        self.tree.itemChanged.connect(self.handle_item_change)
        
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

# 菜单栏模块
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

# 信号槽定义
    def connect_signals(self):
        """连接信号与槽"""

        # 连接菜单动作按钮
        self.open_cfg_action.triggered.connect(self.open_cfg_file)
        self.save_cfg_action.triggered.connect(self.save_cfg_file)
        self.cfg_save_as_action.triggered.connect(self.cfg_file_save_as)

        # 连接编辑菜单动作按钮
        self.start_listener_key_action.triggered.connect(self.start_listener)
        self.export_data_key_action.triggered.connect(self.export_data_csv)

        # 连接信号
        self.signals.modified.connect(self.update_title) # 更新标题

# 文件操作相关方法
    def open_cfg_file(self):
        """打开配置文件对话框"""
        path, _ = QFileDialog.getOpenFileName(
            self, "打开配置文件", "", 
            "配置文件 (*.yaml *.yml);;所有文件 (*.*)"
        )
        if path:
            self.load_cfg_file(path)

    def load_cfg_file(self, path):
        """加载配置文件"""
        try:
            with open(path, "rb") as f:
                if path.endswith((".yaml", ".yml")):
                    self.config_data = yaml.safe_load(f)
            
            self.current_file = path
            self.build_tree()
            self.signals.file_loaded.emit(path)
            self.signals.modified.emit(False)
            self.status_bar.showMessage(f"已加载文件: {path}")

            self.log_message(f"配置文件已加载: {path}", "SUCCESS")

        except Exception as e:
            self.log_message(f"文件加载失败: {str(e)}", "ERROR")
            QMessageBox.critical(self, "错误", f"文件加载失败: {str(e)}")

    def save_cfg_file(self):
        """保存当前文件"""
        try:
            if self.current_file:
                self.save_to_file(self.current_file)
            else:
                self.cfg_file_save_as()

            self.log_message(f"配置文件已保存: {path}", "SUCCESS")
        
        except Exception as e:
            self.log_message(f"保存失败: {str(e)}", "ERROR")

    def cfg_file_save_as(self):
        """另存为文件"""
        try:
            path, _ = QFileDialog.getSaveFileName(
                self, "保存配置文件", "",
                "YAML文件 (*.yaml *.yml)"
            )
            if path:
                self.save_to_file(path)
                self.current_file = path
                self.status_bar.showMessage(f"文件已保存到: {path}")

            self.log_message(f"配置文件已另存为: {path}", "SUCCESS")
        except Exception as e:
            self.log_message(f"另存为失败: {str(e)}", "ERROR")
            QMessageBox.critical(self, "错误", f"另存为失败: {str(e)}")

    def save_to_file(self, path):
        """将数据保存到文件"""
        try:
            with open(path, "w", encoding="utf-8") as f:
                if path.endswith((".yaml", ".yml")):
                    yaml.dump(self.config_data, f, allow_unicode=True)
            
            self.signals.file_saved.emit(path)
            self.signals.modified.emit(False)

            self.log_message(f"文件已成功保存: {path}", "SUCCESS")
            QMessageBox.information(self, "保存成功", "文件已成功保存！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存失败: {str(e)}")

# 树形视图相关方法
    def build_tree(self, parent=None, data=None):
        """构建配置树形视图"""
        self.tree.clear()
        data = data or self.config_data
        parent = parent or self.tree
        
        if isinstance(data, dict):
            for key, value in data.items():
                item = QTreeWidgetItem(parent)
                item.setText(0, str(key))
                item.setData(0, Qt.UserRole, key)
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.build_tree(item, value)
        elif isinstance(data, list):
            for index, value in enumerate(data):
                item = QTreeWidgetItem(parent)
                item.setText(0, str(index))
                self.build_tree(item, value)
        else:
            item = QTreeWidgetItem(parent)
            item.setText(0, str(data))
            item.setFlags(item.flags() | Qt.ItemIsEditable)

    def handle_item_change(self, item):
        """处理树节点修改"""
        new_key = item.text(0)
        parent = item.parent()
        
        try:
            if parent:
                parent_data = self.get_data_from_item(parent)
                old_key = item.data(0, Qt.UserRole)
                
                if isinstance(parent_data, dict):
                    parent_data[new_key] = parent_data.pop(old_key)
                elif isinstance(parent_data, list):
                    index = parent.indexOfChild(item)
                    parent_data[index] = self.parse_value(new_key)
                
                item.setData(0, Qt.UserRole, new_key)
            else:
                self.config_data = self.parse_value(new_key)
            
            self.signals.modified.emit(True)
        except Exception as e:
            QMessageBox.warning(self, "修改错误", str(e))

    def update_ui(self, file_path):
        """根据文件类型更新显示"""
        self.tree_view.clear()
        self.table_view.clear()

        if self.handler.file_type == 'json':
            self.show_json_data(self.handler.config_data)
        elif self.handler.file_type == 'ini':
            self.show_ini_data(self.handler.config_data)
        elif self.handler.file_type in ('yaml', 'yml'):
            self.show_yaml_data(self.handler.config_data)

    def show_error(self, message):
        """显示错误信息"""
        QMessageBox.critical(self, "错误", message)

# 控制面板相关模块
    def init_control_panel(self):
        """初始化控制面板"""
        self.init_operations_tab()
        self.init_cfg_tab()
        self.init_logs_tab()

    def init_operations_tab(self):
        """初始化操作面板"""
        operations_tab = QWidget()
        operations_tab_layout = QVBoxLayout()
        
        self.start_listener_key_action = QAction("开始监听数据", self)
        self.export_data_key_action = QAction("导出当前数据", self)
        
        start_listener_button = QPushButton("添加键")
        start_listener_button.clicked.connect(self.start_listener_key_action.trigger)
        export_data_button = QPushButton("删除键")
        export_data_button.clicked.connect(self.export_data_key_action.trigger)

        operations_tab_layout.addWidget(start_listener_button)
        operations_tab_layout.addWidget(export_data_button)
        operations_tab.setLayout(operations_tab_layout)

        self.control_panel.addTab(operations_tab, "操作面板")

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


# 日志模块
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
        splitter.setSizes([600, 150])
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
        print("开始监听")
    
    def stop_listener(self):
        """停止监听"""
        print("停止监听")

    def export_data_csv(self):
        """导出数据为CSV文件"""
        print("导出数据为CSV文件")

# UI相关模块
    def update_title(self, modified):
        """更新窗口标题"""
        self.is_modified = modified
        title = "配置文件编辑器"
        if self.current_file:
            title += f" - {Path(self.current_file).name}"
        if modified:
            title += " *"
        self.setWindowTitle(title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParaReader()
    window.show()
    sys.exit(app.exec())