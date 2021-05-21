from PyQt5 import QtCore, QtGui, QtWidgets


class addFunctions:
    def choose_map(self):
        # выбор страницы от кнопки
        sender = self.sender()
        page = sender.text()
        exec("self.stackedWidget.setCurrentWidget(self." + self.page_names[int(page)] + ")")
        # анимация кнопки
        for i in range(1, 3+1):
            exec("self.pushButton_page" + str(i) + ".resize(37, 27)")
        exec("self.pushButton_page" + page + ".resize(37, 32)")

    def set_map(self, page):
        # выбор страницы от любой части кода
        exec("self.stackedWidget.setCurrentWidget(self." + self.page_names[int(page)] + ")")
        # анимация кнопки
        for i in range(1, 3+1):
            exec("self.pushButton_page" + str(i) + ".resize(37, 27)")
        exec("self.pushButton_page" + page + ".resize(37, 32)")

    def resize_map(self):
        x = self.horizontalSlider_size.value() / 20  # коэффицент увеличения

        # карты
        for i in self.original_sizes_maps.keys():
            exec("self." + i + ".setGeometry(self.offset_x, self.offset_y, int(self.original_sizes_maps[i][0]) * x, int(self.original_sizes_maps[i][1]) * x)")
        # кабинеты
        for i in self.original_sizes_rooms.keys():
            exec("self." + i + ".setGeometry((int(self.original_sizes_rooms[i][0]) * x) + self.offset_x, (int(self.original_sizes_rooms[i][1]) * x) + self.offset_y, int(self.original_sizes_rooms[i][2]) * x, int(self.original_sizes_rooms[i][3]) * x)")

        # смещение карты к центру
        cof = (self.horizontalSlider_size.value() - self.last_size) * 20
        self.offset_x -= cof
        self.offset_y -= cof

        self.last_size = self.horizontalSlider_size.value()  # задание прошлого размера

    def show_maximize(self):
        #  развернуть окно на весь экран ИЛИ вернуть изначальный размер
        if not self.maximazed:
            self.showMaximized()
            self.maximazed = True
        elif self.maximazed:
            self.showNormal()
            self.maximazed = False

    def find_room(self):
        # вернуть цвет прошлому найденному кабинету
        if self.last_found != "":
            exec("self." + self.last_found + ".setStyleSheet(self.stylesheet_alpha)")

        name = self.lineEdit_findName.text()  # имя искомого кабинета

        # цикл идет по кабинетам, и при нахождении нужного, выделяет его зеленым цветом и центрирует на нем экран
        for i in self.original_sizes_rooms.keys():
            if self.original_sizes_rooms[i][5] == name:
                self.horizontalSlider_size.setValue(20)
                self.offset_x = ((self.stackedWidget.width() // 2) - int(self.original_sizes_rooms[i][0]) - 100)
                self.offset_y = ((self.stackedWidget.height() // 2) - int(self.original_sizes_rooms[i][1]) - 100)
                self.set_map(self.original_sizes_rooms[i][4])
                self.resize_map()
                exec("self." + i + ".setStyleSheet(self.stylesheet_green)")
                self.last_found = i
                break
