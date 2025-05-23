import sys
import yaml
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
                              QFileDialog, QMessageBox, QSplitter, QTabWidget, QMenuBar,
                              QStatusBar, QInputDialog)
from PySide6.QtGui import QAction
from PySide6.QtCore import (Qt, Signal, QObject, QSize)

class ConfigSignals(QObject):
    file_loaded = Signal(str)
    file_saved = Signal(str)
    modified = Signal(bool)

class ConfigEditor(QMainWindow):
    SUPPORTED_FORMATS = ("yaml", "yml")
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.config_data = None
        self.is_modified = False
        self.signals = ConfigSignals()
        
        self.init_ui()
        self.init_menu()
        self.connect_signals()

    def init_ui(self):
        """初始化主界面"""
        self.setWindowTitle("配置文件编辑器")
        self.setGeometry(100, 100, 1024, 768)
        
        # 创建主部件
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("配置结构")
        self.tree.itemChanged.connect(self.handle_item_change)
        
        self.tab_widget = QTabWidget()
        
        # 使用分割器布局
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.tree)
        splitter.addWidget(self.tab_widget)
        splitter.setSizes([300, 700])
        
        self.setCentralWidget(splitter)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def init_menu(self):
        """初始化菜单系统"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        self.new_action = QAction("新建", self)
        self.open_action = QAction("打开", self)
        self.save_action = QAction("保存", self)
        self.save_as_action = QAction("另存为", self)
        file_menu.addActions([self.new_action, self.open_action, self.save_action, self.save_as_action])
        
        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        self.add_key_action = QAction("添加键", self)
        self.delete_key_action = QAction("删除键", self)
        edit_menu.addActions([self.add_key_action, self.delete_key_action])

    def connect_signals(self):
        """连接信号与槽"""
        self.new_action.triggered.connect(self.new_file)
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.save_as_action.triggered.connect(self.save_as_file)
        self.add_key_action.triggered.connect(self.add_config_item)
        self.delete_key_action.triggered.connect(self.delete_config_item)
        self.signals.modified.connect(self.update_title)

    # 文件操作相关方法
    def check_unsaved_changes(self):
        """检查未保存修改, 返回True表示继续操作"""
        if self.is_modified:
            reply = QMessageBox.question(
                self, '未保存的修改',
                '当前修改尚未保存，是否要保存？',
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Save:
                self.save_file()
                return True
            elif reply == QMessageBox.Cancel:
                return False
        return True

    def init_new_document(self):
        """初始化新文档"""
        # 弹出格式选择对话框
        format_choice, ok = QInputDialog.getItem(
            self, "选择格式", "请选择配置文件格式:",
            ["YAML"], 0, False
        )
        
        if ok:
            # 初始化数据结构
            self.config_data = {} if format_choice == "YAML" else {}
            self.current_file = None
            self.file_format = format_choice.lower()
            
            # 更新界面
            self.build_tree()
            self.signals.modified.emit(False)
            self.status_bar.showMessage("新建 {} 文件".format(format_choice))
            self.update_title(modified=False)

    def new_file(self):
        """新建文件"""
        if self.check_unsaved_changes():
            self.init_new_document()
        
        self.current_file = None
        self.config_data = {}
        self.build_tree()
        self.signals.modified.emit(False)
        self.status_bar.showMessage("新建文件")
        self.update_title(modified=False)
    def open_file(self):
        """打开配置文件对话框"""
        path, _ = QFileDialog.getOpenFileName(
            self, "打开配置文件", "", 
            "配置文件 (*.yaml *.yml);;所有文件 (*.*)"
        )
        if path:
            self.load_file(path)

    def load_file(self, path):
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
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"文件加载失败: {str(e)}")

    def save_file(self):
        """保存当前文件"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_as_file()

    def save_as_file(self):
        """另存为文件"""
        path, _ = QFileDialog.getSaveFileName(
            self, "保存配置文件", "",
            "YAML文件 (*.yaml *.yml)"
        )
        if path:
            self.save_to_file(path)
            self.current_file = path
            self.status_bar.showMessage(f"文件已保存到: {path}")

    def save_to_file(self, path):
        """将数据保存到文件"""
        try:
            with open(path, "w", encoding="utf-8") as f:
                if path.endswith((".yaml", ".yml")):
                    yaml.dump(self.config_data, f, allow_unicode=True)
            
            self.signals.file_saved.emit(path)
            self.signals.modified.emit(False)
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

    # 数据操作相关方法
    def add_config_item(self):
        """添加新配置项"""
        current_item = self.tree.currentItem()
        parent_data = self.get_data_from_item(current_item)
        
        key, ok = QInputDialog.getText(
            self, "新建配置项", "请输入键名:"
        )
        if ok and key:
            try:
                if isinstance(parent_data, dict):
                    parent_data[key] = ""
                elif isinstance(parent_data, list):
                    parent_data.append("")
                else:
                    raise ValueError("无法在此节点添加子项")
                
                self.build_tree()
                self.signals.modified.emit(True)
            except Exception as e:
                QMessageBox.warning(self, "添加失败", str(e))

    def delete_config_item(self):
        """删除配置项"""
        current_item = self.tree.currentItem()
        if not current_item:
            return
        
        parent = current_item.parent()
        parent_data = self.get_data_from_item(parent)
        
        try:
            if isinstance(parent_data, dict):
                del parent_data[current_item.data(0, Qt.UserRole)]
            elif isinstance(parent_data, list):
                index = parent.indexOfChild(current_item)
                del parent_data[index]
            
            self.build_tree()
            self.signals.modified.emit(True)
        except Exception as e:
            QMessageBox.warning(self, "删除失败", str(e))

    # 辅助方法
    def get_data_from_item(self, item):
        """从树节点获取对应的数据"""
        data = self.config_data
        path = []
        
        while item and item != self.tree.invisibleRootItem():
            path.append(item.data(0, Qt.UserRole))
            item = item.parent()
        
        for key in reversed(path):
            if isinstance(data, dict):
                data = data.get(key)
            elif isinstance(data, list) and isinstance(key, int):
                data = data[key]
        
        return data

    def parse_value(self, value_str):
        """尝试解析值类型"""
        try:
            return int(value_str)
        except ValueError:
            try:
                return float(value_str)
            except ValueError:
                if value_str.lower() in ("true", "false"):
                    return value_str.lower() == "true"
                return value_str

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
    editor = ConfigEditor()
    editor.show()
    sys.exit(app.exec())