__author__ = 'MaitreyaBuddha'

from .MFade import MFade
from .MScale import MScale
from .MCircularReveal import MCircularReveal


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
        animator_name = 'fade'
        self.__to_animate[animator_name] = {
            'target': target,
            'duration': duration,
            'animator': MFade()
        }

        # # Check if there is any ongoing animation
        # if self.__animations[animator_name] is not None:
        #     # then cancel that animation while saving the state
        #     self.__animations[animator_name]['animator'].paused = True
        #     self.__animations[animator_name]['animator'].canceled = True
        #     # Resetting the animation
        #     self.__animations[animator_name] = None
        # # Now worry about the current animation
        # # Building the animation dictionary
        return self

    def scale(self, target, duration=0):
        animator_name = 'scale'
        # Check if there is any ongoing animation
        if self.__animations[animator_name] is not None:
            # then cancel that animation while saving the state
            self.__animations[animator_name]['animator'].paused = True
            self.__animations[animator_name]['animator'].canceled = True
            # Resetting the animation
            self.__animations[animator_name] = None
        # Now worry about the current animation
        # Building the animation dictionary
        self.__animations[animator_name] = {
            'target': target,
            'duration': duration,
            'animator': MScale()
        }
        return self

    def reveal(self, target, duration=0):
        animator_name = 'reveal'
        # Check if there is any ongoing animation
        if self.__animations[animator_name] is not None:
            # then cancel that animation while saving the state
            self.__animations[animator_name]['animator'].pause()
            self.__animations[animator_name]['animator'].cancel()
            # Resetting the animation
            self.__animations[animator_name] = None
        # Now worry about the current animation
        # Building the animation dictionary
        self.__animations[animator_name] = {
            'target': target,
            'duration': duration,
            'animator': MCircularReveal()
        }
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
            print("poop", animation, parmas)
            if parmas is not None:
                if self.__animations[animation] is not None:
                    print("already exists so canceling")
                    # canceling at the current state if there is an ongoing animation
                    self.__animations[animation]['animator'].pause()
                    self.__animations[animation]['animator'].cancel()
                # setting up the duration and target
                print("parmas are", parmas)
                parmas['animator'].target = parmas['target']
                if parmas['duration'] != 0:
                    parmas['animator'].duration = parmas['duration']
                else:
                    parmas['animator'].duration = self.__duration
                # storing it for the next round
                self.__animations[animation] = parmas
                # finally, starting that shit
                parmas['animator'].add_target(self)
                parmas['animator'].start()
