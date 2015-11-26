from PySide.QtGui import *
from MUtilities.MShape import MShape
from MAnimations.MFade import MFadeOut, MFadeIn

__author__ = 'MaitreyaBuddha'


class OuterRing(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setWidth(17)
        self.setHeight(17)
        self.__color = QColor("#F00")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.getOpacity())
        painter.setPen(QPen(self.__color, 2))
        painter.drawEllipse(self.getX(), self.getX(), self.getWidth(), self.getHeight())
        painter.end()


class InnerCircle(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setWidth(9)
        self.setHeight(9)
        self.__penColor = QColor(255, 255, 255, 0)
        self.__pen = QPen(self.__penColor, 0)
        self.__color = QColor("#F00")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.getOpacity())
        painter.setPen(self.__pen)
        painter.setBrush(self.__color)
        painter.drawEllipse(self.getX(), self.getX(), self.getWidth(), self.getHeight())
        painter.end()


class MRadioButton(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.innerCircle = InnerCircle()
        self.innerCircle.setX(self.getX() + 5)
        self.innerCircle.setY(self.getY() + 5)
        self.outerRing = OuterRing()
        self.outerRing.setX(self.getX() + 1)
        self.outerRing.setY(self.getY() + 1)
        layout = QGridLayout()
        layout.addWidget(self.innerCircle, 0, 0)
        layout.addWidget(self.outerRing, 0, 0)
        self.setLayout(layout)
        self.setWidth(self.outerRing.getWidth())
        self.setHeight(self.outerRing.getHeight())
        self.__checked = True

    def mousePressEvent(self, event):
        if self.__checked:
            MFadeOut.start(self.innerCircle)
            self.__checked = False
        else:
            MFadeIn.start(self.innerCircle)
            self.__checked = True
