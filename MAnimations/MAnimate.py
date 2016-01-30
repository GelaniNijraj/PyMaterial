__author__ = 'MaitreyaBuddha'

from .MFade import MFade
from .MScale import MScale
from .MCircularReveal import MCircularReveal


class MAnimate:
    def animate(self):
        """
        Sets all the possible animation's values to None
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
        self.__animators = {'fade': 'MFade', 'scale': 'MScale', 'reveal': 'MCircularReveal'}
        self.__duration = 1000
        return self

    def fade(self, target, duration=0):
        animator_name = 'fade'
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
            'animator': MFade()
        }
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

    def start(self):
        for key, value in self.__animations.items():
            if value is not None:
                value['animator'].add_target(self)
                value['animator'].target = value['target']
                value['animator'].duration = value['duration']
                if value['duration'] == 0:
                    value['animator'].duration = self.__duration
                value['animator'].start()
