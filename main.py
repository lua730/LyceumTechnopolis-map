from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file import Ui_MainWindow
import sys


# Подключение модулей
from modules.add_map import addMap
from modules.add_styles import addStyles
from modules.frameless_window_stuff import framelessWindow
from modules.catch_events import catchEvents
from modules.functions import addFunctions
from modules.connect_buttons import connectButtons


class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #  переменные размеров
        self.title_heigth = self.groupBox_title.size().height()  # высота заголовка
        self.original_sizes_maps = dict()  # оригинальные размеры элементов (для масштабирования)
        self.original_sizes_rooms = dict()
        self.offset_x = 100  # отступы для движения карты
        self.offset_y = 100

        self.last_found = ""  # последний найденный кабинет
        self.last_size = self.horizontalSlider_size.value()  # последний размер карты

        self.page_names = ["page_0", "page_1", "page_2", "page_3"]    # object-name страниц в stackedWidget

        addStyles.add_styles(self)  # добавление стилей из файда add_styles.py
        addMap.add_map(self)  # добавление карт из файла add_map.py
        framelessWindow.make_frameless(self)  # создание безрамочного окна через frameless_window_stuff.py
        connectButtons.connect_buttons(self)  # добавление функций кнопкам

    # объявление функций через functions.py
    def choose_map(self):
        addFunctions.choose_map(self)

    def set_map(self, page):
        addFunctions.set_map(self, page)

    def resize_map(self):
        addFunctions.resize_map(self)

    def show_maximize(self):
        addFunctions.show_maximize(self)

    def find_room(self):
        addFunctions.find_room(self)

    # использованеие events с помощью catch_events.py
    def resizeEvent(self, event):
        catchEvents.resizeEvent(self, event)

    def mousePressEvent(self, event):
        catchEvents.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        catchEvents.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        catchEvents.mouseReleaseEvent(self, event)

    def wheelEvent(self, event):
        catchEvents.wheelEvent(self, event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
