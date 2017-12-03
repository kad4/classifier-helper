# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 226)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(640, 226))
        Dialog.setMaximumSize(QtCore.QSize(640, 226))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 621, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.categoriesPath = QtGui.QTextEdit(self.groupBox)
        self.categoriesPath.setGeometry(QtCore.QRect(10, 30, 491, 31))
        self.categoriesPath.setReadOnly(True)
        self.categoriesPath.setObjectName(_fromUtf8("categoriesPath"))
        self.browseCategoriesButton = QtGui.QPushButton(self.groupBox)
        self.browseCategoriesButton.setGeometry(QtCore.QRect(510, 30, 93, 31))
        self.browseCategoriesButton.setObjectName(_fromUtf8("browseCategoriesButton"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 621, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.documentsPath = QtGui.QTextEdit(self.groupBox_2)
        self.documentsPath.setGeometry(QtCore.QRect(10, 30, 491, 31))
        self.documentsPath.setReadOnly(True)
        self.documentsPath.setObjectName(_fromUtf8("documentsPath"))
        self.browseDocumentsButton = QtGui.QPushButton(self.groupBox_2)
        self.browseDocumentsButton.setGeometry(QtCore.QRect(510, 30, 93, 31))
        self.browseDocumentsButton.setObjectName(_fromUtf8("browseDocumentsButton"))
        self.loadButton = QtGui.QPushButton(Dialog)
        self.loadButton.setGeometry(QtCore.QRect(540, 190, 93, 28))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Categories Directory", None))
        self.browseCategoriesButton.setText(_translate("Dialog", "Browse", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Documents Directory", None))
        self.browseDocumentsButton.setText(_translate("Dialog", "Browse", None))
        self.loadButton.setText(_translate("Dialog", "Load", None))

