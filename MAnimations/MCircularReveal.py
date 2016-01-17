__author__ = "Samvid Mistry"

import time
from MAnimations.MAnimator import MAnimator
from PySide.QtGui import QApplication, QPainterPath
from PySide.QtCore import QPoint


class MCircularReveal(MAnimator):
    def __init__(self):
        MAnimator.__init__(self)
        self.__clip = QPainterPath()
        self.duration = 300

    def animate(self, shapes):
        self.start_signal.emit()

        time.sleep(self.start_delay)

        self.running = True
        self.ended = False

        max_radius = []
        original_clips = []
        centers = []
        animating_width = []
        animating_height = []
        animating_radius = []
        inc_rate = []

        for s in shapes:
            # Setting max of width or height as radius, ergo "circular" reveal,
            # not "oval" reveal
            target = max(s.width, s.height)
            max_radius.append(target)
            # Starting from the zero reaching the max
            animating_radius.append(0)
            # Getting the original masks; Used in case of cancelation
            original_clips.append(s.clip)
            # Center of the shape
            centers.append(QPoint((s.width / 2), (s.height / 2)))
            # Calculating the increase rate using the good ol' formula
            inc_rate.append((target / self.fps) * (1000 / self.duration))

        while self.running or self.paused:
            if self.canceled:
                for i, s in enumerate(shapes):
                    s.clip = original_clips[i]
                self.cancel_signal.emit()
                return

            elif self.ended:
                self.end_signal.emit()
                return

            elif self.paused:
                # Handling the pause
                self.pause_signal.emit()
                while not self.paused:
                    pass
                self.resume_signal.emit()

            else:
                # Setting FPS from the animator
                time.sleep(1 / self.fps)

                completed = False

                for i, s in enumerate(shapes):

                    if animating_radius[i] < max_radius[i]:
                        path = QPainterPath()
                        s.clip = path.addEllipse(centers[i], 10, 10)
                        print(centers[i], animating_radius[i], animating_radius[i])
                        s.update()
                        QApplication.processEvents()
                        animating_radius[i] += inc_rate[i]

                    else:
                        completed = True

                    if completed:
                        self.end_signal.emit()
                        self.started = False
                        self.ended = True
                        return