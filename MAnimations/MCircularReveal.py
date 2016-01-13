__author__ = "Samvid Mistry"

import time
from MAnimations.MAnimator import MAnimator
from PySide.QtGui import QApplication, QPainterPath
from PySide.QtCore import QPointF


class MCircularReveal(MAnimator):
    def __init__(self):
        MAnimator.__init__(self)
        self.__clip = QPainterPath()
        self.duration = 300

    def animate(self, shapes):
        self.start_signal.emit()

        time.sleep(self.start_delay)

        self.running = True

        original_width = []
        original_height = []
        centers = []
        animating_width = []
        animating_height = []
        inc_width = []
        inc_height = []

        for s in shapes:
            original_width.append(s.width)
            original_height.append(s.height)
            animating_width.append(0)
            animating_height.append(0)
            centers.append(-1)
            inc_width.append(float(s.width) / self.duration)
            inc_height.append(float(s.height) / self.duration)

        while self.running or self.paused:
            if self.canceled:
                self.cancel_animation(shapes, original_width, original_height)
                return

            elif self.ended:
                self.end_signal.emit()
                return

            else:
                time.sleep(1 / 1000)
                completed = False

                for i, s in enumerate(shapes):

                    if animating_width[i] < s.width and animating_height[i] < s.height:
                        if centers[i] is -1:
                            centers[i] = QPointF(s.width / 2, s.height / 2)

                        self.__clip = QPainterPath()
                        self.__clip.addEllipse(centers[i], animating_width[i], animating_height[i])
                        s.clip = self.__clip
                        s.update()
                        QApplication.processEvents()

                        print(str(s.width) + " " + str(s.height) + " " + str(animating_width[i]) + " " + str(
                                animating_height[i]))

                        animating_width[i] += inc_width[i]
                        animating_height[i] += inc_height[i]
                    else:
                        completed = True

                    if completed:
                        self.end_signal.emit()
                        self.started = False
                        self.ended = True
                        return

    def cancel_animation(self, shapes, original_width, original_height):
        for i, s in enumerate(shapes):
            s.width = original_width[i]
            s.height = original_height[i]

        self.cancel_signal.emit()
