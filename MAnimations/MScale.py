__author__ = 'MaitreyaBuddha'

import time
import math
from threading import Thread
from PySide.QtGui import QApplication


class MScaleOut():
    @staticmethod
    def stepForward(shape):
        if not (shape.getWidth() <= shape.getMinWidth() or shape.getHeight() <= shape.getMinHeight()):
            # Calculating the 1% of maximum width and height
            w = math.ceil((shape.getMaxWidth() / 100))
            h = math.ceil((shape.getMaxHeight() / 100))
            # Keeping the shape in the center
            shape.setMarginX(shape.getMarginX() + (w / 2))
            shape.setMarginY(shape.getMarginY() + (h / 2))
            # Reducing the height and width by 1%
            shape.setWidth(shape.getWidth() - w)
            shape.setHeight(shape.getHeight() - h)
            return False
        else:
            return True

    @staticmethod
    def stop(shape):
        shape.setScaleAnimationRunning(False)

    @staticmethod
    def action(shape, speed = 0.016667):
        t = False
        if shape.isScaleAnimationRunning():
            shape.setScaleAnimationRunning(False)
            time.sleep(speed + 0.001)
        if not shape.isScaleAnimationRunning():
            shape.setScaleAnimationRunning(True)
            while not t:
                if not shape.isScaleAnimationRunning():
                    return False
                t = MScaleOut.stepForward(shape)
                shape.update()
                QApplication.processEvents()
                time.sleep(speed)
            shape.setScaleAnimationRunning(False)
            return True
        else:
            return False

    @staticmethod
    def start(shape, speed):
        t = Thread(target = MScaleOut.action, args = (shape, speed))
        t.start()


class MScaleIn():
    @staticmethod
    def stepForward(shape):
        if not (shape.getWidth() >= shape.getMaxWidth() or shape.getHeight() >= shape.getMaxHeight()):
            # Calculating the 1% of maximum width and height
            w = math.ceil((shape.getMaxWidth() / 100))
            h = math.ceil((shape.getMaxHeight() / 100))
            # Keeping the shape in the center
            shape.setMarginX(shape.getMarginX() - (w / 2))
            shape.setMarginY(shape.getMarginY() - (h / 2))
            # Increasing the width and height by 1%
            shape.setWidth(shape.getWidth() + w)
            shape.setHeight(shape.getHeight() + h)
            return False
        else:
            return True

    @staticmethod
    def stop(shape):
        shape.setScaleAnimationRunning(False)

    @staticmethod
    def action(shape, speed = 0.016667):
        t = False
        if shape.isScaleAnimationRunning():
            shape.setScaleAnimationRunning(False)
            time.sleep(speed + 0.001)
        if not shape.isScaleAnimationRunning():
            shape.setScaleAnimationRunning(True)
            while not t:
                if not shape.isScaleAnimationRunning():
                    return False
                t = MScaleIn.stepForward(shape)
                shape.update()
                QApplication.processEvents()
                time.sleep(speed)
            shape.setScaleAnimationRunning(False)
            return True
        else:
            return False

    @staticmethod
    def start(shape, speed):
        t = Thread(target = MScaleIn.action, args = (shape, speed))
        t.start()

