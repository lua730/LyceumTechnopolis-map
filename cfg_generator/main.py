import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.rooms_export = "# x y width height page text\n"
        self.maps_export = "# width heigth filepath page\n"

        f = open("files.txt", "r")
        text = f.read().splitlines()
        f.close()

        for i in text:
            uic.loadUi(i, self)
            self.export_objectNames(i)
            self.delete_objects()

        f = open("export/rooms_coordinates.txt", "w")
        f.write(self.rooms_export)
        f.close()

        f = open("export/maps_names_sizes.txt", "w")
        f.write(self.maps_export)
        f.close()

        sys.exit()

    def delete_objects(self):
        children = self.findChildren(QtWidgets.QPushButton) + self.findChildren(QtWidgets.QLabel) + self.findChildren(QtWidgets.QLineEdit)
        for child in children:
            exec("self." + child.objectName() + ".setParent(None)")
            exec("self." + child.objectName() + ".deleteLater()")


    def export_objectNames(self, ui_name):
        children = self.findChildren(QtWidgets.QPushButton)
        for child in children:
            info = []
            exec("info.append(self." + str(child.objectName()) + ".x())")
            exec("info.append(self." + str(child.objectName()) + ".y())")
            exec("info.append(self." + str(child.objectName()) + ".width())")
            exec("info.append(self." + str(child.objectName()) + ".height())")
            info.append(ui_name[:-3])
            exec("info.append(self." + str(child.objectName()) + ".text())")
            self.rooms_export += " ".join(list(map(str, info))) + "\n"

        info = []
        children = self.findChildren(QtWidgets.QLabel)
        for child in children:
            exec("info.append(self." + str(child.objectName()) + ".width())")
            exec("info.append(self." + str(child.objectName()) + ".height())")
        children = self.findChildren(QtWidgets.QLineEdit)
        for child in children:
            exec("info.append(self." + str(child.objectName()) + ".text().split()[0])")
        exec("info.append('" + str(ui_name[:-3]) + "')")
        self.maps_export += " ".join(list(map(str, info))) + "\n"

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
