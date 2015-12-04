__author__ = 'MaitreyaBuddha'

from PySide.QtGui import *
from PySide.QtCore import *
from MUtilities.MShape import MShape
from MUtilities import MColors
from MAnimations.MFade import MFadeOut


class OuterRing(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setMaxWidth(20)
        self.setMaxHeight(20)
        self.setWidth(20)
        self.setHeight(20)
        self.setMarginX(15)
        self.setMarginY(15)
        self.__color = MColors.PRIMARY_COLOR

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.getOpacity())
        painter.setPen(QPen(self.__color, 2))
        painter.drawEllipse(self.getX()+self.getMarginX(), self.getY()+self.getMarginY(), self.getWidth(), self.getHeight())
        painter.end()


class InnerCircle(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.__pen = QPen(MColors.PRIMARY_COLOR, 0)
        self.__color = MColors.PRIMARY_COLOR

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.opacity)
        painter.setPen(self.__pen)
        painter.setBrush(self.__color)
        painter.drawEllipse(0, 0, 10, 10)
        painter.end()


class MRadioButton(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setFixedSize(QSize(50, 50))
        self.innerCircle = InnerCircle()
        # self.outerRing = OuterRing()
        # self.addLayoutItem(self.outerRing, 0, 0)
        self.add_layout_item(self.innerCircle, 0, 0)
        self.setLayout(self.layout)
        self.__checked = True
        self.__fade = MFadeOut()
        self.__fade.add_target(self.innerCircle)
        self.__fade.end_signal.connect(self.test_slot)

    def test_slot(self):
        print("Ended gracefully")

    def mousePressEvent(self, event):
        if self.__checked:
            self.__fade.start()
            self.__checked = False
        else:
            self.__checked = True

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setClipRect(QRect(0, 0, 50, 50))
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor('#FFF'), 1))
        painter.end()
