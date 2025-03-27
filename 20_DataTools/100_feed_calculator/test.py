import sys
import pandas as pd

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from Ui_mainwindow import Ui_MainWindow


# define the main window class
class NexusWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        ## Set up the user interface from Designer.
        self.setupUi(self)
        self.bind_click()
        global default_path
        default_path = "./"

    def bind_click(self):
        self.calculate_button.clicked.connect(self.calculate)
        self.calculate_button.clicked.connect(self.show_output)
        self.load_stra_button.clicked.connect(self.load_path)
        self.load_stra_button_2.clicked.connect(self.load_path)
        

    def load_path(self):
        global f_path
        f_path = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "./feed_plan",
            "CSV Files (*.csv)"
        )
        self.lineedit_path.setText(f_path[0])


    def load_strategies(self):
        stra = strategy = pd.read_csv(
            f_path,
            encoding = "utf8",
            sep = ",",
            dtype = {"Index":int,"Name":str,"Type":str,"Quantity":float},
            na_values = "NaN",
            thousands = ",",
            decimal = ".",
        )[col]

    
    def save_strategies(self):
        print("save_strategies")


    def save_configs(self):
        print("save_configs")


    def calculate(self):
        ## read the values from the spinboxes
        global be_vol
        be_vol = before_volume = float(self.spinbox_before_sampling.value())
        global sa_vol
        sa_vol = sample_volume = float(self.spinbox_sampling.value())

        ## calculate the feed volume
        global af_vol
        af_vol = after_volume = be_vol - sa_vol


    def show_output(self):
        output_text = f"""
        取样前体系质量为：
        {be_vol}  (g)(ml)
        取样量为：
        {sa_vol}  (g)(ml)
        取样后体系质量为：
        {af_vol}  (g)(ml)
        """
        self.textbrowser_output.setText(output_text)



# define the main window function
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = window = NexusWindow()
    wid.show()
    app.exec()