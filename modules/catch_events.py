from PyQt5 import QtCore, QtGui, QtWidgets


class catchEvents:
    def resizeEvent(self, event):
        # Масштабирование элементов окна

        # Основное окно
        self.groupBox_main.setFixedSize(self.size().width(), self.size().height() - self.title_heigth)
        self.label_corner.move(self.size().width() - 10, self.size().height() - 43)
        self.stackedWidget.setFixedSize(self.size().width() - 35, self.size().height() - 75)

        # Заголовок
        self.groupBox_title.setFixedSize(self.size().width(), self.title_heigth)
        self.exitAppButton.setGeometry(self.size().width() - 21, 0, 21, 21)
        self.maximizeButton.setGeometry(self.size().width() - 42, 0, 21, 21)
        self.minimizeButton.setGeometry(self.size().width() - 63, 0, 21, 21)

    def mousePressEvent(self, event):
        # Считывания координат мыши
        if event.buttons() == QtCore.Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # Движение мыши
        if event.buttons() == QtCore.Qt.LeftButton:
            # Определение перетаскивания окна
            if self.groupBox_title.underMouse() and not self.resising and \
                    not self.grapping and not self.grapping_map:
                self.grapping = True
                QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.ClosedHandCursor)
            # Определение масштабирования окна
            elif event.x() > self.size().width() - 20 and event.y() > self.size().height() - 20 and not self.resising and \
                    not self.grapping and not self.grapping_map:
                self.resising = True
                QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.SizeAllCursor)
            # Определение движения карты
            elif event.x() < self.stackedWidget.size().width() and \
                    event.x() > self.stackedWidget.geometry().x() and \
                    event.y() < self.stackedWidget.size().height() and \
                    event.y() > self.stackedWidget.geometry().y() and not self.resising and \
                    not self.grapping and not self.grapping_map:
                QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.ClosedHandCursor)
                self.grapping_map = True

            delta = QtCore.QPoint(event.globalPos() - self.oldPos)  # Дельта движения мыши
            # Перетаскивание окна
            if self.grapping and self.groupBox_title.underMouse():
                self.move(self.x() + delta.x(), self.y() + delta.y())
            # Масштабирование окна
            if self.resising:
                if self.size().width() + delta.x() >= self.minimumSizeWidht:
                    self.setFixedSize(self.size().width() + delta.x(), self.size().height())
                if self.size().height() + delta.y() >= self.minimumSizeHeight:
                    self.setFixedSize(self.size().width(), self.size().height() + delta.y())
            # Движение карты
            if self.grapping_map:
                self.offset_x += delta.x()
                self.offset_y += delta.y()
                self.resize_map()
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        # Отмена всех действий при отпускании мыши
        self.resising = False
        self.grapping = False
        self.grapping_map = False
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

    def wheelEvent(self, event):
        self.horizontalSlider_size.setValue(self.horizontalSlider_size.value() + event.angleDelta().y() // 120)
