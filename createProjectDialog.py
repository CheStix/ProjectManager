from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets import createProject_uis as ui


class createProjectClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parrent):
        super(createProjectClass, self).__init__(parrent)
        self.setupUi(self)
        # connects
        self.create_btn.clicked.connect(self.doCreate)
        self.cancel_btn.clicked.connect(self.reject)

    def doCreate(self):
        if self.name_le.text():
            self.accept()

    def getDialogData(self):
        return dict(
            name=self.name_le.text(),
            comment=self.comment_te.toPlainText()
        )
