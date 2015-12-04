__author__ = 'MaitreyaBuddha'

import time
from MAnimations.MAnimator import MAnimator
from PySide.QtGui import QApplication


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
        # Getting the original opacities of shapes in case the animation is
        # canceled in between
        for s in shapes:
            original_opacity.append(s.opacity)
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
                time.sleep(1/60)
                # Flag to find out even if one shape is left to complete the
                # whole fade out animation
                completed = False
                for s in shapes:
                    if s.opacity > s.min_opacity:
                        # Reducing the opacity by 0.1 if the opacity is not
                        # already below minimum
                        # TODO:
                        # calculate the opacity to be reduced on each frame
                        # to fit animation inside the duration
                        s.opacity = float("%.2f"%(s.opacity-0.01))
                        s.update()
                        QApplication.processEvents()
                        print(s.opacity)
                    else:
                        completed = True

                if completed:
                    # Emitting end signal
                    self.end_signal.emit()
                    self.started = False
                    self.ended = True
                    # Complete the thread if all shapes are faded out to
                    # its minimum opacity
                    return