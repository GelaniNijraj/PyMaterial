__author__ = 'MaitreyaBuddha'

import time
from MAnimations.MAnimator import MAnimator


class MFadeOut(MAnimator):
    def animate(self, shapes):
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
                return
            elif self.ended:
                # Setting the opacity to the final value, i.e. min_opacity
                # in case if the animation was ended
                for s in shapes:
                    s.opacity = s.min_opacity
                return
            elif self.paused:
                # Loop which will hold the thread until the animation is
                # paused
                while not self.paused:
                    pass
            else:
                # Sleeping for 1/60 seconds, for 60fps
                time.sleep(1/60)
                # Flag to find out even if one shape is left to complete the
                # whole fade out animation
                completed = True
                for s in shapes:
                    if s.opacity > s.min_opacity:
                        # Reducing the opacity by 0.1 if the opacity is not
                        # already below minimum
                        s.opacity -= 0.1
                    else:
                        completed = False
                if completed:
                    # Complete the thread if all shapes are faded out to
                    # its minimum opacity
                    return