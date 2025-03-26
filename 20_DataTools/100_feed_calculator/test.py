import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from Ui_mainwindow import Ui_MainWindow

# define the main window class
class NexusWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ## Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


# define the main window function
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = window = NexusWindow()
    wid.show()
    app.exec()