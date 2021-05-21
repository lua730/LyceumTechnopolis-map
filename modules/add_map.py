from PyQt5 import QtCore, QtGui, QtWidgets


class addMap():
    def add_map(self):
        #  Добавление карт
        # картинки
        f = open("cfg/maps_names_sizes.txt", "r")  # чтение из конфига
        maps_names_sizes = f.read().splitlines()
        f.close()
        for i in range(len(maps_names_sizes)):  # цикл идет по конфигу и создает картинки согласно ему
            a = maps_names_sizes[i].split()
            if a != []:
                if a[0] != "#":
                    pic_size = [int(a[0]), int(a[1])]
                    id = "map_label_" + a[3]
                    exec("self." + id + " = QtWidgets.QLabel(self." + self.page_names[int(a[3])] + ")")
                    exec("self." + id + ".setGeometry(0 + self.offset_x, 0 + self.offset_y, pic_size[0], pic_size[1])")
                    exec('self.' + id + '.setStyleSheet("background-color: rgba(255, 255, 255, 0);")')
                    exec("self." + id + '.setText("")')
                    exec("self." + id + ".setPixmap(QtGui.QPixmap(a[2]))")
                    exec("self." + id + ".setScaledContents(True)")
                    self.original_sizes_maps[id] = a

        # кнопки комнат
        f = open("cfg/rooms_coordinates.txt", "r")  # чтение из конфига
        rooms_coordinates = f.read().splitlines()
        f.close()
        self.rooms_numbers = []  # переменная, для хранения номеров кабинетов
        for i in range(len(rooms_coordinates)):  # цикл идет по конфигу и добавляет кабинеты согласно ему
            if rooms_coordinates[i].split() != [] and rooms_coordinates[i].split()[0] != "#":
                current = rooms_coordinates[i].split()
                page = self.page_names[int(current[4])]
                id = "room_button_" + str(current[5])
                exec("self." + id + " = QtWidgets.QPushButton(self." + page + ")")
                exec("self." + id + ".setGeometry(int(current[0]) + self.offset_x, int(current[1]) + self.offset_y, int(current[2]), int(current[3]))")
                exec("self." + id + ".setStyleSheet(self.stylesheet_alpha)")
                exec("self." + id + ".setText(current[5])")
                exec("self." + id + ".setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)")
                self.original_sizes_rooms[id] = current
