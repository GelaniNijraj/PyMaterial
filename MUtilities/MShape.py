__author__ = 'MaitreyaBuddha'

from PySide.QtGui import QWidget


class MShape(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__x = 0
        self.__y = 0
        self.__width = None
        self.__height = None
        self.__opacity = 1
        self.__clip = None
        self.__maxWidth = None
        self.__maxHeight = None
        self.__maxOpacity = 1
        self.__minOpacity = 0
        self.__fadeAnimation = False

    def setFadeAnimationRunning(self, val):
        self.__fadeAnimation = val

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setOpacity(self, opacity):
        self.__opacity = opacity

    def setMinOpacity(self, opacity):
        self.__maxOpacity = opacity

    def setMaxOpacity(self, opacity):
        self.__minOpacity = opacity

    def setHeight(self, height):
        self.__height = height

    def setWidth(self, width):
        self.__width = width

    def setClipRegion(self, clip):
        self.__clip = clip

    def setMaxWidth(self, width):
        self.__maxWidth = width

    def setMaxHeight(self, height):
        self.__maxHeight = height

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

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

    def getMinOpacity(self):
        return self.__minOpacity

    def getMaxOpacity(self):
        return self.__maxOpacity

    def isFadeAnimationRunning(self):
        return self.__fadeAnimation
