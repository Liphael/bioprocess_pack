import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                              QPushButton, QLabel, QVBoxLayout, QTextEdit)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class TabDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget 示例")
        self.setGeometry(100, 100, 600, 400)
        
        # 创建 QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # 初始化三个标签页
        self.init_first_tab()
        self.init_second_tab()
        self.init_third_tab()
        
        # 添加标签页切换事件
        self.tabs.currentChanged.connect(self.on_tab_changed)
        
        # 设置标签属性
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)  # 允许拖动排序
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)  # 关闭标签事件

    def init_first_tab(self):
        """第一个标签页：基础控件"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        btn = QPushButton("点击测试", self)
        btn.clicked.connect(lambda: print("第一个标签的按钮被点击"))
        layout.addWidget(btn)
        
        label = QLabel("这是第一个标签页的内容")
        layout.addWidget(label)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, QIcon("icon1.png"), "标签页1")

    def init_second_tab(self):
        """第二个标签页：文本编辑器"""
        text_edit = QTextEdit()
        text_edit.setPlainText("在此输入文本...")
        self.tabs.addTab(text_edit, QIcon("icon2.png"), "编辑器")

    def init_third_tab(self):
        """第三个标签页：动态内容"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        self.add_tab_btn = QPushButton("添加新标签页")
        self.add_tab_btn.clicked.connect(self.add_new_tab)
        layout.addWidget(self.add_tab_btn)
        
        widget.setLayout(layout)
        self.tabs.addTab(widget, "动态管理")

    def on_tab_changed(self, index):
        """标签切换事件处理"""
        print(f"切换到标签页: {self.tabs.tabText(index)}")

    def close_tab(self, index):
        """关闭标签页处理"""
        if index != 0:  # 禁止关闭第一个标签页
            self.tabs.removeTab(index)

    def add_new_tab(self):
        """动态添加新标签页"""
        new_tab = QTextEdit()
        new_tab.setPlainText(f"新标签页 {self.tabs.count() + 1}")
        self.tabs.addTab(new_tab, f"Tab {self.tabs.count() + 1}")
        self.tabs.setCurrentIndex(self.tabs.count() - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabDemo()
    window.show()
    sys.exit(app.exec())