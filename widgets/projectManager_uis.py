# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python Project\Workshop's_Python_PyQt\SimpleWidget\projectManager\widgets\projectManager.ui',
# licensing of 'D:\Python Project\Workshop's_Python_PyQt\SimpleWidget\projectManager\widgets\projectManager.ui' applies.
#
# Created: Tue Oct 15 14:23:20 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_projectManager(object):
    def setupUi(self, projectManager):
        projectManager.setObjectName("projectManager")
        projectManager.resize(428, 357)
        self.centralwidget = QtWidgets.QWidget(projectManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.projectList_ly = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.projectList_ly.setContentsMargins(0, 0, 0, 0)
        self.projectList_ly.setObjectName("projectList_ly")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_btn = QtWidgets.QPushButton(self.widget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.templateEditor_btn = QtWidgets.QPushButton(self.widget)
        self.templateEditor_btn.setObjectName("templateEditor_btn")
        self.verticalLayout.addWidget(self.templateEditor_btn)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_lb = QtWidgets.QLabel(self.groupBox)
        self.info_lb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_lb.setObjectName("info_lb")
        self.verticalLayout_3.addWidget(self.info_lb)
        self.verticalLayout.addWidget(self.groupBox)
        self.settings_btn = QtWidgets.QPushButton(self.widget)
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.verticalLayout_2.addWidget(self.splitter)
        projectManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(projectManager)
        QtCore.QMetaObject.connectSlotsByName(projectManager)

    def retranslateUi(self, projectManager):
        projectManager.setWindowTitle(QtWidgets.QApplication.translate("projectManager", "Project Manager", None, -1))
        self.create_btn.setText(QtWidgets.QApplication.translate("projectManager", "Create Project", None, -1))
        self.templateEditor_btn.setText(QtWidgets.QApplication.translate("projectManager", "Template Editor", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("projectManager", "Info", None, -1))
        self.info_lb.setText(QtWidgets.QApplication.translate("projectManager", "TextLabel", None, -1))
        self.settings_btn.setText(QtWidgets.QApplication.translate("projectManager", "Settings", None, -1))

