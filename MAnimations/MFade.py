import time
from MAnimations.MAnimator import MAnimator
from PySide.QtGui import QApplication

__author__ = 'MaitreyaBuddha'


class MFadeOut(MAnimator):
    def __init__(self):
        MAnimator.__init__(self)

    def animate(self, shapes):
        self.start_signal.emit()
        # Sleeping to account the start_delay
        time.sleep(self.start_delay)
        self.running = True
        # Used to store the original opacities of the shapes
        original_opacity = []
        # Used to store opacity to be reduced bu each frame
        reduce_rate = []
        # Getting the original opacities of shapes in case the animation is
        # canceled in between
        for s in shapes:
            original_opacity.append(s.opacity)
            # Uses formula (((start - target) / fps) * (1000 / duration))
            reduce_rate.append((s.opacity / self.fps) * (1000 / self.duration))

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
                # Setting the opacity to the final value, i.e. min_opacity
                # in case if the animation was ended
                for s in shapes:
                    s.opacity = s.min_opacity
                # Emitting end signal
                self.end_signal.emit()
                return
            elif self.paused:
                # Emitting pause signal
                self.pause_signal.emit()
                # Loop which will hold the thread until the animation is
                # paused
                while not self.paused:
                    pass
                # Emitting resume signal
                self.resume_signal.emit()
            else:
                # Sleeping for 1/60 seconds, for 60fps
                time.sleep(1 / self.fps)
                # Flag to find out even if one shape is left to complete the
                # whole fade out animation
                completed = False
                shape_counter = 0
                for s in shapes:
                    if s.opacity > s.min_opacity:
                        # Reducing the opacity by 0.1 if the opacity is not
                        # already below minimum
                        s.opacity = float("%.6f" % (s.opacity - reduce_rate[shape_counter]))
                        s.update()
                        QApplication.processEvents()
                    else:
                        completed = True
                    shape_counter += 1

                if completed:
                    # Emitting end signal
                    self.end_signal.emit()
                    self.started = False
                    self.ended = True
                    # Complete the thread if all shapes are faded out to
                    # its minimum opacity
                    return
