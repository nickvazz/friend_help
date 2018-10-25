# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testQt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 482)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 410, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(19, 79, 451, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 449, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(300, 40, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.listView = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.listView.setGeometry(QtCore.QRect(20, 30, 256, 192))
        self.listView.setObjectName("listView")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 70, 87, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox"))
