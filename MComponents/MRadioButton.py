__author__ = 'MaitreyaBuddha'

from PySide.QtCore import *
from PySide.QtGui import *

from MComponents.MShape import MShape
from MUtilities import MColors


class OuterRing(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 16
        self.max_height = 16
        self.width = 16
        self.height = 16
        self.margin_top = 4
        self.margin_left = 4
        self.__color = MColors.PRIMARY_COLOR
        self.__pen = QPen(self.__color, 2)
        self.__bounding_rect = QRect(self.x + self.margin_left, self.y + self.margin_top,
                                     self.width, self.height)

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
        self.max_width = 8
        self.max_height = 8
        self.width = 8
        self.height = 8
        self.margin_top = 8
        self.margin_left = 8
        self.__pen = QPen(QColor(0, 0, 0, 0), 0)
        self.__color = MColors.PRIMARY_COLOR
        self.__bounding_rect = QRect(self.x + self.margin_left, self.y + self.margin_top,
                                     self.width, self.height)
        self.hide_initially()

    def hide_initially(self):
        path = QPainterPath()
        path.addEllipse(0, 0, 0, 0)
        self.clip = path

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.clip is not None:
            painter.setClipPath(self.clip)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.setBrush(self.__color)
        painter.drawEllipse(self.__bounding_rect)
        painter.end()


# TODO: extend it with TwoStateShape?
class MRadioButton(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 30
        self.max_height = 30
        self.width = 30
        self.height = 30
        self.setFixedSize(self.width, self.height)
        self.innerCircle = InnerCircle()
        self.outerRing = OuterRing()
        self.add_layout_item(self.outerRing, 0, 0)
        self.add_layout_item(self.innerCircle, 0, 0)
        self.setLayout(self.layout)
        self.__checked = False
        self.__bounding_rect = QRect(self.x + self.margin_left / 2, self.y + self.margin_top / 2,
                                     self.width - self.margin_left, self.height - self.margin_top)

    def mouseReleaseEvent(self, event):
        if self.__checked:
            self.uncheck()
        else:
            self.check()

    def check(self):
        if self.__checked is not True:
            self.innerCircle.animate().reveal("show_circle").duration(200).start()
            self.__checked = True

    def uncheck(self):
        if self.__checked is True:
            self.innerCircle.animate().reveal("hide_circle").duration(200).start()
            self.__checked = False
