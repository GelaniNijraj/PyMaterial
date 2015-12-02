__author__ = "Samvid Mistry"

import abc


class MAnimationPauseListener:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def onAnimationPause(self, animation):
        """
        Called from {@link MAnimator} when animation is paused.
        :param animation: MAnimator
        :return: None
        """
        pass

    @abc.abstractmethod
    def onAnimationResume(self, animation):
        """
        Called from {@link MAnimator} when animation is resumed.
        :param animation: MAnimator
        :return: None
        """
        pass
