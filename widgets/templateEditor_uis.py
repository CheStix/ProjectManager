# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python Project\Workshop's_Python_PyQt\SimpleWidget\projectManager\widgets\templateEditor.ui',
# licensing of 'D:\Python Project\Workshop's_Python_PyQt\SimpleWidget\projectManager\widgets\templateEditor.ui' applies.
#
# Created: Thu Oct 17 10:51:07 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        templateEditor.setObjectName("templateEditor")
        templateEditor.resize(274, 411)
        self.verticalLayout = QtWidgets.QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_btn = QtWidgets.QPushButton(templateEditor)
        self.add_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_2.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QPushButton(templateEditor)
        self.remove_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout_2.addWidget(self.remove_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tree = QtWidgets.QTreeWidget(templateEditor)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "1")
        self.tree.header().setVisible(False)
        self.verticalLayout.addWidget(self.tree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_btn = QtWidgets.QPushButton(templateEditor)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.close_btn = QtWidgets.QPushButton(templateEditor)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(templateEditor)
        QtCore.QMetaObject.connectSlotsByName(templateEditor)

    def retranslateUi(self, templateEditor):
        templateEditor.setWindowTitle(QtWidgets.QApplication.translate("templateEditor", "Template Editor", None, -1))
        self.add_btn.setText(QtWidgets.QApplication.translate("templateEditor", "+", None, -1))
        self.remove_btn.setText(QtWidgets.QApplication.translate("templateEditor", "-", None, -1))
        self.save_btn.setText(QtWidgets.QApplication.translate("templateEditor", "Save", None, -1))
        self.close_btn.setText(QtWidgets.QApplication.translate("templateEditor", "Close", None, -1))

