from PyQt4 import QtGui

import os
import codecs


class file():
    def __init__(self, path, name=None):
        if name is None:
            self.full_name = path
            self.name = path.reverse().split("\\", 1)[0].reverse()
            self.path = path.reverse().split("\\", 1)[1].reverse()
        else:
            self.full_name = path + "\\" + name

            self.path = path
            self.name = name

    def read(self):
        f = codecs.open(self.full_name, encoding='utf-8', mode='r')
        output = f.read()
        f.close()
        return output

    def move(self, path):
        new_name = path+"\\" + self.name
        os.rename(self.full_name, new_name)
        self.path = path
        self.full_name = new_name

    def get_parent_directory(self):
        return directory(self.path)


class directory():
    def __init__(self, path=None):
        if path is None:
            path = os.getcwd()
        self.name = path.split('\\')[-1]
        self.path = path

    def get_all_files(self):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            f.extend(filenames)
            break
        return f

    def get_all_directories(self):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            f.extend(dirnames)
            break
        return f

    def get_file(self, name):
        if name in self.get_all_files():
            return file(self.path, name)
        else:
            return None

    def get_directory(self, name):
        if name in self.get_all_directories():
            return directory(self.path + "\\" + name)
        else:
            return None


class undo():
    def __init__(self, html_view, file, old_path):
        self.html_view = html_view
        self.file = file
        self.old_path = old_path

    def undo(self, file_list):
        self.file.move(self.old_path)
        file_list.insert(0, self.file.name)
        print("Moving %s back to %s" % (self.file.name, self.old_path))
        self.html_view.setHtml(self.file.read())

class UndoStack():
    def __init__(self):
        self.stack = []

    def push(self, undo_command):
        self.stack.insert(0, undo_command)
        
    def undo(self, file_list):
        if (self.isEmpty()):
            print("Undo stack empty")
            return False

        undo_command = self.stack.pop(0)
        undo_command.undo(file_list)
        return True

    def isEmpty(self):
        return len(self.stack) == 0

