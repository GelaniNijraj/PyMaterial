__author__ = 'MaitreyaBuddha'

import time

from PySide.QtGui import QWidget, QPainter, QBrush, QPen, QColor, QApplication

from MUtilities import MColors

class MRipple(QWidget):
    def __init__(self, origin, target_center, clip):
        QWidget.__init__(self)
        self.__origin = origin
        self.__target_center = target_center
        self.__clip = clip
        # Default flag values
        self.__flag = 0
        self.__finished = False
        self.__release = False
        # Default animation speed
        self.__speed = 0.006
        # Default release fade out step counts
        self.__releaseSpeed = 30
        # Default color
        self.__color = MColors.PRIMARY_COLOR
        # Default maximum radius of the ripple
        self.__maxRadius = 23
        # Default minimum radius of the ripple
        self.__r = 1
        # Default minimum opacity
        self.__minOpacity = 30
        # Default maximum opacity
        self.__opacity = 255
        # Counter used in release animation
        self.__i = 0

    def stepAnimate(self):
        self.animate(1)

    def animate(self, steps=None):
        """
        This function animates the initial animation of ripple
        :return: None
        """
        s = 0
        while self.__r < self.__maxRadius:
            if steps is not None and s == steps:
                return
            if self.__flag == 1:
                self.destroy()
                self.update()
                self.__finished = True
                break
            # checking of origin and target case are the same points
            if self.__origin != self.__target_center:
                # moving x coord of origin towards x of target_center
                if self.__origin.x() > self.__target_center.x():
                    self.__origin.setX(self.__origin.x() - 1)
                elif self.__origin.x() < self.__target_center.x():
                    self.__origin.setX(self.__origin.x() + 1)
                else:
                    pass
                # moving y coord of origin towards y of target_center
                if self.__origin.y() > self.__target_center.y():
                    self.__origin.setY(self.__origin.y() - 1)
                elif self.__origin.y() < self.__target_center.y():
                    self.__origin.setY(self.__origin.y() + 1)
                else:
                    pass
            self.__r += 1
            self.__opacity = 255 - (255 * self.__r) / self.__maxRadius
            if self.__opacity <= self.__minOpacity:
                self.__opacity = self.__minOpacity
            # repainting the canvas
            self.update()
            QApplication.processEvents()
            # animation speed
            time.sleep(self.__speed)
            # increasing step count
            try:
                if self.__origin == self.__target_center and self.__r == self.__maxRadius and self.__opacity == self.__maxOpacity:
                    self.__finished = True
            except AttributeError:
                pass
            s += 1
        # setting the flag finished True, once the animation is performed to its full
        # checking if the mouse button is released yet or not
        if self.__release:
            # performing mouse release animation
            if steps is None:
                self.releaseAnimate(None)
            else:
                self.releaseStepAnimate()
        return

    def releaseStepAnimate(self):
        self.releaseAnimate(1)

    def releaseAnimate(self, steps=None):
        """
        This function creates the animation to be performed when mouse is released
        :return: None
        """
        s = 0
        while self.__i < self.__releaseSpeed:
            if steps is not None and steps == s:
                return
            if self.__flag == 1:
                self.destroy()
                self.update()
                break
            # reducing alpha to zero, in 23 steps
            self.__opacity = self.__minOpacity - (self.__minOpacity * self.__i) / self.__releaseSpeed
            self.__i += 1
            # repainting the canvas
            self.update()
            QApplication.processEvents()
            # animation speed
            time.sleep(self.__speed)
            s += 1

    def stop(self):
        """
        This function stop the ripple effect. Setting the flag=1, indicating that the ripple is no longer needed.
        :return: None
        """
        self.__flag = 1

    def paintEvent(self, event):
        """
        This function handles the low level painting of component.
        :param event:
        :return:
        """
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.__flag == 1:
            painter.end()
            return
        # setting the masking ellipse
        painter.setClipRegion(self.__clip)
        self.__color.setAlpha(self.__opacity)
        painter.setBrush(QBrush(self.__color))
        painter.setPen(QPen(QColor(0, 0, 0, 0)))
        painter.drawEllipse(self.__origin, self.__r, self.__r)
        painter.end()

    # Setters
    def setReleased(self, val):
        """
        This function sets the flag release, indicating that the mouse button is now released.
        :param val: Boolean::Flag indicating the release status of the ripple
        :return: None
        """
        self.__release = val

    def setMaxRadius(self, r):
        """
        This function sets the maximum radius of the ripple.
        :param r: int::radius
        :return: None
        """
        self.__maxRadius = r

    def setMinRadius(self, r):
        """
        This function sets the minimum radius of the ripple i.e. starting radius.
        :param r: int::radius
        :return: None
        """
        self.__r = r

    def setColor(self, color):
        """
        This function sets custom color for the ripple.
        :param color: PySide.QtGui.QColor::Color of the ripple
        :return: None
        """
        self.__color = color

    def setAnimationSpeed(self, speed):
        """
        This function sets the animation speed.
        :param speed: int::Animation speed of the ripple
        :return: None
        """
        self.__speed = speed

    def setReleaseStepCount(self, count):
        """
        This function sets the release fade out step count.
        :param count: int::Animation speed of the fading out of the ripple
        :return: None
        """
        self.__releaseSpeed = count

    def setMinOpacity(self, opacity):
        """
        This function sets the minimum opacity.
        :param opacity: int::Minimum possible opacity of the ripple
        :return: None
        """
        self.__minOpacity = opacity

    def setMaxOpacity(self, opacity):
        """
        This function sets the maximum opacity i.e. starting opacity.
        :param opacity: int::Maximum possible opacity of the ripple
        :return: None
        """
        self.__maxOpacity = opacity

    def setOrigin(self, origin):
        """
        This function sets the origin of the ripple.
        :param origin: PySide.QtCore.QPoint::Origin(clicked point) of the ripple
        :return: None
        """
        self.__origin = origin

    def setTargetCenter(self, center):
        """
        This function sets thr target center of the ripple
        :param center: PySide.QtCore.QPoint::Center to which ripple must reach
        :return: None
        """
        self.__target_center = center

    # Getters
    def isFinished(self):
        """
        This function return the state of animation i.e. is it finished or not
        :return: Boolean::Animation status of the ripple
        """
        return self.__finished
