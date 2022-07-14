# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoMonUIJuVThs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 541)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 60, 256, 192))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 30, 251, 22))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(690, 50, 81, 81))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 80, 75, 23))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(350, 30, 105, 40))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbLoadNew = QRadioButton(self.widget)
        self.rbLoadNew.setObjectName(u"rbLoadNew")
        self.rbLoadNew.setChecked(True)

        self.verticalLayout.addWidget(self.rbLoadNew)

        self.rbLoadOld = QRadioButton(self.widget)
        self.rbLoadOld.setObjectName(u"rbLoadOld")

        self.verticalLayout.addWidget(self.rbLoadOld)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 784, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rbLoadNew.setText(QCoreApplication.translate("MainWindow", u"\ubaa9\ub85d \uac31\uc2e0", None))
        self.rbLoadOld.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\uaddc \ub18d\uc7a5 \ucc3e\uae30", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())