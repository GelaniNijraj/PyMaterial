__author__ = 'MaitreyaBuddha'

from .MFade import MFade
from .MScale import MScale
from .MCircularReveal import MCircularReveal

from MBase import *

animation_thread = MAnimationThread()
animation_thread.start()


class MAnimator:
    def animate(self):
        """
        Initializing all the required variables
        :return: MAnimate
        """
        try:
            # Check if animations is already declared
            if self.__animations is None:
                pass
        except AttributeError:
            # If not, initialize all known animations to None
            self.__animations = {'fade': None, 'scale': None, 'reveal': None}
        # List of classes with respective animations
        self.__to_animate = {'fade': None, 'scale': None, 'reveal': None}
        self.__duration = 1000
        self.__end_listener = None
        return self

    def fade(self, target, duration=0):
        animation_name = 'fade'
        self.__to_animate[animation_name] = {
            'target': target,
            'duration': duration,
            'animator': MFade()
        }

        # Check if there is any ongoing animation
        if self.__animations[animation_name] is not None:
            # then cancel that animation while saving the state
            self.__animations[animation_name]['animator'].paused = True
            self.__animations[animation_name]['animator'].canceled = True
            # Resetting the animation
            self.__animations[animation_name] = None
        # Now worry about the current animation
        # Building the animation dictionary
        return self

    def duration(self, duration):
        self.__duration = duration
        return self

    def when_ends(self, end_listener):
        """
        Function to be executed when animations ends. i.e. end listener
        :param end_listener:
        :return:
        """
        self.__end_listener = end_listener
        return self

    def start(self):
        for animation, parmas in self.__to_animate.items():
            if parmas is not None:
                if self.__animations[animation] is not None:
                    print("already exists so canceling")
                    # canceling at the current state if there is an
                    # ongoing animation
                    self.__animations[animation]['animator'].pause()
                    self.__animations[animation]['animator'].cancel()
                # setting up the duration and target)
                parmas['animator'].target = parmas['target']
                if parmas['duration'] != 0:
                    parmas['animator'].duration = parmas['duration']
                else:
                    parmas['animator'].duration = self.__duration
                # storing it for the next round
                self.__animations[animation] = parmas
                # finally, starting that shit
                parmas['animator'].add_target(self)
                parmas['animator'].start(animation_thread)
