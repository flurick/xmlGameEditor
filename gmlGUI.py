#!/bin/python
import sys
from bs4 import BeautifulSoup
from PySide.QtCore import *
from PySide.QtGui import *

assetTags = ["prite", "sound", "background", "path", "script",
             "shader", "font", "timeline", "object"]
objectTags = ["event"]
pathTags = ["point"]
roomTags = ["code"]


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        #self.columns = ["a"]
        self.button = QPushButton("+")
        self.button1 = QPushButton("-")
        self.text = QTextBrowser()
        # asset model
        self.col1 = QListView()
        self.assetModel = QStandardItemModel(self.col1)
        self.col1.setModel(self.assetModel)
        self.col1sel = self.col1.selectionModel()
        # event model
        self.col2 = QListView()
        self.eventModel = QStandardItemModel(self.col2)
        self.col2.setModel(self.eventModel)

        layout = QHBoxLayout()
        layout.addWidget(self.col1)
        layout.addWidget(self.col2)
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        self.setLayout(layout)

        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("gml")

        self.col1sel.selectionChanged.connect(self.listEvents)
        self.button.clicked.connect(self.addCol)
        self.button1.clicked.connect(self.clearEvents)

        page = "../mmxv.gmx/mmxv.project.gmx"  # sys.argv[1]
        ProjectFile = open(page)
        self.tmpProjectFile = ProjectFile.read()
        ProjectFile.close()

        self.soup = BeautifulSoup(self.tmpProjectFile, 'lxml')
        assets.addItems(["a","b"])
        #for asset in self.soup.find_all(assetTags):
        #    item = QStandardItem(asset.text)
        #    self.assetModel.appendRow(item)


    def listEvents(self):
        self.text.setText(self.tmpProjectFile)
        self.eventModel.clear()
        for asset in self.soup.find_all():
            item = QStandardItem(asset.text)
            self.eventModel.appendRow(item)

    def clearEvents(self):
        self.eventModel.clear()

    def addCol(self):
        item = QStandardItem("New Object")
        self.eventModel.appendRow(item)

    def updateUI(self):
        try:
            text = self.lineedit.text()
            self.browser.append(text)
        except:
            self.browser.append("nope")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
