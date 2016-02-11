__author__ = 'MaitreyaBuddha'

from PySide.QtGui import QWidget, QGridLayout, QApplication
from PySide.QtCore import QMargins

from MAnimations.MAnimate import MAnimate


class MShape(QWidget, MAnimate):
    def __init__(self):
        QWidget.__init__(self)
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0
        self.__opacity = 1.0
        self.__clip = None
        self.__parent_clip = None
        self.__max_width = 0
        self.__max_height = 0
        self.__min_width = 0
        self.__min_height = 0
        self.__max_opacity = 1.0
        self.__min_opacity = 0.0
        self.__margin_left = 0
        self.__margin_top = 0
        self.__padding_x = 0
        self.__padding_y = 0
        # Defining the layout which will hold the child shapes of the widget
        self.__layout = QGridLayout()
        self.__layout.setVerticalSpacing(0)
        self.__layout.setHorizontalSpacing(0)
        self.__layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.__children = []

    def add_layout_item(self, shape, x, y):
        self.__layout.addWidget(shape, x, y)
        self.__children.append(shape)
        self.update()

    def remove_layout_item(self, shape):
        self.__layout.removeWidget(shape)
        self.__children.remove(shape)
        shape.deleteLater()
        self.update()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def layout(self):
        return self.__layout

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        if self.width < self.min_width:
            self.__width = self.min_width
        elif self.width > self.max_width:
            self.__width = self.max_width

    @property
    def min_width(self):
        return self.__min_width

    @min_width.setter
    def min_width(self, width):
        self.__min_width = width

    @property
    def max_width(self):
        return self.__max_width

    @max_width.setter
    def max_width(self, width):
        self.__max_width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        if self.height < self.min_height:
            self.__height = self.min_height
        elif self.height > self.max_height:
            self.__height = self.max_height

    @property
    def min_height(self):
        return self.__min_height

    @min_height.setter
    def min_height(self, height):
        self.__min_height = height

    @property
    def max_height(self):
        return self.__max_height

    @max_height.setter
    def max_height(self, height):
        self.__max_height = height

    @property
    def opacity(self):
        return self.__opacity

    @opacity.setter
    def opacity(self, opacity):
        self.__opacity = opacity
        if self.opacity < self.min_opacity:
            self.opacity = self.min_opacity

    @property
    def min_opacity(self):
        return self.__min_opacity

    @min_opacity.setter
    def min_opacity(self, opacity):
        self.__min_opacity = opacity

    @property
    def max_opacity(self):
        return self.__max_opacity

    @max_opacity.setter
    def max_opacity(self, opacity):
        self.__max_opacity = opacity

    @property
    def margin_left(self):
        return self.__margin_left

    @margin_left.setter
    def margin_left(self, margin):
        self.__margin_left = margin

    @property
    def margin_top(self):
        return self.__margin_top

    @margin_top.setter
    def margin_top(self, margin):
        self.__margin_top = margin

    @property
    def clip(self):
        return self.__clip

    @clip.setter
    def clip(self, value):
        self.__clip = value

    @property
    def parent_clip(self):
        return self.__parent_clip

    @parent_clip.setter
    def parent_clip(self, value):
        self.__parent_clip = value
