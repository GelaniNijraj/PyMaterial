import time
from threading import Thread
from PySide.QtGui import QApplication

__author__ = 'MaitreyaBuddha'


class MFadeOut():
    @staticmethod
    def stepForward(shape):
        if not shape.getOpacity() <= shape.getMinOpacity():
            shape.setOpacity(shape.getOpacity() - 0.01)
            return False
        else:
            return True

    @staticmethod
    def stop(shape):
        shape.setFadeAnimationRunning(False)

    @staticmethod
    def action(shape, speed=0.016667):
        t = False
        if shape.isFadeAnimationRunning():
            shape.setFadeAnimationRunning(False)
            time.sleep(speed + 0.001)
        if not shape.isFadeAnimationRunning():
            shape.setFadeAnimationRunning(True)
            while not t:
                if not shape.isFadeAnimationRunning():
                    return False
                t = MFadeOut.stepForward(shape)
                shape.update()
                QApplication.processEvents()
                time.sleep(speed)
            shape.setFadeAnimationRunning(False)
            return True
        else:
            return False

    @staticmethod
    def start(shape):
        t = Thread(target=MFadeOut.action, args=(shape, 0.006))
        t.start()


class MFadeIn():
    @staticmethod
    def stepForward(shape):
        if not shape.getOpacity() >= shape.getMaxOpacity():
            shape.setOpacity(shape.getOpacity() + 0.01)
            return False
        else:
            return True

    @staticmethod
    def stop(shape):
        shape.setFadeAnimationRunning(False)

    @staticmethod
    def action(shape, speed=0.016667):
        t = False
        if shape.isFadeAnimationRunning():
            shape.setFadeAnimationRunning(False)
            time.sleep(speed + 0.001)
        if not shape.isFadeAnimationRunning():
            shape.setFadeAnimationRunning(True)
            while not t:
                if not shape.isFadeAnimationRunning():
                    return False
                t = MFadeIn.stepForward(shape)
                shape.update()
                QApplication.processEvents()
                time.sleep(speed)
            shape.setFadeAnimationRunning(False)
            return True
        else:
            return False

    @staticmethod
    def start(shape):
        t = Thread(target=MFadeIn.action, args=(shape, 0.006))
        t.start()
