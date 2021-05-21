from PyQt5 import QtCore


class framelessWindow:
    def make_frameless(self):
        #   Безрамочное окно + кнопки в заголовке
        self.minimumSizeWidht = 800
        self.minimumSizeHeight = 600
        self.setMinimumSize(self.minimumSizeWidht, self.minimumSizeHeight)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.exitAppButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.minimizeButton.clicked.connect(self.showMinimized)
        self.maximazed = False
        self.maximizeButton.clicked.connect(self.show_maximize)
        self.setMouseTracking(True)
        self.resising = False
        self.grapping = False
        self.grapping_map = False
        self.label_corner.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # Сделать символ в углу невидимым для мыши
        self.label_name.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # Сделать название программы невидимым для мыши
