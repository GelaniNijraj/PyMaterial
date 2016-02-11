__author__ = 'MaitreyaBuddha'

import time

from PySide.QtGui import QApplication
from PySide.QtCore import QPoint, QPointF

from MAnimations.MAnimator import MAnimator


class MScale(MAnimator):
    """
    Can be used to scale an MShape object to desired size.
    (Does not handle children).
    Requires target to be a QPoint object where QPoint.x() is target
    width and QPoint.y() is target height.
    """
    def __init__(self):
        MAnimator.__init__(self)
        self.can_run_reversed = True

    def animate(self, shapes):
        self.start_signal.emit()
        # Sleeping to account the start_delay
        time.sleep(self.start_delay)
        self.running = True
        self.ended = False
        # Used to store the original size of the shapes
        original_size = []
        # Used to store size to be added by each frame
        rate_of_change = []
        # Getting the original opacities of shapes in case the animation is
        # canceled in between
        for s in shapes:
            original_size.append(QPoint(s.width, s.height))
            # Uses formula (((start - target) / fps) * (1000 / duration))
            tmp_point = QPointF(
                ((self.target.x() - s.width) / self.fps) * (1000 / self.duration),
                ((self.target.y() - s.height) / self.fps) * (1000 / self.duration)
            )
            rate_of_change.append(tmp_point)

        # Main thread loop
        while self.running or self.paused:
            if self.canceled:
                # Restoring the size to the original in case the animation
                # was canceled
                for i, s in enumerate(shapes):
                    s.width = original_size[i].x()
                    s.height = original_size[i].y()
                # Emitting cancel signal
                self.cancel_signal.emit()
                return
            elif self.ended:
                # Setting the size to the final value, i.e. target
                # in case if the animation was ended
                for s in shapes:
                    s.width = self.target.x()
                    s.width = self.target.y()
                # Emitting end signal
                self.end_signal.emit()
                return
            elif self.paused:
                # Emitting pause signal
                self.pause_signal.emit()
                # Loop which will hold the thread until the animation is
                # paused
                while not self.paused:
                    if self.canceled:
                        self.ended = True
                        self.started = False
                        self.cancel_signal.emit()
                        return
                # Emitting resume signal
                self.resume_signal.emit()
            else:
                # Sleeping for 1/60 seconds, for 60fps
                time.sleep(1 / self.fps)
                # Flag to find out even if one shape is left to complete the
                # whole animation
                completed = False
                for shape_counter, s in enumerate(shapes):
                    height_complete = False
                    width_complete = False
                    # Two values suck...
                    # First for width...
                    if rate_of_change[shape_counter].x() > 0:
                        if s.width < self.target.x():
                            s.width += rate_of_change[shape_counter].x()
                        else:
                            width_complete = True
                    else:
                        if s.width > self.target.x():
                            s.width += rate_of_change[shape_counter].x()
                        else:
                            width_complete = True
                    # ...and then for height
                    if rate_of_change[shape_counter].y() > 0:
                        if s.height < self.target.y():
                            s.height += rate_of_change[shape_counter].y()
                        else:
                            height_complete = True
                    else:
                        if s.height > self.target.y():
                            s.height += rate_of_change[shape_counter].y()
                        else:
                            height_complete = True

                    s.update()
                    QApplication.processEvents()
                    completed = width_complete & height_complete

                if completed:
                    # Emitting end signal
                    self.end_signal.emit()
                    self.started = False
                    self.ended = True
                    # Complete the thread if all shapes have reached to
                    # its target
                    return
