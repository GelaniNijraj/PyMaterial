import sys

from PySide.QtGui import *
from PySide.QtCore import *
from MUtilities import MColors
from MComponents.MShape import MShape


class Box(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_height = 200
        self.max_width = 200
        self.height = 200
        self.width = 200
        self.opacity = 0
        self.__brush = QBrush(QColor("#00796B"))
        self.__pen = QPen(QColor(0, 0, 0, 0))

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.__brush)
        painter.setPen(self.__pen)
        painter.setOpacity(self.opacity)
        if self.clip is not None:
            painter.setClipPath(self.clip)
        painter.drawRect(QRect(self.x, self.y, self.height, self.width))
        painter.end()


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Animation Tests")
        self.setGeometry(100, 100, 500, 500)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_DARK)
        self.setPalette(p)
        self.__box = Box()

    def add_component(self):
        layout = QGridLayout()
        layout.addWidget(self.__box)

        fade_in = QPushButton("Fade In")
        fade_out = QPushButton("Fade Out")
        scale_in = QPushButton("Scale In")
        scale_out = QPushButton("Scale Out")
        circular_in = QPushButton("Reveal In")
        circular_out = QPushButton("Reveal Out")

        fade_in.clicked.connect(self.fade_in)
        fade_out.clicked.connect(self.fade_out)
        scale_in.clicked.connect(self.scale_in)
        scale_out.clicked.connect(self.scale_out)
        circular_in.clicked.connect(self.reveal_in)
        circular_out.clicked.connect(self.reveal_out)


        fade_buttons = QHBoxLayout()
        scale_buttons = QHBoxLayout()
        reveal_buttons = QHBoxLayout()

        fade_buttons.addWidget(fade_in)
        fade_buttons.addWidget(fade_out)
        scale_buttons.addWidget(scale_in)
        scale_buttons.addWidget(scale_out)
        reveal_buttons.addWidget(circular_in)
        reveal_buttons.addWidget(circular_out)

        cancel = QPushButton("Cancel Animation")
        cancel.clicked.connect(self.cancel_animation)
        layout.addItem(fade_buttons)
        layout.addItem(scale_buttons)
        layout.addItem(reveal_buttons)
        layout.addWidget(cancel)
        self.setLayout(layout)

    def fade_in(self):
        self.__box.animate().fade(1).duration(5000).start()

    def fade_out(self):
        self.__box.animate().fade(0).duration(5000).start()

    def scale_in(self):
        self.__box.animate().scale(QPoint(200, 200)).duration(1000).start()

    def scale_out(self):
        self.__box.animate().scale(QPoint(0, 0)).duration(10000).start()

    def reveal_in(self):
        self.__box.animate().reveal("show").duration(1000).start()

    def reveal_out(self):
        self.__box.animate().reveal("hide").duration(1000).start()

    def cancel_animation(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.add_component()
    win.show()
    app.exec_()
    sys.exit()
