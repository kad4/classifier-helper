from PyQt4 import QtGui
import sys
import os

import utils

from load_dialog import Ui_Dialog
from main_dialog import Ui_MainWindow


class mainDialog(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.documentView.setFont(QtGui.QFont("Consolas"))

        self.categoriesListView.clicked.connect(self.listItemSelected)

        self.statusBar = QtGui.QStatusBar()
        self.setStatusBar(self.statusBar)
        # self.statusBar = QtGui.QStatusBar(self)
        self.undoStack = utils.UndoStack()

    def listItemSelected(index):
        pass


class loadDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None, categoriesDirectory=None, documentsDirectory=None):
        super(loadDialog, self).__init__(parent)
        self.setupUi(self)

        path = os.getcwd()

        print("Attempting to load categories from %s" % categoriesDirectory)

        if categoriesDirectory is None:
            print("Loading categories failed")
            categoriesDirectory = path

        print("Attempting to load documents from %s" % documentsDirectory)
        
        if documentsDirectory is None:
            print("Loading documents failed")
            documentsDirectory = path

        self.categoriesPath.setText(categoriesDirectory)
        self.documentsPath.setText(documentsDirectory)

        self.browseCategoriesButton.clicked.connect(self.browseCategories)
        self.browseDocumentsButton.clicked.connect(self.browseDocuments)
        self.loadButton.clicked.connect(self.loadMainDialog)

    def browseDocuments(self):
        pass

    def browseCategories(self):
        pass

    def loadMainDialog(self):
        pass
