from PyQt4 import QtGui
import os
import json
import sys
import designer
import utils

KEY_DOCUMENTS = 'documents'
KEY_CATEGORIES = 'categories'
KEY_ERROR = 'error'
config = None


class LoadDialog(designer.loadDialog):
    def browseDocuments(self):
        global documents_directory
        directory = QtGui.QFileDialog.getExistingDirectory(
            self,
            "Pick a filder with documents",
            config[KEY_DOCUMENTS]
        )

        if directory:
            print("New documents directory %s" % directory)
            self.documents_directory = directory
            self.documentsPath.setText(directory)
            config[KEY_DOCUMENTS] = directory

    def browseCategories(self):
        global categories_directory
        directory = QtGui.QFileDialog.getExistingDirectory(
            self,
            "Pick a folder with categories",
            config[KEY_CATEGORIES]
        )

        if directory:
            print("New categories directory %s" % directory)
            self.categories_directory = directory
            self.categoriesPath.setText(directory)
            config[KEY_CATEGORIES] = directory

    def loadMainDialog(self):
        save_configuration()
        mainDialog = MainDialog()
        mainDialog.show()
        mainDialog.setupMainWindow()
        mainDialog.populateDocument()
        mainDialog.populateList()
        self.close()


class MainDialog(designer.mainDialog):

    def setupMainWindow(self):
        self.setWindowTitle("Classifier")

        self.documents_directory = utils.directory(config[KEY_DOCUMENTS])
        self.documents = self.documents_directory.get_all_files()

        self.categories_directory = utils.directory(config[KEY_CATEGORIES])
        self.categories = self.categories_directory.get_all_directories()

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Z"), self, self.undoAction)

    def undoAction(self):
        self.undoStack.undo(self.documents)
        self.showRemainingItemsMessage()

    def showRemainingItemsMessage(self):
        self.statusBar.showMessage(str(len(self.documents)) + " items remaining")

    def populateDocument(self):
        path = self.documents_directory.path
        name = self.documents[0]
        file = utils.file(path, name)
        print("Opening file %s" % file.full_name)
        content = file.read()
        self.documentView.setHtml(content)
        self.showRemainingItemsMessage()

    def populateList(self):
        # self.icon = QtGui.QIcon('icon.png')
        model = QtGui.QStandardItemModel(self.categoriesListView)
        print("Loaded %d categories" % len(self.categories))
        for category in self.categories:
            item = QtGui.QStandardItem(category)
            model.appendRow(item)
        self.categoriesListView.setModel(model)

    def listItemSelected(self, index):
        self.showRemainingItemsMessage()
        old_path = config[KEY_DOCUMENTS]
        file_name = self.documents.pop(0)
        new_category = config[KEY_CATEGORIES] + "\\" + self.categories[index.row()]
        file = utils.file(old_path, file_name)
        undo_command = utils.undo(
            self.documentView,
            file,
            file.get_parent_directory().path
        )
        self.undoStack.push(undo_command)
        message = "Moving file %s to %s" % (file.name, new_category.split('\\')[-1])
        print(message)
        file.move(new_category)
        if len(self.documents) == 0:
            self.close()
        else:
            self.populateDocument()


def save_configuration():
    global config
    config_file = open('config.json', 'w')
    json.dump(config, config_file)
    config_file.close()


def load_config():
    global config
    configuration = {}

    try:
        config_file = open('config.json', 'r')
        configuration = json.load(config_file)
    except:
        pass
    finally:
        if (os.path.exists('config.json')):
            config_file.close()

    path = os.getcwd()
    configuration[KEY_ERROR] = False

    if KEY_CATEGORIES not in configuration or not os.path.exists(configuration[KEY_CATEGORIES]):
        print("key %s not found" % KEY_CATEGORIES)
        configuration[KEY_CATEGORIES] = path
        configuration[KEY_ERROR] = True

    if KEY_DOCUMENTS not in configuration or not os.path.exists(configuration[KEY_DOCUMENTS]):
        print("key %s not found" % KEY_DOCUMENTS)
        configuration[KEY_DOCUMENTS] = path
        configuration[KEY_ERROR] = True

    config = configuration

app = QtGui.QApplication(sys.argv)

mainDialog = None
loadDialog = None


def main():
    global config

    load_config()

    if config[KEY_ERROR]:
        print(config)
        print("Opening load dialog")
        loadDialog = LoadDialog(
            documentsDirectory=config[KEY_DOCUMENTS],
            categoriesDirectory=config[KEY_CATEGORIES]
        )
        loadDialog.show()
    else:
        mainDialog = MainDialog()
        mainDialog.show()
        mainDialog.setupMainWindow()
        mainDialog.populateDocument()
        mainDialog.populateList()

    app.exec_()

if __name__ == '__main__':
    main()
