import sys
import pandas as pd
import json
import configparser
import yaml

from pathlib import Path

from PySide6.QtCore import QAbstractTableModel,Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from Ui_mainwindow import Ui_MainWindow


global log

# define the datamodel class
# This class is used to formulate data in the pyside-tableview
class DataModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            else:
                return str(section + 1)
        return None

class CfgEditor:
    Supported_Formats = {'json', 'ini', 'yaml', 'yml'}
    
    def __init__(self):
        self.signals = ConfigSignal()
        self.current_path = None
        self.file_type = None
        self.config_data = None

    ## automatically detect the file type
    def detect_file_type(self, file_path):
        f_sfx = file_suffix = Path(file_path).suffix.lower()[1:]
        if f_sfx in {'yaml', 'yml'}:
            return 'yaml'
        return f_sfx if f_sfx in self.Supported_Formats else None

    ## load the config file
    def load_config(self, file_path):
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

# define the main window class
class NexusWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        ## Set up the user interface from Designer.
        self.setupUi(self)
        self.bind_click()
        global default_path
        default_path = './'

    def bind_click(self):
        self.calculate_button.clicked.connect(self.calculate)
        self.calculate_button.clicked.connect(self.show_output)
        self.load_stra_button.clicked.connect(self.load_strategies)
        self.load_stra_button_2.clicked.connect(self.load_strategies)
        

    def load_path(self):
        global f_path
        try:
            f_path = QFileDialog.getOpenFileName(
                self,
                'Open File',
                './feed_plan',
                'CSV Files (*.csv)'
            )[0]
        except FileNotFoundError:
            log = log + '\\File not found!'
        self.lineedit_path.setText(f_path)


    def load_strategies(self):
        self.load_path()
        with open(f_path, encoding='utf8') as f:
            stra = strategy = pd.read_csv(
                f,
                encoding = 'utf8',
                sep = ',',
                header = 0,
                dtype = {'name':str,'type':str,'quantity':float,'unit':str},
                names = ['name','type','quantity','unit'],
                na_values = 'null',
                thousands = ',',
                decimal = '.',
            )
        f.close()
        stra_model = DataModel(stra)
        self.tableview_stra.setModel(stra_model)
        self.tableview_stra2.setModel(stra_model)

    ##todo: strategy editor & save the strategies to files
    def strategy_editor(self):
        print('save_strategies')


    def save_configs(self):
        print('save_configs')


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