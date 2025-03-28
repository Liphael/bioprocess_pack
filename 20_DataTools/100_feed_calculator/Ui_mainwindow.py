# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollBar,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(250, 150))
        MainWindow.setWindowOpacity(0.960000000000000)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1000, 600))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab_cal = QWidget()
        self.tab_cal.setObjectName(u"tab_cal")
        self.show_box = QGroupBox(self.tab_cal)
        self.show_box.setObjectName(u"show_box")
        self.show_box.setGeometry(QRect(440, 10, 521, 361))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.show_box.sizePolicy().hasHeightForWidth())
        self.show_box.setSizePolicy(sizePolicy1)
        self.tableWidget = QTableWidget(self.show_box)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 30, 481, 311))
        self.Input_box = QGroupBox(self.tab_cal)
        self.Input_box.setObjectName(u"Input_box")
        self.Input_box.setGeometry(QRect(440, 380, 521, 151))
        self.layoutWidget = QWidget(self.Input_box)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 377, 101))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_5.addWidget(self.label_9)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.combox_sampling = QComboBox(self.layoutWidget)
        self.combox_sampling.addItem("")
        self.combox_sampling.addItem("")
        self.combox_sampling.addItem("")
        self.combox_sampling.setObjectName(u"combox_sampling")

        self.verticalLayout_6.addWidget(self.combox_sampling)

        self.combox_before_sampling = QComboBox(self.layoutWidget)
        self.combox_before_sampling.addItem("")
        self.combox_before_sampling.addItem("")
        self.combox_before_sampling.addItem("")
        self.combox_before_sampling.addItem("")
        self.combox_before_sampling.addItem("")
        self.combox_before_sampling.addItem("")
        self.combox_before_sampling.setObjectName(u"combox_before_sampling")

        self.verticalLayout_6.addWidget(self.combox_before_sampling)

        self.combox_before_sampling_2 = QComboBox(self.layoutWidget)
        self.combox_before_sampling_2.addItem("")
        self.combox_before_sampling_2.addItem("")
        self.combox_before_sampling_2.addItem("")
        self.combox_before_sampling_2.addItem("")
        self.combox_before_sampling_2.addItem("")
        self.combox_before_sampling_2.addItem("")
        self.combox_before_sampling_2.setObjectName(u"combox_before_sampling_2")

        self.verticalLayout_6.addWidget(self.combox_before_sampling_2)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinbox_before_sampling = QDoubleSpinBox(self.layoutWidget)
        self.spinbox_before_sampling.setObjectName(u"spinbox_before_sampling")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinbox_before_sampling.sizePolicy().hasHeightForWidth())
        self.spinbox_before_sampling.setSizePolicy(sizePolicy2)
        self.spinbox_before_sampling.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinbox_before_sampling.setMaximum(100000.000000000000000)
        self.spinbox_before_sampling.setSingleStep(0.050000000000000)
        self.spinbox_before_sampling.setValue(1200.000000000000000)

        self.gridLayout.addWidget(self.spinbox_before_sampling, 1, 0, 1, 1)

        self.spinbox_sampling = QSpinBox(self.layoutWidget)
        self.spinbox_sampling.setObjectName(u"spinbox_sampling")
        sizePolicy2.setHeightForWidth(self.spinbox_sampling.sizePolicy().hasHeightForWidth())
        self.spinbox_sampling.setSizePolicy(sizePolicy2)
        self.spinbox_sampling.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinbox_sampling.setMaximum(1000)
        self.spinbox_sampling.setValue(10)

        self.gridLayout.addWidget(self.spinbox_sampling, 0, 0, 1, 1)

        self.spinbox_gluc = QDoubleSpinBox(self.layoutWidget)
        self.spinbox_gluc.setObjectName(u"spinbox_gluc")
        sizePolicy2.setHeightForWidth(self.spinbox_gluc.sizePolicy().hasHeightForWidth())
        self.spinbox_gluc.setSizePolicy(sizePolicy2)
        self.spinbox_gluc.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinbox_gluc.setDecimals(5)
        self.spinbox_gluc.setMaximum(1000.000000000000000)
        self.spinbox_gluc.setSingleStep(0.000010000000000)
        self.spinbox_gluc.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.spinbox_gluc, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.Input_box)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(390, 30, 111, 101))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.load_stra_button = QPushButton(self.layoutWidget1)
        self.load_stra_button.setObjectName(u"load_stra_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.load_stra_button.sizePolicy().hasHeightForWidth())
        self.load_stra_button.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.load_stra_button)

        self.clear_button = QPushButton(self.layoutWidget1)
        self.clear_button.setObjectName(u"clear_button")
        sizePolicy3.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.clear_button)

        self.calculate_button = QPushButton(self.layoutWidget1)
        self.calculate_button.setObjectName(u"calculate_button")
        sizePolicy3.setHeightForWidth(self.calculate_button.sizePolicy().hasHeightForWidth())
        self.calculate_button.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.calculate_button)

        self.groupBox = QGroupBox(self.tab_cal)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 391, 521))
        self.textbrowser_output = QTextBrowser(self.groupBox)
        self.textbrowser_output.setObjectName(u"textbrowser_output")
        self.textbrowser_output.setGeometry(QRect(20, 30, 351, 471))
        self.textbrowser_output.setFont(font)
        self.tabWidget.addTab(self.tab_cal, "")
        self.tab_feed = QWidget()
        self.tab_feed.setObjectName(u"tab_feed")
        self.groupBox_2 = QGroupBox(self.tab_feed)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 40, 921, 481))
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 30, 861, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineedit_path = QLineEdit(self.layoutWidget2)
        self.lineedit_path.setObjectName(u"lineedit_path")

        self.horizontalLayout.addWidget(self.lineedit_path)

        self.load_stra_button_2 = QPushButton(self.layoutWidget2)
        self.load_stra_button_2.setObjectName(u"load_stra_button_2")
        sizePolicy3.setHeightForWidth(self.load_stra_button_2.sizePolicy().hasHeightForWidth())
        self.load_stra_button_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.load_stra_button_2)

        self.tableview_stra = QTableView(self.groupBox_2)
        self.tableview_stra.setObjectName(u"tableview_stra")
        self.tableview_stra.setGeometry(QRect(20, 270, 256, 192))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 861, 194))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textbrowser_stra = QTextBrowser(self.widget)
        self.textbrowser_stra.setObjectName(u"textbrowser_stra")

        self.horizontalLayout_2.addWidget(self.textbrowser_stra)

        self.verticalScrollBar = QScrollBar(self.widget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalScrollBar)

        self.tabWidget.addTab(self.tab_feed, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\"\u751f\u7269\u8fc7\u7a0b\u8865\u6599\u8ba1\u7b97\u5668\"", None))
        self.show_box.setTitle(QCoreApplication.translate("MainWindow", u"\u5c06\u6267\u884c\u7684\u8865\u6599\u7b56\u7565\uff1a", None))
        self.Input_box.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u53c2\u6570\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u91cf\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u524d_\u4f53\u7cfb\u8d28\u91cf\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4f53\u7cfb\u5269\u4f59\u8461\u8404\u7cd6\uff1a", None))
        self.combox_sampling.setItemText(0, QCoreApplication.translate("MainWindow", u"mL", None))
        self.combox_sampling.setItemText(1, QCoreApplication.translate("MainWindow", u"\u03bcL", None))
        self.combox_sampling.setItemText(2, QCoreApplication.translate("MainWindow", u"L", None))

        self.combox_before_sampling.setItemText(0, QCoreApplication.translate("MainWindow", u"mL", None))
        self.combox_before_sampling.setItemText(1, QCoreApplication.translate("MainWindow", u"L", None))
        self.combox_before_sampling.setItemText(2, QCoreApplication.translate("MainWindow", u"\u03bcL", None))
        self.combox_before_sampling.setItemText(3, QCoreApplication.translate("MainWindow", u"g", None))
        self.combox_before_sampling.setItemText(4, QCoreApplication.translate("MainWindow", u"kg", None))
        self.combox_before_sampling.setItemText(5, QCoreApplication.translate("MainWindow", u"mg", None))

        self.combox_before_sampling_2.setItemText(0, QCoreApplication.translate("MainWindow", u"g/L", None))
        self.combox_before_sampling_2.setItemText(1, QCoreApplication.translate("MainWindow", u"mg/L", None))
        self.combox_before_sampling_2.setItemText(2, QCoreApplication.translate("MainWindow", u"mg/mL", None))
        self.combox_before_sampling_2.setItemText(3, QCoreApplication.translate("MainWindow", u"g/mL", None))
        self.combox_before_sampling_2.setItemText(4, QCoreApplication.translate("MainWindow", u"kg/L", None))
        self.combox_before_sampling_2.setItemText(5, QCoreApplication.translate("MainWindow", u"kg/mL", None))

        self.spinbox_sampling.setSuffix("")
        self.spinbox_sampling.setPrefix("")
        self.load_stra_button.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b56\u7565", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u8f93\u51fa\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cal), QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u5668", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.lineedit_path.setText("")
        self.lineedit_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u52a0\u8f7d\u6587\u4ef6\u76ee\u5f55", None))
        self.load_stra_button_2.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b56\u7565", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_feed), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8865\u6599\u7b56\u7565", None))
    # retranslateUi

