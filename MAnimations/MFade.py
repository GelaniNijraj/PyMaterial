__author__ = 'MaitreyaBuddha'

import time

from PySide.QtGui import QApplication

from MAnimations.MAnimator import MAnimator


class MFade(MAnimator):
    """
    Can be used to set desired opacity of an MShape object.
    (Does not handle children).
    Requires target to be any fractional value between 0 and 1,
    including 0 and 1
    """
    def __init__(self):
        MAnimator.__init__(self)
        self.can_run_reversed = True

    def animate(self, shapes):
        self.start_signal.emit()
        # Sleeping to account the start_delay
        print(self.target)
        time.sleep(self.start_delay)
        self.running = True
        self.ended = False
        # Used to store the original opacities of the shapes
        original_opacity = []
        # Used to store opacity to be reduced bu each frame
        rate_of_change = []
        # Getting the original opacities of shapes in case the animation is
        # canceled in between
        for s in shapes:
            original_opacity.append(s.opacity)
            # Uses formula (((start - target) / fps) * (1000 / duration))
            rate_of_change.append(
                ((self.target - s.opacity) / self.fps) *
                (1000 / self.duration)
            )

        # Main thread loop
        while self.running or self.paused:
            if self.canceled:
                # Restoring the opacity to the original in case the animation
                # was canceled
                for i, s in enumerate(shapes):
                    s.opacity = original_opacity[i]
                # Emitting cancel signal
                self.cancel_signal.emit()
                return
            elif self.ended:
                # Setting the opacity to the final value, i.e. target
                # in case if the animation was ended
                for s in shapes:
                    s.opacity = self.target
                # Emitting end signal
                self.end_signal.emit()
                return
            elif self.paused:
                # Emitting pause signal
                self.pause_signal.emit()
                # Loop which will hold the thread until the animation is
                # paused
                while not self.paused:
                    # If you want the current state, pause the
                    # animation and then cancel it
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
                # whole fade out animation
                completed = False
                for shape_counter, s in enumerate(shapes):
                    if rate_of_change[shape_counter] > 0:
                        if s.opacity < self.target:
                            s.opacity = \
                                float(
                                    "%.6f" %
                                    (s.opacity + rate_of_change[shape_counter])
                                )
                        else:
                            completed = True
                    else:
                        if s.opacity > self.target:
                            s.opacity = \
                                float(
                                    "%.6f" %
                                    (s.opacity + rate_of_change[shape_counter])
                                )
                        else:
                            completed = True
                    s.update()
                    QApplication.processEvents()

                if completed:
                    # Emitting end signal
                    self.end_signal.emit()
                    self.started = False
                    self.ended = True
                    # Complete the thread if all shapes are faded to
                    # its target
                    return
