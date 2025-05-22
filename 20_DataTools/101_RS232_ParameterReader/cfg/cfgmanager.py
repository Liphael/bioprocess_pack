import json
import configparser
import yaml
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
                              QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox,
                              QSplitter, QTabWidget)
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QAction

class ConfigSignal(QObject):
    config_loaded = Signal(str)
    config_saved = Signal(str)
    error_occurred = Signal(str)

class ConfigFileHandler:
    SUPPORTED_FORMATS = {'json', 'ini', 'yaml', 'yml'}
    
    def __init__(self):
        self.signals = ConfigSignal()
        self.current_path = None
        self.file_type = None
        self.config_data = None

    def detect_file_type(self, file_path):
        """自动检测配置文件类型"""
        suffix = Path(file_path).suffix.lower()[1:]
        if suffix in {'yaml', 'yml'}:
            return 'yaml'
        return suffix if suffix in self.SUPPORTED_FORMATS else None

    def load_config(self, file_path):
        """加载配置文件"""
        try:
            self.file_type = self.detect_file_type(file_path)
            if not self.file_type:
                raise ValueError("不支持的配置文件格式")

            with open(file_path, 'r', encoding='utf-8') as f:
                if self.file_type == 'json':
                    self.config_data = json.load(f)
                elif self.file_type == 'ini':
                    config = configparser.ConfigParser()
                    config.read_file(f)
                    self.config_data = {s: dict(config.items(s)) 
                                      for s in config.sections()}
                elif self.file_type in ('yaml', 'yml'):
                    self.config_data = yaml.safe_load(f)

            self.current_path = file_path
            self.signals.config_loaded.emit(file_path)
            return True

        except Exception as e:
            self.signals.error_occurred.emit(f"加载失败: {str(e)}")
            return False

    def save_config(self, save_path=None):
        """保存配置文件"""
        try:
            save_path = save_path or self.current_path
            if not save_path:
                raise ValueError("未指定保存路径")

            with open(save_path, 'w', encoding='utf-8') as f:
                if self.file_type == 'json':
                    json.dump(self.config_data, f, indent=2)
                elif self.file_type == 'ini':
                    config = configparser.ConfigParser()
                    for section, items in self.config_data.items():
                        config.add_section(section)
                        for key, value in items.items():
                            config.set(section, key, str(value))
                    config.write(f)
                elif self.file_type in ('yaml', 'yml'):
                    yaml.dump(self.config_data, f, default_flow_style=False)

            self.signals.config_saved.emit(save_path)
            return True

        except Exception as e:
            self.signals.error_occurred.emit(f"保存失败: {str(e)}")
            return False

class ConfigEditorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.handler = ConfigFileHandler()
        self.init_ui()
        self.connect_signals()
        self.current_view = None

    def init_ui(self):
        """初始化界面组件"""
        self.setWindowTitle("配置文件编辑器")
        self.setGeometry(100, 100, 800, 600)

        # 创建菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件")
        
        self.open_action = QAction("打开", self)
        self.save_action = QAction("保存", self)
        self.save_as_action = QAction("另存为", self)
        
        file_menu.addActions([self.open_action, self.save_action, self.save_as_action])

        # 主界面布局
        self.tab_widget = QTabWidget()
        self.tree_view = QTreeWidget()
        self.table_view = QTableWidget()
        
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.tree_view)
        splitter.addWidget(self.table_view)
        self.tab_widget.addTab(splitter, "编辑视图")
        
        self.setCentralWidget(self.tab_widget)

    def connect_signals(self):
        """连接信号与槽"""
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.save_as_action.triggered.connect(self.save_as_file)
        self.handler.signals.config_loaded.connect(self.update_ui)
        self.handler.signals.error_occurred.connect(self.show_error)

    def open_file(self):
        """打开文件对话框"""
        path, _ = QFileDialog.getOpenFileName(
            self, "打开配置文件", "", 
            "配置文件 (*.json *.ini *.yaml *.yml);;所有文件 (*.*)"
        )
        if path:
            self.handler.load_config(path)

    def save_file(self):
        """保存文件"""
        self.handler.save_config()

    def save_as_file(self):
        """另存为文件"""
        path, _ = QFileDialog.getSaveFileName(
            self, "保存配置文件", "",
            "配置文件 (*.json *.ini *.yaml *.yml);;所有文件 (*.*)"
        )
        if path:
            self.handler.save_config(path)

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

    def show_json_data(self, data, parent=None):
        """显示JSON数据结构"""
        parent = parent or self.tree_view
        if isinstance(data, dict):
            for key, value in data.items():
                item = QTreeWidgetItem([str(key)])
                parent.addChild(item)
                self.show_json_data(value, item)
        elif isinstance(data, list):
            for index, value in enumerate(data):
                item = QTreeWidgetItem([str(index)])
                parent.addChild(item)
                self.show_json_data(value, item)
        else:
            item = QTreeWidgetItem([str(data)])
            parent.addChild(item)

    def show_ini_data(self, data):
        """显示INI数据到表格"""
        self.table_view.setRowCount(0)
        self.table_view.setColumnCount(2)
        self.table_view.setHorizontalHeaderLabels(["键", "值"])
        
        row = 0
        for section, items in data.items():
            self.table_view.insertRow(row)
            self.table_view.setItem(row, 0, QTableWidgetItem(f"[{section}]"))
            self.table_view.setItem(row, 1, QTableWidgetItem(""))
            row +=1
            for key, value in items.items():
                self.table_view.insertRow(row)
                self.table_view.setItem(row, 0, QTableWidgetItem(key))
                self.table_view.setItem(row, 1, QTableWidgetItem(str(value)))
                row +=1

    def show_yaml_data(self, data):
        """显示YAML数据"""
        # 实现类似JSON的树形显示
        self.show_json_data(data)

    def show_error(self, message):
        """显示错误信息"""
        QMessageBox.critical(self, "错误", message)

if __name__ == "__main__":
    app = QApplication([])
    editor = ConfigEditorUI()
    editor.show()
    app.exec()