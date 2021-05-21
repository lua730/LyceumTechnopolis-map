from PyQt5 import QtGui


class addStyles:
    def add_styles(self):
        # Создание стилей
        self.stylesheet_green = "QPushButton {\n" \
                            "    border: 0px;\n" \
                            "    background-color: rgba(0, 255, 0, 50);\n" \
                            "}\n" \
                            "QPushButton:pressed {\n" \
                            "    background-color: rgba(0, 255, 0, 50);\n}"
        self.stylesheet_alpha = "QPushButton {\n"\
                                "    border: 0px;\n"\
                                "    background-color: rgba(255, 255, 255, 0);\n"\
                                "}\n"\
                                "QPushButton:pressed {\n"\
                                "    background-color: rgba(0, 0, 0, 10);\n}"

        # Присвоение стилей и шрифтов
        QtGui.QFontDatabase.addApplicationFont('sources/fonts/Proxima Nova.otf')
        self.label_name.setFont(QtGui.QFont("Proxima Nova", 12))
        self.label_2.setFont(QtGui.QFont("Proxima Nova", 12))
        self.label_4.setFont(QtGui.QFont("Proxima Nova", 12))
        self.pushButton_find.setFont(QtGui.QFont("Proxima Nova", 12))
        self.pushButton_page1.setFont(QtGui.QFont("Proxima Nova", 12))
        self.pushButton_page2.setFont(QtGui.QFont("Proxima Nova", 12))
        self.pushButton_page3.setFont(QtGui.QFont("Proxima Nova", 12))
