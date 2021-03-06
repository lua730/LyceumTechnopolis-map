# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_100x100.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: #FFF;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_main = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_main.setGeometry(QtCore.QRect(0, 25, 801, 581))
        self.groupBox_main.setStyleSheet("QGroupBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background-color: #FFF;\n"
"\n"
"}")
        self.groupBox_main.setTitle("")
        self.groupBox_main.setObjectName("groupBox_main")
        self.label_corner = QtWidgets.QLabel(self.groupBox_main)
        self.label_corner.setGeometry(QtCore.QRect(790, 560, 16, 20))
        self.label_corner.setStyleSheet("")
        self.label_corner.setObjectName("label_corner")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_main)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 40, 771, 531))
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: #FFF;\n"
"    border: 1px solid black;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalSlider_size = QtWidgets.QSlider(self.groupBox_main)
        self.horizontalSlider_size.setGeometry(QtCore.QRect(80, 10, 160, 22))
        self.horizontalSlider_size.setStyleSheet("")
        self.horizontalSlider_size.setMinimum(10)
        self.horizontalSlider_size.setMaximum(50)
        self.horizontalSlider_size.setProperty("value", 20)
        self.horizontalSlider_size.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_size.setObjectName("horizontalSlider_size")
        self.label_2 = QtWidgets.QLabel(self.groupBox_main)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_main)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 51, 21))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.lineEdit_findName = QtWidgets.QLineEdit(self.groupBox_main)
        self.lineEdit_findName.setGeometry(QtCore.QRect(440, 10, 271, 21))
        self.lineEdit_findName.setObjectName("lineEdit_findName")
        self.pushButton_find = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_find.setGeometry(QtCore.QRect(721, 5, 61, 31))
        self.pushButton_find.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_find.setObjectName("pushButton_find")
        self.pushButton_page1 = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_page1.setGeometry(QtCore.QRect(300, 5, 37, 32))
        self.pushButton_page1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page1.setObjectName("pushButton_page1")
        self.pushButton_page2 = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_page2.setGeometry(QtCore.QRect(345, 5, 37, 27))
        self.pushButton_page2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page2.setObjectName("pushButton_page2")
        self.pushButton_page3 = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_page3.setGeometry(QtCore.QRect(390, 5, 37, 27))
        self.pushButton_page3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page3.setObjectName("pushButton_page3")
        self.groupBox_title = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_title.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.groupBox_title.setStyleSheet("QGroupBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background-color:rgb(78, 124, 255)\n"
"}")
        self.groupBox_title.setTitle("")
        self.groupBox_title.setObjectName("groupBox_title")
        self.label_name = QtWidgets.QLabel(self.groupBox_title)
        self.label_name.setGeometry(QtCore.QRect(5, 3, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("QLabel {\n"
"    color: #FFF;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_name.setObjectName("label_name")
        self.exitAppButton = QtWidgets.QPushButton(self.groupBox_title)
        self.exitAppButton.setGeometry(QtCore.QRect(780, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitAppButton.setFont(font)
        self.exitAppButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #FFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(69, 69, 106);\n"
"}")
        self.exitAppButton.setObjectName("exitAppButton")
        self.minimizeButton = QtWidgets.QPushButton(self.groupBox_title)
        self.minimizeButton.setGeometry(QtCore.QRect(740, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #FFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(69, 69, 106);\n"
"}")
        self.minimizeButton.setObjectName("minimizeButton")
        self.maximizeButton = QtWidgets.QPushButton(self.groupBox_title)
        self.maximizeButton.setGeometry(QtCore.QRect(760, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.maximizeButton.setFont(font)
        self.maximizeButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #FFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(69, 69, 106);\n"
"}")
        self.maximizeButton.setObjectName("maximizeButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lua730"))
        self.label_corner.setText(_translate("MainWindow", ".:"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">????????????:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">????????:</span></p></body></html>"))
        self.pushButton_find.setText(_translate("MainWindow", "??????????"))
        self.pushButton_page1.setText(_translate("MainWindow", "1"))
        self.pushButton_page2.setText(_translate("MainWindow", "2"))
        self.pushButton_page3.setText(_translate("MainWindow", "3"))
        self.label_name.setText(_translate("MainWindow", "<html><head/><body><p>?????????? ?????????? ??????????????????????</p></body></html>"))
        self.exitAppButton.setText(_translate("MainWindow", "X"))
        self.minimizeButton.setText(_translate("MainWindow", "_"))
        self.maximizeButton.setText(_translate("MainWindow", "???"))
