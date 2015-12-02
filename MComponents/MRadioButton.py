__author__ = 'MaitreyaBuddha'

from PySide.QtGui import *
from PySide.QtCore import *
from MUtilities.MShape import MShape
from MUtilities import MColors
from MAnimations.MFade import MFadeOut, MFadeIn
from MAnimations.MScale import MScaleOut, MScaleIn


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
        self.setMaxWidth(10)
        self.setMaxHeight(10)
        self.setWidth(10)
        self.setHeight(10)
        self.setMarginX(20)
        self.setMarginY(20)
        self.__pen = QPen(MColors.PRIMARY_COLOR, 0)
        self.__color = MColors.PRIMARY_COLOR

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.getOpacity())
        painter.setPen(self.__pen)
        painter.setBrush(self.__color)
        painter.drawEllipse(self.getX()+self.getMarginX(), self.getY()+self.getMarginY(), self.getWidth(), self.getHeight())
        painter.end()


class MRadioButton(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setFixedSize(QSize(50, 50))
        self.innerCircle = InnerCircle()
        self.outerRing = OuterRing()
        self.addLayoutItem(self.outerRing, 0, 0)
        self.addLayoutItem(self.innerCircle, 0, 0)
        self.setLayout(self.getLayout())
        self.__checked = True

    def mousePressEvent(self, event):
        if self.__checked:
            MScaleOut.start(self.innerCircle, 0.006)
            self.__checked = False
        else:
            MScaleIn.start(self.innerCircle, 0.006)
            self.__checked = True

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setClipRect(QRect(0, 0, 50, 50))
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor('#FFF'), 1))
        painter.end()
