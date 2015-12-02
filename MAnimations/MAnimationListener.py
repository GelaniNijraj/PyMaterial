__author__ = "Samvid Mistry"

import abc


class MAnimationListener:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def onAnimationStart(self, animation):
        """
        Called by MAnimator when the animation is started, after any start delay is elapsed.
        :param animation: MAnimator
        :return: None
        """
        pass

    @abc.abstractmethod
    def onAnimationEnd(self, animation):
        """
        Called by MAnimator when the animation is ended.
        :param animation: MAnimator
        :return: None
        """
        pass

    @abc.abstractmethod
    def onAnimationCancel(self, animation):
        """
        Called by MAnimator when the animation is cancelled.
        :param animation: MAnimator
        :return: None
        """
        pass
