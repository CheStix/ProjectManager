from PySide2.QtWidgets import *
from PySide2.QtCore import *

from widgets import settingsDialog_uis as ui
import settings


class settingsDialogClass(QDialog, ui.Ui_settingsDialog):
    def __init__(self, parrent):
        super(settingsDialogClass, self).__init__(parrent)
        self.setupUi(self)
        #ui
        self.table.setColumnCount(2)
        # start
        self.fillTable()

    def fillTable(self):
        data = settings.settingsClass().load()
        for key, value in data.items():
            self.addParm(key, value)

    def addParm(self, key, value):
        self.table.insertRow(self.table.rowCount())
        item = QTableWidgetItem()
        item.setText(key)
        self.table.setItem(self.table.rowCount()-1, 0, item)
        item = QTableWidgetItem()
        item.setText(value)
        self.table.setItem(self.table.rowCount() - 1, 1, item)

    def getTableData(self):
        data = dict()
        for i in range(0, self.table.rowCount()):
            key = self.table.item(i, 0).text()
            value = self.table.item(i, 1).text()
            data[key] = value
        return data




