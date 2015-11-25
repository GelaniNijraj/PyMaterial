__author__ = 'MaitreyaBuddha'

from PySide.QtGui import *
from PySide.QtCore import *
from MUtilities.MShape import MShape
from MAnimations.MFade import MFadeOut, MFadeIn


class OuterRing(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setWidth(17)
        self.setHeight(17)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.getOpacity())
        painter.setPen(QPen(QColor("#F00"), 2))
        painter.drawEllipse(QRect(self.getX(), self.getX(), self.getWidth(), self.getHeight()))


class InnerCircle(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.setWidth(9)
        self.setHeight(9)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self.getOpacity())
        painter.setPen(QPen(QColor(255, 255, 255, 0), 0))
        painter.setBrush(QColor("#F00"))
        painter.drawEllipse(QRect(self.getX(), self.getX(), self.getWidth(), self.getHeight()))
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
        self.__checked = True

    def mousePressEvent(self, event):
        if self.__checked:
            MFadeOut.start(self.innerCircle)
            self.__checked = False
        else:
            MFadeIn.start(self.innerCircle)
            self.__checked = True

