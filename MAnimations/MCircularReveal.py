from math import sqrt

__author__ = "Samvid Mistry"

import time
from MAnimations.MAnimate import MAnimate
from PySide.QtGui import QApplication, QPainterPath
from PySide.QtCore import QPoint, QPointF


class MCircularReveal(MAnimate):
    """
    Can be used to perform circular reveal or circular hide animation
    on an MShape object.
    Requires self.target to be either 'show[_circle]' or 'hide[_circle]'
    """
    def __init__(self):
        MAnimate.__init__(self)
        self.__clip = QPainterPath()

    def animate(self, shapes):
        self.start_signal.emit()
        time.sleep(self.start_delay)
        self.running = True
        self.ended = False
        target_radius = []
        original_clips = []
        centers = []
        animating_radius = []
        rate_of_change = []
        for s in shapes:
            if self.target.startswith("show"):
                # Setting max of width or height as radius, ergo "circular" reveal,
                # not "oval" reveal
                side = max(s.width, s.height)
                side_square = side * side
                # Applying pythagoras theorem
                target = sqrt(side_square + side_square)
                # Starting from the zero reaching the max
                animating_radius.append(0)
                rate_of_change.append((target / self.fps) * (1000 / self.duration))
            elif self.target.startswith("hide"):
                # You know why...
                target = 0
                # Starting from the max reaching the 0
                animating_radius.append(max(s.width, s.height))
                rate_of_change.append(((target - max(s.width, s.height)) / self.fps) * (1000 / self.duration))
            else:
                raise ValueError("Target should be either 'reveal' or 'hide'")
            target_radius.append(target)
            # Getting the original masks; Used in case of cancellation
            original_clips.append(s.clip)
            # Center of the shape, considering margin
            centers.append(QPoint((s.width / 2) + s.margin_left, (s.height / 2) + s.margin_top))
            # Calculating the increase rate using the good ol' formula
        while self.running or self.paused:
            if self.canceled and not self.paused:
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
                while self.paused:
                    # If you want the current state, pause the
                    # animation and then cancel it
                    if self.canceled:
                        self.ended = True
                        self.started = False
                        self.cancel_signal.emit()
                        return
                self.resume_signal.emit()
            else:
                # Setting FPS from the animator
                time.sleep(1 / self.fps)
                completed = False
                for i, s in enumerate(shapes):
                    if rate_of_change[i] > 0:
                        if not animating_radius[i] < target_radius[i]:
                            completed = True
                    else:
                        # TODO: leaves 1 pixel visible in hiding the check,
                        # added 1 to overall radius checking for now, look into this issue
                        if not animating_radius[i] > target_radius[i] + 1:
                            completed = True
                    if not completed:
                        animating_radius[i] += rate_of_change[i]
                    path = QPainterPath()
                    if self.target.endswith("circle"):
                        path.addEllipse(
                            QPointF((s.width / 2) + s.margin_left,
                            (s.height / 2) + s.margin_top),
                            animating_radius[i] / 2,
                            animating_radius[i] / 2
                        )
                    else:
                        path.addEllipse(
                            QPointF((s.width / 2) + s.margin_left,
                            (s.height / 2) + s.margin_top),
                            animating_radius[i],
                            animating_radius[i]
                        )

                    s.clip = path
                    s.update()
                    QApplication.processEvents()
                # No need to check on every iteration, duration is same so
                # all objects are gonna end at the same time
                if completed:
                    self.end_signal.emit()
                    self.started = False
                    self.ended = True
                    return
