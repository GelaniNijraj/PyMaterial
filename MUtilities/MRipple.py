__author__ = 'MaitreyaBuddha'

from PySide.QtGui import *
from PySide.QtCore import *

from MComponents.MShape import MShape
from MUtilities import MColors


class MRippleShape(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.max_width = 100
        self.max_height = 100
        self.width = 0
        self.height = 0
        self.__painter = QPainter()
        self.__color = QColor(0, 0, 0, 100)
        self.__pen = QPen(QColor(0, 0, 0, 0), 2)
        self.__max_size = 100

    def reset(self):
        print("resetting!")
        self.height = 0
        self.width = 0
        # self.opacity = 1
        self.update()

    def paintEvent(self, event):
        self.__painter.begin(self)
        self.__painter.setRenderHint(QPainter.Antialiasing)
        self.__painter.setOpacity(self.opacity)
        self.__painter.setPen(self.__pen)
        self.__painter.setBrush(self.__color)
        self.__painter.drawEllipse(QRect(
            self.x + self.margin_left - (self.width / 2),
            self.y + self.margin_top - (self.height / 2),
            self.width,
            self.height
        ))
        self.__painter.end()


class MRipple(MShape):
    def __init__(self):
        MShape.__init__(self)
        self.__ripple = MRippleShape()
        self.add_layout_item(self.__ripple, 0, 0)
        self.setLayout(self.layout)

    def handle_click_events(self, event):
        """
        Handles all the events(i.e. expanding, moving, fading) that the
        ripple should and repaints the ripple at the end.
        :param event: QMouseEvent
        :return: None
        """
        if not isinstance(event, QMouseEvent):
            raise ValueError("event must be an instance of QMouseEvent")
        mouse_position = event.pos()
        self.__ripple.x = mouse_position.x()
        self.__ripple.y = mouse_position.y()
        self.__ripple.update()
        self.__ripple.animate().fade(1).scale(QPoint(100, 100)).duration(200).start()
        QApplication.processEvents()

    def handle_release_events(self, event):
        self.__ripple.animate().fade(0).duration(200).start()
