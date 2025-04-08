import sys
import pandas as pd
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                              QFileDialog, QMessageBox, QToolBar, QStatusBar)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class ExcelEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.df = pd.DataFrame()
        self.init_ui()
        self.init_menu()
        
        # 跟踪修改状态
        self.modified = False

    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle("Excel 编辑器")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建表格部件
        self.table = QTableWidget()
        self.table.cellChanged.connect(self.mark_modified)
        self.setCentralWidget(self.table)
        
        # 状态栏
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # 工具栏
        toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        
        # 工具栏按钮
        self.open_action = QAction("打开", self)
        self.save_action = QAction("保存", self)
        self.save_as_action = QAction("另存为", self)
        self.add_row_action = QAction("添加行", self)
        self.add_col_action = QAction("添加列", self)
        
        toolbar.addActions([
            self.open_action,
            self.save_action,
            self.save_as_action,
            self.add_row_action,
            self.add_col_action
        ])

    def init_menu(self):
        """初始化菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        
        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        edit_menu.addAction(self.add_row_action)
        edit_menu.addAction(self.add_col_action)
        
        # 连接信号
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.save_as_action.triggered.connect(self.save_as_file)
        self.add_row_action.triggered.connect(self.add_row)
        self.add_col_action.triggered.connect(self.add_col)

    def open_file(self):
        """打开Excel文件"""
        path, _ = QFileDialog.getOpenFileName(
            self, "打开Excel文件", "", 
            "Excel文件 (*.xlsx *.xls *.csv);;所有文件 (*.*)"
        )
        
        if path:
            try:
                # 使用pandas读取Excel文件
                self.df = pd.read_excel(path, engine='openpyxl')
                self.file_path = path
                self.load_data_to_table()
                self.status_bar.showMessage(f"已打开文件: {path}")
                self.modified = False
            except Exception as e:
                QMessageBox.critical(self, "错误", f"打开文件失败:\n{str(e)}")

    def save_file(self):
        """保存文件"""
        if self.file_path:
            self.save_to_excel(self.file_path)
        else:
            self.save_as_file()

    def save_as_file(self):
        """另存为文件"""
        path, _ = QFileDialog.getSaveFileName(
            self, "保存Excel文件", "", 
            "Excel文件 (*.xlsx);;所有文件 (*.*)"
        )
        if path:
            if not path.endswith('.xlsx'):
                path += '.xlsx'
            self.save_to_excel(path)
            self.file_path = path
            self.status_bar.showMessage(f"文件已保存到: {path}")

    def load_data_to_table(self):
        """将数据加载到表格"""
        self.table.blockSignals(True)  # 防止触发cellChanged信号
        
        # 设置表格维度
        rows, cols = self.df.shape
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        
        # 设置表头
        self.table.setHorizontalHeaderLabels(self.df.columns.astype(str))
        
        # 填充数据
        for i in range(rows):
            for j in range(cols):
                value = str(self.df.iloc[i, j])
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(i, j, item)
        
        self.table.blockSignals(False)
        self.modified = False

    def save_to_excel(self, path):
        """将表格数据保存到Excel"""
        try:
            # 从表格获取数据
            rows = self.table.rowCount()
            cols = self.table.columnCount()
            
            # 获取列头
            columns = [self.table.horizontalHeaderItem(i).text() 
                      for i in range(cols)]
            
            # 构建DataFrame
            data = []
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
            
            self.df = pd.DataFrame(data, columns=columns)
            
            # 保存文件
            self.df.to_excel(path, index=False, engine='openpyxl')
            self.modified = False
            QMessageBox.information(self, "保存成功", "文件已成功保存！")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存失败:\n{str(e)}")

    def add_row(self):
        """添加新行"""
        current_row = self.table.currentRow()
        self.table.insertRow(current_row + 1)
        self.modified = True

    def add_col(self):
        """添加新列"""
        current_col = self.table.currentColumn()
        col_name = f"列{self.table.columnCount() + 1}"
        self.table.insertColumn(current_col + 1)
        self.table.setHorizontalHeaderItem(
            current_col + 1, QTableWidgetItem(col_name))
        self.modified = True

    def mark_modified(self):
        """标记文件修改状态"""
        if not self.modified:
            self.modified = True
            self.setWindowTitle("Excel 编辑器*")

    def closeEvent(self, event):
        """关闭前检查保存"""
        if self.modified:
            reply = QMessageBox.question(
                self, '未保存的修改',
                '您有未保存的修改，是否要保存？',
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Save:
                self.save_file()
                event.accept()
            elif reply == QMessageBox.Cancel:
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ExcelEditor()
    editor.show()
    sys.exit(app.exec())