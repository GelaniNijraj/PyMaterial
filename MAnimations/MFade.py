import time

from PySide.QtGui import QApplication

from MAnimations.MAnimate import MAnimate
from MBase import *


class MFade(MAnimate):
    """
    Can be used to set desired opacity of an MShape object.
    (Does not handle children).
    Requires target to be any fractional value between 0 and 1,
    including 0 and 1 (0 for complete invisibility and 1 for complete
    visibility)
    """
    def __init__(self):
        MAnimate.__init__(self)
        self.can_run_reversed = True

    def animate(self, shapes):
        self.start_signal.emit()
        # Sleeping to account the start_delay
        # TODO: Sleeping here's not gonna work, think somewhere else
        time.sleep(self.start_delay)
        self.running = True
        self.ended = False
        # Used to store the original opacities of the shapes
        original_opacity = []
        # Used to store opacity to be reduced bu each frame
        rate_of_change = []
        # Getting the original opacities of shapes in case the animation is
        # canceled in between
        try:
            if self.value_animators is None:
                pass
        except AttributeError:
            self.value_animators = []
            for s in shapes:
                print("target is", self.target)
                self.value_animators.append(MValueAnimator(s.opacity, self.target, self.duration, self.fps))


        # Main thread loop
        if self.running or self.paused:
            if self.canceled:
                # Restoring the opacity to the original in case the animation
                # was canceled
                for i, s in enumerate(shapes):
                    s.opacity = self.value_animators[i].get_original_value()
                    s.fading = False
                # Emitting cancel signal
                self.cancel_signal.emit()
                return
            elif self.ended:
                # Setting the opacity to the final value, i.e. target
                # in case if the animation was ended
                for s in shapes:
                    s.fading = False
                    s.opacity = self.target
                # Emitting end signal
                self.end_signal.emit()
                return
            elif self.paused:
                # Emitting pause signal
                self.pause_signal.emit()
                # Loop which will hold the thread until the animation is
                # paused
                if not self.paused:
                    # If you want the current state, pause the
                    # animation and then cancel it
                    if self.canceled:
                        self.ended = True
                        self.started = False
                        self.cancel_signal.emit()
                        for s in shapes:
                            s.fading = False
                        return
                # Emitting resume signal
                self.resume_signal.emit()
            else:
                # Flag to find out even if one shape is left to complete the
                # whole fade out animation
                completed = False
                for shape_counter, s in enumerate(shapes):
                    try:
                        s.opacity = self.value_animators[shape_counter].step()
                    except MFinalValueReachedException:
                        print("we're done, bruh")
                        completed = True
                        break
                    s.update()
                    QApplication.processEvents()

                if completed:
                    # Emitting end signal
                    for s in shapes:
                        s.fading = False
                    self.end_signal.emit()
                    self.started = False
                    self.ended = True
                    # Complete the thread if all shapes are faded to
                    # its target
                    return False
