__author__ = "Samvid Mistry"

from PySide.QtGui import *
from PySide.QtCore import *

from MComponents.MShape import MShape
from MUtilities import MColors
from MAnimations.MCircularReveal import MCircularReveal
from MAnimations.MFade import MFadeOut


class CheckboxBorder(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 20
        self.max_height = 20
        self.width = 20
        self.height = 20
        self.margin_x = 4
        self.margin_y = 4
        self.__color = QColor("#5A5A5A")
        self.__pen = QPen(self.__color, 2)
        self.__bounding_rect = QRect(self.x() + self.margin_x / 2, self.y() + self.margin_y / 2,
                                     self.width - self.margin_x, self.height - self.margin_y)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.drawRoundedRect(self.__bounding_rect, 2, 2)


class CheckboxArea(MShape):
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
        self.__white_color = QColor("#FFF")
        self.__check_pen = QPen(self.__white_color, 2, c=Qt.SquareCap, j=Qt.MiterJoin)
        self.__check_path = QPainterPath()
        self.__check_path.moveTo(5, 10)
        self.__check_path.lineTo(9, 14)
        self.__check_path.moveTo(9, 14)
        self.__check_path.lineTo(15, 6)
        self.__bounding_rect = QRect(self.x() + self.margin_x / 2, self.y() + self.margin_y / 2,
                                     self.width - self.margin_x, self.height - self.margin_y)

    def paintEvent(self, event):
        painter = QPainter()
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


class MCheckBox(MShape):
    def __init__(self):
        MShape.__init__(self)

        self.max_height = 20
        self.max_width = 20
        self.width = self.max_width
        self.height = self.max_height
        self.setFixedSize(self.width, self.height)
        self.__border = CheckboxBorder()
        self.__area = None
        self.add_layout_item(self.__border, 0, 0)
        self.__reveal = MCircularReveal()
        self.__reveal.duration = 300
        self.__fade = MFadeOut()
        self.__fade.duration = 200
        self.setLayout(self.layout)
        self.__checked = False

    def mousePressEvent(self, event):
        if self.__checked:
            self.__reveal.remove_target(self.__area)
            self.__fade.add_target(self.__area)
            self.__fade.end_signal.connect(self.on_fade_end)
            self.__fade.start()
        else:
            self.__area = CheckboxArea()
            self.add_layout_item(self.__area, 0, 0)
            self.__reveal.add_target(self.__area)
            self.__reveal.start()
            self.__checked = True

    def on_fade_end(self):
        self.__fade.remove_target(self.__area)
        self.__fade.end_signal.disconnect(self.on_fade_end)
        self.remove_layout_item(self.__area)
        self.__checked = False
