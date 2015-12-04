__author__ = 'MaitreyaBuddha'

import time
from MAnimations.MAnimator import MAnimator


class MFadeOut(MAnimator):
    def animate(self, shape):
        time.sleep(self.start_delay)
        self.running = True
        original_opacity = shape.opacity
        while self.running or self.paused:
            if self.canceled:
                shape.opacity = original_opacity
                return
            elif self.ended:
                shape.opacity = shape.min_opacity
                self.iEndSignal.emit("ended")
                return
            elif self.paused:
                while not self.paused:
                    pass
            else:
                if shape.opacity > shape.min_opacity:
                    shape.opacity -= 0.1
                    time.sleep(1/60)
                else:
                    self.running = False
                    return