from MComponents.MTwoStateShape import MTwoStateShape

__author__ = "Samvid Mistry"

from PySide.QtGui import *
from PySide.QtCore import *

from MComponents.MShape import MShape
from MUtilities import MColors


# TODO: Change according to the new MFade
class CheckboxBorder(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 20
        self.max_height = 20
        self.width = 20
        self.height = 20
        self.__color = QColor("#5A5A5A")
        self.__pen = QPen(self.__color, 2)
        self.__painter = QPainter()
        self.__bounding_rect = QRect(self.x + self.margin_left, self.y + self.margin_top,
                                     self.width, self.height)

    def paintEvent(self, event):
        painter = self.__painter
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.drawRoundedRect(self.__bounding_rect, 2, 2)
        painter.end()


class CheckboxArea(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 20
        self.max_height = 20
        self.width = 20
        self.height = 20
        self.__color = MColors.PRIMARY_COLOR
        self.__pen = QPen(self.__color, 2)
        self.__white_color = QColor("#FFF")
        self.__check_pen = QPen(self.__white_color, 2, c=Qt.SquareCap, j=Qt.MiterJoin)
        self.__check_path = QPainterPath()
        self.__check_path.moveTo(5, 10)
        self.__check_path.lineTo(9, 14)
        self.__check_path.moveTo(9, 14)
        self.__check_path.lineTo(15, 6)
        self.__painter = QPainter()
        self.__bounding_rect = QRect(self.x + self.margin_left, self.y + self.margin_top,
                                     self.width, self.height)
        self.hide_initially()

    def hide_initially(self):
        path = QPainterPath()
        path.addEllipse(0, 0, 0, 0)
        self.clip = path

    def paintEvent(self, event):
        painter = self.__painter
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.clip is not None:
            painter.setClipPath(self.clip)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.setBrush(self.__color)
        painter.drawRoundedRect(self.__bounding_rect, 2, 2)
        painter.setBrush(self.__white_color)
        painter.setPen(self.__check_pen)
        painter.drawPath(self.__check_path)
        painter.setBrush(self.__color)
        painter.setPen(self.__pen)
        painter.end()


class MCheckBox(MTwoStateShape):
    def __init__(self):
        MTwoStateShape.__init__(self)

        self.max_height = 20
        self.max_width = 20
        self.width = self.max_width
        self.height = self.max_height
        self.setFixedSize(self.width, self.height)
        self.__border = CheckboxBorder()
        self.__area = CheckboxArea()
        self.add_layout_item(self.__border, 0, 0)
        self.add_layout_item(self.__area, 0, 0)
        self.setLayout(self.layout)
        self.checked = False

    def mousePressEvent(self, event):
        if not self.checked:
            self.check()
        else:
            self.uncheck()

    def check(self):
        if MTwoStateShape.check(self):
            self.__area.animate().reveal("show_circle").duration(200).start()

    def uncheck(self):
        if MTwoStateShape.uncheck(self):
            self.__area.animate().reveal("hide_circle").duration(200).start()
