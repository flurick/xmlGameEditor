import sys
import os
import fnmatch
#libs
from bs4 import BeautifulSoup 
from PySide.QtCore import *
from PySide.QtGui import *
#modules
import mainwindow
import util
import gmx

groupTags = ["sprites", "sounds", "backgrounds", "paths", "scripts", 
             "shaders", "fonts", "timelines", "objects"]
assetTags = ["sprite", "sound", "background", "path", "script", 
             "shader", "font", "timeline", "object"]
#assetTags = ["object"]
objectTags = ["event"]
pathTags = ["point"]
roomTags = ["code"]
eventType = {"0": "someevent"}
actionID = {"604": "someaction"}

Testing=True
TestingID=1
def test(msg, id=0):
    if TestingID == 0:
        print(msg)
    elif TestingID == id:
        print(msg)
    else:
        pass

class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.groups.currentRowChanged.connect(self.listAssets)
        self.ui.assets.currentRowChanged.connect(self.listProperties) #TODO fix trigger when deselected, alternative qt api seems broken in this pyside?
        self.ui.events.currentRowChanged.connect(self.listActions)

        self.getProjectFile()
        self.listGroups()
        self.ui.groups.setCurrentRow(5)

    def findGMX(self):
        test("not implemented")

    def getProjectFile(self):
        test("load project file")
        self.path = "../../mmxv.gmx/mmxv.project.gmx"  # sys.argv[1]
        try:
            ProjectFile = open(self.path)
            self.tmpProjectFile = ProjectFile.read()
            ProjectFile.close()
        except:
            print("Failed to open gmx file.")
            sys.exit(app.exec_())


    def listGroups(self):
        test("list groups")
        self.ui.assets.clear()
        self.ui.events.clear()
        self.soup = BeautifulSoup(self.tmpProjectFile, 'xml')
        for tag in self.soup.find_all(groupTags):
            self.ui.groups.addItem(tag.name)

    def listAssets(self):
        test("list assets")
        group = self.ui.groups.currentItem().text()
        group = group[:-1] #get items not everything as one big blob
        self.ui.statusbar.showMessage("Assets of " + group)
        self.soup = BeautifulSoup(self.tmpProjectFile, 'lxml')
        
        self.ui.assets.clear()
        self.ui.events.clear()
        for tag in self.soup.find_all(group):
            group, name = tag.text.split('\\')
            self.ui.assets.addItem(name)
        self.ui.assets.sortItems()

    def listProperties(self):
        test("list props")
        asset = self.ui.assets.currentItem()
        #group, name = asset.text().split('\\')
        group = self.ui.groups.currentItem().text()
        name = self.ui.assets.currentItem().text()

        # load assets xml file
        self.ui.statusbar.showMessage("Properties of " + group + " " + name)
        dir = os.path.dirname(os.path.abspath(self.path))
        if (group == "objects"):
            group = group[:-1]
            assetPath = os.path.join(dir, group+"s", name+"."+group+".gmx")
            assetFile = open(assetPath)
            self.soup = BeautifulSoup(assetFile, 'lxml')
        elif (group == "scripts"):
            group = group[:-1]
            assetPath = os.path.join(dir, group+"s", name)
            assetFile = open(assetPath)

        # show properties and events
        if (group == "object"):

            self.ui.events.clear()
            for tag in self.soup.find_all("event"):
                self.ui.events.addItem(gmx.eventNumber[tag['eventtype']]) #tag>eventtype lookedup in gmx dictionary
           
            self.ui.objSprite.clear()
            self.ui.objSprite.addItem(self.soup.find("spritename").contents[0])

            self.ui.objMask.clear()
            self.ui.objMask.addItem(self.soup.find("maskname").contents[0])

            self.ui.objParent.clear()
            self.ui.objParent.addItem(self.soup.find("parentname").contents[0])

            util.check(self.ui.objSolid, self.soup.find("solid").contents[0])
            util.check(self.ui.objPhysics, self.soup.find("physicsobject").contents[0])
            util.check(self.ui.objVisible, self.soup.find("visible").contents[0])
            util.check(self.ui.objPersistent, self.soup.find("persistent").contents[0])

            #self.ui.objChildren.clear()
            #for child in gmx.children():
            #    self.ui.objChildren.addItem(child)

        elif (group == "script"):
            self.ui.code.setText(assetFile.read())

        # clean
        try: assetFile.close()
        finally: test("Closed")

    def listActions(self):
        test("list actions")
        index = self.ui.events.currentRow()
        action = self.soup.find_all("action")[index]
        #self.soup.select("action:nth-of-type("+str(index+1)+")")
        #for tag in action:
        #    print(tag)
        print(action)
        text = action.string
        self.ui.code.setText(str(action))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlMainWindow()
    window.show()
    sys.exit(app.exec_())
