# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python Project\Workshop's_Python_PyQt\SimpleWidget\projectManager\widgets\settingsDialog.ui',
# licensing of 'D:\Python Project\Workshop's_Python_PyQt\SimpleWidget\projectManager\widgets\settingsDialog.ui' applies.
#
# Created: Wed Oct 16 11:02:17 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(604, 201)
        self.verticalLayout = QtWidgets.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(settingsDialog)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtWidgets.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtWidgets.QApplication.translate("settingsDialog", "Settings Dialog", None, -1))

