from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os
import settings, createProject


class projectListClass(QListWidget):
    def __init__(self):
        super(projectListClass, self).__init__()

    def updateProjectList(self,):
        self.clear()
        data = settings.settingsClass().load()
        path = data.get('path')
        if path:
            if os.path.exists(path):
                for f in os.listdir(path):
                    fullpath = os.path.join(path, f)
                    if self.isProject(fullpath):
                        item = self.addProject(f)
                        item.setData(32, fullpath)

            return True
        else:
            return False

    def isProject(self, path):
        return os.path.exists(os.path.join(path, createProject.projectFile))

    def addProject(self, name):
        item = QListWidgetItem()
        item.setText(name)
        self.addItem(item)
        return item



