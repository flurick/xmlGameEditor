# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Nov 16 10:39:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 538)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groups = QtGui.QListWidget(self.centralwidget)
        self.groups.setObjectName("groups")
        self.horizontalLayout.addWidget(self.groups)
        self.assets = QtGui.QListWidget(self.centralwidget)
        self.assets.setObjectName("assets")
        self.horizontalLayout.addWidget(self.assets)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.events = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.events.sizePolicy().hasHeightForWidth())
        self.events.setSizePolicy(sizePolicy)
        self.events.setObjectName("events")
        self.verticalLayout_2.addWidget(self.events)
        self.preview = QtGui.QGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setObjectName("preview")
        self.verticalLayout_2.addWidget(self.preview)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.objProperties = QtGui.QWidget()
        self.objProperties.setObjectName("objProperties")
        self.verticalLayout = QtGui.QVBoxLayout(self.objProperties)
        self.verticalLayout.setObjectName("verticalLayout")
        self.objSprite = QtGui.QComboBox(self.objProperties)
        self.objSprite.setObjectName("objSprite")
        self.verticalLayout.addWidget(self.objSprite)
        self.objParent = QtGui.QComboBox(self.objProperties)
        self.objParent.setObjectName("objParent")
        self.verticalLayout.addWidget(self.objParent)
        self.objMask = QtGui.QComboBox(self.objProperties)
        self.objMask.setObjectName("objMask")
        self.verticalLayout.addWidget(self.objMask)
        self.objChildren = QtGui.QComboBox(self.objProperties)
        self.objChildren.setObjectName("objChildren")
        self.verticalLayout.addWidget(self.objChildren)
        self.objSolid = QtGui.QCheckBox(self.objProperties)
        self.objSolid.setObjectName("objSolid")
        self.verticalLayout.addWidget(self.objSolid)
        self.objPhysics = QtGui.QCheckBox(self.objProperties)
        self.objPhysics.setObjectName("objPhysics")
        self.verticalLayout.addWidget(self.objPhysics)
        self.objVisible = QtGui.QCheckBox(self.objProperties)
        self.objVisible.setObjectName("objVisible")
        self.verticalLayout.addWidget(self.objVisible)
        self.objPersistent = QtGui.QCheckBox(self.objProperties)
        self.objPersistent.setObjectName("objPersistent")
        self.verticalLayout.addWidget(self.objPersistent)
        self.tabWidget.addTab(self.objProperties, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.code = QtGui.QTextEdit(self.centralwidget)
        self.code.setObjectName("code")
        self.horizontalLayout.addWidget(self.code)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.objSolid.setText(QtGui.QApplication.translate("MainWindow", "Solid", None, QtGui.QApplication.UnicodeUTF8))
        self.objPhysics.setText(QtGui.QApplication.translate("MainWindow", "Physics", None, QtGui.QApplication.UnicodeUTF8))
        self.objVisible.setText(QtGui.QApplication.translate("MainWindow", "Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.objPersistent.setText(QtGui.QApplication.translate("MainWindow", "Persistent", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.objProperties), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.code.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">101</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

