import os
import sys
import pandas as pd
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                              QFileDialog, QMessageBox, QToolBar, QStatusBar)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


global log
global process_info
process_info = None  # 用于存储进程信息

global default_path
global current_path
default_path = './'
current_path = os.path.abspath(os.path.dirname(__file__)) # 获取当前文件所在目录的绝对路径


class StrategyEditor(QMainWindow):
    global current_path

    def __init__(self):
        super().__init__()
        self.file_path = None
        self.df = pd.DataFrame()
        self.init_ui()
        self.init_menu()
        
        # 跟踪修改状态
        self.modified = False

    def init_ui(self):
        '''初始化界面'''
        self.setWindowTitle('补料策略编辑器')
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
        self.open_action = QAction('打开', self)
        self.open_action.setShortcut('Ctrl+O')
        self.save_action = QAction('保存', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_as_action = QAction('另存为', self)
        self.save_as_action.setShortcut('Ctrl+Shift+S')
        self.load_strategy_action = QAction('加载策略')
        self.load_strategy_action.setShortcut('Ctrl+E')
        self.clear_action = QAction('清空', self)
        self.above_add_row_action = QAction('向前插入新补料', self)
        self.below_add_row_action = QAction('向后插入新补料', self)
        self.left_add_col_action = QAction('向左添加参数', self)
        self.right_add_col_action = QAction('向右添加参数', self)

        
        toolbar.addActions([
            self.open_action,
            self.save_action,
            self.save_as_action,
            self.clear_action,
            self.above_add_row_action,
            self.below_add_row_action,
            self.left_add_col_action,
            self.right_add_col_action,
            self.load_strategy_action
        ])

    def init_menu(self):
        '''初始化菜单栏'''
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu('文件')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addAction(self.load_strategy_action)
        
        # 编辑菜单
        edit_menu = menubar.addMenu('编辑')
        edit_menu.addAction(self.clear_action)
        edit_menu.addAction(self.above_add_row_action)
        edit_menu.addAction(self.below_add_row_action)
        edit_menu.addAction(self.left_add_col_action)
        edit_menu.addAction(self.right_add_col_action)
        
        # 连接信号
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.save_as_action.triggered.connect(self.save_as_file)
        self.above_add_row_action.triggered.connect(self.above_add_row)
        self.below_add_row_action.triggered.connect(self.below_add_row)
        self.left_add_col_action.triggered.connect(self.left_add_col)
        self.right_add_col_action.triggered.connect(self.right_add_col)

    def open_file(self):
        '''打开csv文件'''
        path, _ = QFileDialog.getOpenFileName(
            self,
            '打开csv文件',
            current_path,
            'csv文件 (*.csv);;所有文件 (*.*)'
        )
        
        if path:
            try:
                # 使用pandas读取csv文件
                self.df = pd.read_csv(path)
                self.file_path = path
                self.load_data_to_table()
                self.status_bar.showMessage(f'已打开文件: {path}')
                self.modified = False
            except Exception as e:
                QMessageBox.critical(self, '错误', f'打开文件失败:\n{str(e)}')

    def save_file(self):
        '''保存文件'''
        if self.file_path:
            self.save_to_csv(self.file_path)
        else:
            self.save_as_file()

    def save_as_file(self):
        '''另存为文件'''
        path, _ = QFileDialog.getSaveFileName(
            self,
            '保存csv文件',
            current_path,
            'csv文件 (*.csv);;所有文件 (*.*)'
        )
        if path:
            if not path.endswith('.csv'):
                path += '.csv'
            self.save_to_csv(path)
            self.file_path = path
            self.status_bar.showMessage(f'文件已保存到: {path}')

    def load_data_to_table(self):
        '''将数据加载到表格'''
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

    def save_to_csv(self, path):
        '''将表格数据保存到csv'''
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
                    row_data.append(item.text() if item else '')
                data.append(row_data)
            
            self.df = pd.DataFrame(data, columns=columns)
            
            # 保存文件
            self.df.to_csv(path, index=False, engine='openpyxl')
            self.modified = False
            QMessageBox.information(self, '保存成功', '文件已成功保存！')
        except Exception as e:
            QMessageBox.critical(self, '错误', f'保存失败:\n{str(e)}')

    '''补料行添加器'''
    def below_add_row(self):
        current_row = self.table.currentRow()
        self.table.insertRow(current_row + 1)
        self.modified = True

    def above_add_row(self):
        current_row = self.table.currentRow()
        self.table.insertRow(current_row)
        self.modified = True

    '''参数列添加器'''
    def left_add_col(self):
        current_col = self.table.currentColumn()
        col_name = f'列{self.table.columnCount() + 1}'
        self.table.insertColumn(current_col)
        self.table.setHorizontalHeaderItem(
            current_col, QTableWidgetItem(col_name))
        self.modified = True

    def right_add_col(self):
        current_col = self.table.currentColumn()
        col_name = f'列{self.table.columnCount() + 1}'
        self.table.insertColumn(current_col + 1)
        self.table.setHorizontalHeaderItem(
            current_col + 1, QTableWidgetItem(col_name))
        self.modified = True

    def mark_modified(self):
        '''标记文件修改状态'''
        if not self.modified:
            self.modified = True
            self.setWindowTitle('csv 编辑器*')

    def closeEvent(self, event):
        '''关闭前检查保存'''
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = StrategyEditor()
    editor.show()
    sys.exit(app.exec())