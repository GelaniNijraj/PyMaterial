__author__ = 'MaitreyaBuddha'

from PySide.QtCore import *
from PySide.QtGui import *

from MAnimations.MFade import MFadeOut
from MComponents.MShape import MShape
from MUtilities import MColors


class OuterRing(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 20
        self.max_height = 20
        self.width = 20
        self.height = 20
        self.margin_x = 4
        self.margin_y = 4
        self.__color = MColors.PRIMARY_COLOR
        self.__pen = QPen(self.__color, 2)
        self.__bounding_rect = QRect(self.x() + self.margin_x / 2, self.y() + self.margin_y / 2,
                                     self.width - self.margin_x, self.height - self.margin_y)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.drawEllipse(self.__bounding_rect)
        painter.end()


class InnerCircle(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 20
        self.max_height = 20
        self.width = 20
        self.height = 20
        self.margin_x = 12
        self.margin_y = 12
        self.__pen = QPen(MColors.PRIMARY_COLOR, 0)
        self.__color = MColors.PRIMARY_COLOR
        self.__bounding_rect = QRect(self.x() + self.margin_x / 2, self.y() + self.margin_y / 2,
                                     self.width - self.margin_x, self.height - self.margin_y)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.setBrush(self.__color)
        painter.drawEllipse(self.__bounding_rect)
        painter.end()


class MRadioButton(MShape):
    def __init__(self):
        MShape.__init__(self)

        self.max_height = 20
        self.max_width = 20
        self.width = self.max_width
        self.height = self.max_height
        self.setFixedSize(self.width, self.height)
        self.innerCircle = InnerCircle()
        self.outerRing = OuterRing()
        self.add_layout_item(self.outerRing, 0, 0)
        self.add_layout_item(self.innerCircle, 0, 0)
        self.setLayout(self.layout)
        self.__pen = QPen(QColor('#FFF'), 2)
        self.__checked = True
        self.__fade = MFadeOut()
        self.__fade.duration = 100
        self.__fade.add_target(self.innerCircle)
        self.__bounding_rect = QRect(self.x() + self.margin_x / 2, self.y() + self.margin_y / 2,
                                     self.width - self.margin_x, self.height - self.margin_y)

    def mousePressEvent(self, event):
        if self.__checked:
            self.__fade.start()
            self.__checked = False
        else:
            self.__checked = True
