__author__ = "MaitreyaBuddha"

import abc
from PySide.QtCore import Signal
from MUtilities import MShape


class MAnimator():
    """
    Super class for all the classes providing any kind of animation support
    with MShape.

    @see MUtilities.MShape
    """
    __metaclass__ = abc.ABCMeta

    # Signals declaration
    iStartSignal = Signal(str)
    iPauseSignal = Signal(str)
    iEndSignal = Signal(str)
    iResumeSignal = Signal(str)

    # Check for animation state.
    iPaused = False

    # Checks if the animation is started or not. This gives true if the
    # animation is currently running as well as returns true if the
    # animation is in starting delay.
    iStarted = False

    # Check if animation is started. This means that the animation is past
    # any start delay and is currently animating the MShape
    iRunning = False

    # The time to wait after call to start to start the animation.
    # It is in milliseconds.
    iStartDelay = 0

    # The duration of animation
    iDuration = 0

    # Holds the shapes which are going to be animated
    iShape = ()

    i_run_reversed = False

    @abc.abstractmethod
    def start(self):
        """
        Starts the animation on the MShape. If no delay is set, then the
        animation would immediately start by setting initial values and
        calling {@link MAnimationListener.onAnimationStart()}, else it would
        start elapsing the delay. Subclasses should call
        {@link notifyAnimationStart()} when appropriate to tell the listeners
        that the animation has been started.
        :return: None

        @see notifyAnimationStart()
        """
        raise NotImplementedError

    @abc.abstractmethod
    def cancel(self):
        """
        Cancels the animation on MShape. Cancelling involves setting all the
        values of MShape to the values before animation started. Subclasses
        should call {@link notifyAnimationCancel()} when appropriate to tell
        the listeners that the animation has been cancelled.
        :return: None

        @see notifyAnimationCancel()
        """
        raise NotImplementedError

    @abc.abstractmethod
    def end(self):
        """
        Ends the animation on MShape. Ending animation would skip all the
        frames between the current state of animation and end of animation
        and will directly set MShape to final values. Subclasses should call
        {@link notifyAnimationEnd()} when appropriate to tell the listeners
        that the animation has been ended.
        :return: None

        @see notifyAnimationEnd()
        """
        raise NotImplementedError

    def isRunning(self):
        """
        Checks if the animation is currently running. This means the animation
        is currently out of start delay and is currently animation MShape.
        :return: Boolean
        """
        return not self.iRunning

    def isPaused(self):
        """
        A logical compliment of method {@link isRunning()}
        :return: Boolean
        """
        return self.iPaused

    def pause(self):
        """
        Pauses the animation and calls
        {@link MAnimationPauseListener.onAnimationPause()} on all the
        {@link MAnimationPauseListener} listeners.
        :return: None
        """
        if self.iRunning and not self.iPaused:
            self.iPaused = True

    def resume(self):
        """
        Resumes the animation and calls
        {@link MAnimationPauseListener.onAnimationResume()} on all the
        {@link MAnimationPauseListener} listeners.
        :return: None
        """
        if self.iPaused:
            self.iPaused = False

    def setStartDelay(self, startDelay):
        """
        Sets the start delay for animation. Animator would wait this much
        milliseconds to actually start the animation.
        :param startDelay: int
        :return: None
        """
        self.iStartDelay = startDelay

    def getStartDelay(self):
        """
        Returns start delay for animation in milliseconds.
        :return: int

        @see setStartDelay()
        """
        return self.iStartDelay

    def setDuration(self, duration):
        """
        Total duration of animation in milliseconds.
        :param duration: int
        :return: int
        """
        self.iDuration = duration

    def getDuration(self):
        """
        Returns the total duration of animation in milliseconds
        :return: int

        @see setDuration()
        """
        return self.iDuration

    @abc.abstractmethod
    def setInterpolator(self, interpolator):
        """
        Sets the interpolator for animation to the provided interpolator.
        For more information on what an interpolator is, see
        {@link MInterpolator}.
        :param interpolator: MInterpolator
        :return: None

        @see MInterpolator
        """
        pass

    def getInterpolator(self):
        """
        Returns the interpolator used by the animator. For more information on
        what an interpolator is, see {@link MInterpolator}.
        :return: None

        #see setInterpolator()
        """
        return None

    @abc.abstractmethod
    def addTarget(self, shape):
        """
        Sets the target for animation to run on. Multiple targets can also
        be assigned if subclass implements so.
        :param shape: MShape
        :return: None
        """
        pass

    @abc.abstractmethod
    def removeTarget(self, shape):
        """
        Removes the target for animation to run on.
        :param shape: MShape
        :return: None

        @see addTarget(MShape)
        """
        pass

    @abc.abstractproperty
    def can_run_reversed(self):
        """
        Tells if the animation can be run in reversed manner.
        :return: Boolean

        @see runReversed()
        """
        return False

    @abc.abstractmethod
    def run_reversed(self):
        """
        Method to allow animation to be run in reverse manner. Subclasses can
        provide support for that.
        :return: None
        """
        pass
