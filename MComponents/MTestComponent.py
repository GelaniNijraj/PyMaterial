__author__ = 'Samvid Mistry'

from PySide.QtCore import *
from PySide.QtGui import *

from MAnimations.MScale import MScale
from MAnimations.MFade import MFade
from MComponents.MShape import MShape
from MUtilities import MColors
from MUtilities.MRipple import MRipple
from MComponents.MRadioButton import MRadioButton


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

        self.__ripple = MRipple()
        self.add_layout_item(self.__ripple, 0, 0)
        self.margin_left = 10
        self.margin_top = 15
        self.setLayout(self.layout)
        self.__scale = MFade()
        path = QPainterPath()
        path.addRect(0, 0, 100, 100)
        self.clip = path
        self.__scale.add_target(self)
        self.__bounding_rect = QRect(self.margin_left, self.margin_top, self.width, self.height)

    def paintEvent(self, event):
        self.__painter.begin(self)
        self.__painter.setRenderHint(QPainter.Antialiasing)
        self.__painter.setOpacity(self.opacity)
        self.__painter.setPen(self.__pen)
        self.__painter.setBrush(self.__color)
        # if self.clip is not None:
        self.__painter.drawRect(QRect(self.x + self.margin_left, self.y + self.margin_top, self.width, self.height))
        self.__painter.end()

    def mousePressEvent(self, event):
        self.__ripple.handle_click_events(event)

    def mouseReleaseEvent(self, event):
        self.__ripple.handle_release_events(event)

    def trigger_cancel(self):
        self.__scale.target = 0
        self.__scale.start()
