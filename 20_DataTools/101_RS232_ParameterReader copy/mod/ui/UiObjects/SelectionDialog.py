from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout, QPushButton, QLabel, QAbstractItemView

class SelectionDialog(QDialog):
    """通用列表选择对话框"""
    def __init__(self, items, multi_select = False, parent = None):
        super().__init__(parent)
        self.selected_items = []
        self.setWindowTitle("请选择")
        self.setMinimumSize(300, 400)
        
        # 创建界面组件
        self.list_widget = QListWidget()
        self.list_widget.addItems(items)
        
        # 设置选择模式
        if multi_select:
            self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        
        # 操作按钮
        self.confirm_btn = QPushButton("确认")
        self.confirm_btn.clicked.connect(self.accept_selection)
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.reject)

        # 布局管理
        layout = QVBoxLayout()
        layout.addWidget(QLabel("请选择项目:"))
        layout.addWidget(self.list_widget)
        btn_layout = QVBoxLayout()
        btn_layout.addWidget(self.confirm_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def accept_selection(self):
        """获取选中项并关闭对话框"""
        selected = [item.text() for item in self.list_widget.selectedItems()]
        if selected:
            self.selected_items = selected
            self.accept()
        else:
            self.reject()

    @staticmethod
    def get_selection(options, multi_select=False, parent=None):
        """静态方法快速调用"""
        dialog = SelectionDialog(options, multi_select, parent)
        result = dialog.exec()
        return dialog.selected_items if result == QDialog.Accepted else None