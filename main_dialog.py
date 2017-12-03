# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_dialog.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(955, 635)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(955, 610))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setSizeIncrement(QtCore.QSize(0, -1))
        self.horizontalFrame.setAutoFillBackground(True)
        self.horizontalFrame.setObjectName(_fromUtf8("horizontalFrame"))
        self.parent_layout = QtGui.QHBoxLayout(self.horizontalFrame)
        self.parent_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.parent_layout.setMargin(5)
        self.parent_layout.setSpacing(5)
        self.parent_layout.setObjectName(_fromUtf8("parent_layout"))
        self.documentView = QtWebKit.QWebView(self.horizontalFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.documentView.sizePolicy().hasHeightForWidth())
        self.documentView.setSizePolicy(sizePolicy)
        self.documentView.setMinimumSize(QtCore.QSize(800, 600))
        self.documentView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.documentView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.documentView.setZoomFactor(2.0)
        self.documentView.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.documentView.setObjectName(_fromUtf8("documentView"))
        self.parent_layout.addWidget(self.documentView)
        self.categoriesListView = QtGui.QListView(self.horizontalFrame)
        self.categoriesListView.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.categoriesListView.sizePolicy().hasHeightForWidth())
        self.categoriesListView.setSizePolicy(sizePolicy)
        self.categoriesListView.setMinimumSize(QtCore.QSize(150, 600))
        self.categoriesListView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.categoriesListView.setFont(font)
        self.categoriesListView.setAutoFillBackground(True)
        self.categoriesListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.categoriesListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.categoriesListView.setAlternatingRowColors(True)
        self.categoriesListView.setIconSize(QtCore.QSize(0, 0))
        self.categoriesListView.setViewMode(QtGui.QListView.ListMode)
        self.categoriesListView.setUniformItemSizes(True)
        self.categoriesListView.setWordWrap(True)
        self.categoriesListView.setObjectName(_fromUtf8("categoriesListView"))
        self.parent_layout.addWidget(self.categoriesListView)
        self.parent_layout.setStretch(0, 1)
        self.gridLayout.addWidget(self.horizontalFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

from PyQt4 import QtWebKit
