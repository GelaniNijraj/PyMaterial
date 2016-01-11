__author__ = 'Samvid Mistry'

from PySide.QtCore import *
from PySide.QtGui import *

from MAnimations.MCircularReveal import MCircularReveal
from MComponents.MShape import MShape
from MUtilities import MColors


class MTestComponent(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 100
        self.max_height = 100
        self.width = 100
        self.height = 100
        self.__color = MColors.PRIMARY_COLOR
        self.__pen = QPen(self.__color, 0)
        self.__painter = QPainter()
        self.__reveal = MCircularReveal()
        self.__reveal.duration = 100
        self.__reveal.add_target(self)
        self.__bounding_rect = QRect(10, 15, self.width, self.height)

    def paintEvent(self, event):
        self.__painter.begin(self)
        self.__painter.setRenderHint(QPainter.Antialiasing)
        self.__painter.setPen(self.__pen)
        self.__painter.setBrush(self.__color)
        if self.clip is not None:
            self.__painter.setClipPath(self.clip)
        self.__painter.drawRect(self.__bounding_rect)
        self.__painter.end()

    def mousePressEvent(self, event):
        self.__reveal.start()