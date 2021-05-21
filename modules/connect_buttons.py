class connectButtons:
    def connect_buttons(self):
        # Подлключение функций у виджетам
        self.horizontalSlider_size.valueChanged.connect(self.resize_map)
        self.pushButton_page1.clicked.connect(self.choose_map)
        self.pushButton_page2.clicked.connect(self.choose_map)
        self.pushButton_page3.clicked.connect(self.choose_map)
        self.pushButton_find.clicked.connect(self.find_room)
