'''imports'''
import os
import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from modules.ui.Ui_0001 import Ui_MainWindow
import modules.utils.feedstrategies.stra_editor as stra_editor

'''global variables'''
global log
global process_info
process_info = None  # 用于存储进程信息

global default_path
global current_path
current_path = os.path.abspath(os.path.dirname(__file__))  # 获取当前文件所在目录的绝对路径
default_path = current_path                                # 固定main文件的默认路径


'''UI class'''
class MainWindowUi(QMainWindow):
    global log
    global process_info

    global default_path
    global current_path


    def __init__(self):
        super().__init__()

        '''set ui file'''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     # 这里使用直接通过类名调用setupUi方法，需要手动传入self参数来绑定MainWindow的组件

        '''binding signals and slots'''
        self.bind_clicks()


    '''define slots'''
    def bind_clicks(self):
        self.ui.calculate_button.clicked.connect(self.calculate_button)
        self.ui.load_stra_button.clicked.connect(self.stra_editor_button)
        self.ui.load_stra_button_2.clicked.connect(self.stra_editor_button)

    def calculate_button(self):
        ## read the values from the spinboxes
        be_vol = sa_vol = af_vol = 0  # 给予初始化0值，以防计算问题

        def calculate(self):
            be_vol = before_volume = float(self.ui.spinbox_before_sampling.value())
            sa_vol = sample_volume = float(self.ui.spinbox_sampling.value())

            ## calculate the feed volume
            af_vol = after_volume = be_vol - sa_vol

            def show_output(self):  # 继续使用函数嵌套的方式来定义输出函数
                output_text = f'''
                取样前体系质量为：
                {be_vol}  (g)(ml)
                取样量为：
                {sa_vol}  (g)(ml)
                取样后体系质量为：
                {af_vol}  (g)(ml)
                '''
                self.ui.textbrowser_output.setText(output_text)
        
            show_output(self)  # 调用show_output函数，使能calculate函数显示输出结果

        calculate(self)  # 调用calculate函数；不调用calculate函数，无法显示输出结果
    

    def stra_editor_button(self):
        self.stra_editor = stra_editor.StrategyEditor()
        self.stra_editor.show()


# define the main window function
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = window = MainWindowUi()
    wid.show()
    app.exec()