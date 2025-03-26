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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.show_box = QGroupBox(self.tab)
        self.show_box.setObjectName(u"show_box")
        self.show_box.setGeometry(QRect(30, 30, 401, 500))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.show_box.sizePolicy().hasHeightForWidth())
        self.show_box.setSizePolicy(sizePolicy1)
        self.tableWidget = QTableWidget(self.show_box)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 40, 256, 192))
        self.widget = QWidget(self.show_box)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 280, 311, 131))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_4.addWidget(self.textBrowser)

        self.textBrowser_3 = QTextBrowser(self.widget)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_4.addWidget(self.textBrowser_3)

        self.textBrowser_2 = QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_4.addWidget(self.textBrowser_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.Input_box = QGroupBox(self.tab)
        self.Input_box.setObjectName(u"Input_box")
        self.Input_box.setGeometry(QRect(519, 30, 431, 500))
        self.calculate_button = QPushButton(self.Input_box)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setGeometry(QRect(220, 420, 100, 50))
        self.widget1 = QWidget(self.Input_box)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 40, 360, 151))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.spinBox = QSpinBox(self.widget1)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(10)

        self.verticalLayout_3.addWidget(self.spinBox)

        self.doubleSpinBox = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBox.setMaximum(100000.000000000000000)
        self.doubleSpinBox.setSingleStep(0.050000000000000)
        self.doubleSpinBox.setValue(1200.000000000000000)

        self.verticalLayout_3.addWidget(self.doubleSpinBox)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.doubleSpinBox_2.setMaximum(100000.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.050000000000000)
        self.doubleSpinBox_2.setValue(1200.000000000000000)

        self.verticalLayout_3.addWidget(self.doubleSpinBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox = QComboBox(self.widget1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setModelColumn(3)

        self.verticalLayout_6.addWidget(self.comboBox)

        self.comboBox_3 = QComboBox(self.widget1)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_6.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox(self.widget1)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_6.addWidget(self.comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\"\u751f\u7269\u8fc7\u7a0b\u8865\u6599\u8ba1\u7b97\u5668\"", None))
        self.show_box.setTitle(QCoreApplication.translate("MainWindow", u"\u5c06\u6267\u884c\u7684\u8865\u6599\u7b56\u7565\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u524d_\u4f53\u7cfb\u8d28\u91cf\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u91cf\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u540e_\u4f53\u7cfb\u8d28\u91cf\uff1a", None))
        self.Input_box.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u53c2\u6570\uff1a", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u91cf\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u524d_\u4f53\u7cfb\u8d28\u91cf\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6837\u540e_\u4f53\u7cfb\u8d28\u91cf\uff1a", None))
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u8865\u6599\u7b56\u7565", None))
    # retranslateUi

