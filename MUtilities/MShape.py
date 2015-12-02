__author__ = 'MaitreyaBuddha'

from PySide.QtGui import QWidget, QGridLayout, QApplication, QGraphicsLayout
from PySide.QtCore import QMargins


class MShape(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0
        self.__opacity = 1
        self.__clip = None
        self.__maxWidth = 0
        self.__maxHeight = 0
        self.__minWidth = 0
        self.__minHeight = 0
        self.__maxOpacity = 1
        self.__minOpacity = 0
        self.__marginX = 0
        self.__marginY = 0
        # Animation related flafs
        self.__fadeAnimation = False
        self.__scaleAnimation = False
        # Defining the layout which will hold the child shapes of the widget
        self.__layout = QGridLayout()
        self.__layout.setVerticalSpacing(0)
        self.__layout.setHorizontalSpacing(0)
        self.__layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.__children = []

    def move(self, x, y):
        QWidget.move(self, x, y)
        self.__x = x
        self.__y = y
        self.update()
        QApplication.processEvents()

    def setFadeAnimationRunning(self, val):
        self.__fadeAnimation = val

    def setScaleAnimationRunning(self, val):
        self.__scaleAnimation = val

    def setY(self, y):
        self.move(self.__x, y)

    def setOpacity(self, opacity):
        self.__opacity = opacity

    def setMinOpacity(self, opacity):
        self.__maxOpacity = opacity

    def setMaxOpacity(self, opacity):
        self.__minOpacity = opacity

    def setHeight(self, height):
        self.__height = height
        if self.__height < self.__minHeight:
            self.__height = self.__minHeight
        elif self.__height > self.__maxHeight:
            self.__height= self.__maxHeight

    def setWidth(self, width):
        self.__width = width
        if self.__width < self.__minWidth:
            self.__width = self.__minWidth
        elif self.__width > self.__maxWidth:
            self.__width = self.__maxWidth

    def setClipRegion(self, clip):
        self.__clip = clip

    def setMaxWidth(self, width):
        """
        Must be called before setWidth()
        :param width: int
        :return:
        """
        self.__maxWidth = width

    def setMaxHeight(self, height):
        """
        Must be called before setHeight()
        :param width: int
        :return:
        """
        self.__maxHeight = height

    def setMarginX(self, x):
        self.__marginX = x

    def setMarginY(self, y):
        self.__marginY = y

    def addLayoutItem(self, item, x, y):
        self.__children.append(item)
        self.__layout.addWidget(item, x, y)

    def getX(self):
        return self.x()

    def getY(self):
        return self.y()

    def getOpacity(self):
        return self.__opacity

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getClipRegion(self):
        return self.__clip

    def getMaxWidth(self):
        return self.__maxWidth

    def getMaxHeight(self):
        return self.__maxHeight

    def getMinWidth(self):
        return self.__minWidth

    def getMinHeight(self):
        return self.__minHeight

    def getMinOpacity(self):
        return self.__minOpacity

    def getMaxOpacity(self):
        return self.__maxOpacity

    def getMarginX(self):
        return self.__marginX

    def getMarginY(self):
        return self.__marginY

    def getLayout(self):
        return self.__layout

    def isFadeAnimationRunning(self):
        return self.__fadeAnimation

    def isScaleAnimationRunning(self):
        return self.__scaleAnimation
