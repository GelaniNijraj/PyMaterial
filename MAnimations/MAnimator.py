__author__ = "Samvid Mistry"

import abc


class MAnimator:
    """
    Super class for all the classes providing any kind of animation support with MShape.

    @see MUtilities.MShape
    """
    __metaclass__ = abc.ABCMeta

    # Listener for lifecycle of animation.
    iListeners = list()

    # Listener for pause and resume of animation.
    iPauseListeners = list()

    # Check for animation state.
    iPaused = False

    # Checks if the animation is started or not. This gives true if the animation is currently running
    # as well as returns true if the animation is in starting delay.
    iStarted = False

    # Check if animation is started. This means that the animation is past any start delay and is currently
    # animating the MShape
    iRunning = False

    # The time to wait after call to start to start the animation. It is in milliseconds.
    iStartDelay = 0

    # The duration of animation
    iDuration = 0

    def start(self):
        """
        Starts the animation on the MShape. If no delay is set, then the animation would immediately start
        by setting initial values and calling {@link MAnimationListener.onAnimationStart()}, else it would start
        elapsing the delay. Subclasses should call {@link notifyAnimationStart()} when appropriate to tell the
        listeners that the animation has been started.
        :return: None

        @see notifyAnimationStart()
        """
        pass

    def cancel(self):
        """
        Cancels the animation on MShape. Cancelling involves setting all the values of MShape to the values
        before animation started. Subclasses should call {@link notifyAnimationCancel()} when appropriate to
        tell the listeners that the animation has been cancelled.
        :return: None

        @see notifyAnimationCancel()
        """
        pass

    def end(self):
        """
        Ends the animation on MShape. Ending animation would skip all the frames between the current state
        of animation and end of animation and will directly set MShape to final values. Subclasses should call
        {@link notifyAnimationEnd()} when appropriate to tell the listeners that the animation has been ended.
        :return: None

        @see notifyAnimationEnd()
        """
        pass

    def notifyAnimationStart(self):
        """
        Tells all the animation listeners that animation has started.
        :return: None

        @see MAnimationListener
        """
        if len(self.iListeners) > 0:
            for listener in self.iListeners:
                listener.onAnimationStart(self)

    def notifyAnimationCancel(self):
        """
        Tells all the animation listeners that animation has cancelled.
        :return: None

        @see MAnimationListener
        """
        if len(self.iListeners) > 0:
            for listener in self.iListeners:
                listener.onAnimationCancel(self)

    def notifyAnimationEnd(self):
        """
        Tells all the animation listeners that animation has ended.
        :return: None

        @see MAnimationListener
        """
        if len(self.iListeners) > 0:
            for listener in self.iListeners:
                listener.onAnimationEnd(self)

    def isRunning(self):
        """
        Checks if the animation is currently running. This means the animation is currently out of start
        delay and is currently animation MShape.
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
        Pauses the animation and calls {@link MAnimationPauseListener.onAnimationPause()} on all the
        {@link MAnimationPauseListener} listeners.
        :return: None
        """
        if self.iRunning and not self.iPaused:
            self.iPaused = True
            if len(self.iPauseListeners) > 0:
                for listener in self.iPauseListeners:
                    listener.onAnimationPause(self)

    def resume(self):
        """
        Resumes the animation and calls {@link MAnimationPauseListener.onAnimationResume()} on all the
        {@link MAnimationPauseListener} listeners.
        :return: None
        """
        if self.iPaused:
            self.iPaused = False
            if len(self.iPauseListeners) > 0:
                for listener in self.iPauseListeners:
                    listener.onAnimationResume(self)

    def setStartDelay(self, startDelay):
        """
        Sets the start delay for animation. Animator would wait this much milliseconds to actually start
        the animation.
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
        Sets the interpolator for animation to the provided interpolator. For more information on what an
        interpolator is, see {@link MInterpolator}.
        :param interpolator: MInterpolator
        :return: None

        @see MInterpolator
        """
        pass

    def getInterpolator(self):
        """
        Returns the interpolator used by the animator. For more information on what an
        interpolator is, see {@link MInterpolator}.
        :return: None

        #see setInterpolator()
        """
        return None

    def addListener(self, listener):
        """
        Adds an animation listener to the animation, for more information on what an animation listener is, see
        {@link MAnimationListener}
        :param listener: MAnimationListener
        :return: None

        @see MAnimationListener
        """
        self.iListeners.append(listener)

    def removeListener(self, listener):
        """
        Removes the provided animation listener from the list of animation listeners, for more information
        on what an animation listener is, see {@link MAnimationListener}
        :param listener: MAnimationListener
        :return: None

        @see MAnimationListener
        """
        if len(self.iListeners) > 0:
            self.iListeners.remove(listener)

    def addPauseListener(self, listener):
        """
        Adds an animation pause listener to the animation, for more information on what an animation pause listener
        is, see {@link MAnimationPauseListener}
        :param listener: MAnimationPauseListener
        :return: None

        @see MAnimationPauseListener
        """
        self.iPauseListeners.append(listener)

    def removePauseListener(self, listener):
        """
        Removes the provided animation pause listener from the list of animation pause listeners, for more
        information on what an animation pause listener is, see {@link MAnimationPauseListener}
        :param listener: MAnimationPauseListener
        :return: None

        @see MAnimationPauseListener
        """
        if len(self.iPauseListeners) > 0:
            self.iPauseListeners.remove(listener)

    def removeAllListeners(self):
        """
        Removes all the listeners from animator object, for more information on listeners, see
        {@link MAnimationListener, MAnimationPauseListener}.
        :return: None

        @see MAnimationListener, MAnimationPauseListener
        """
        if len(self.iListeners) > 0:
            for listener in self.iListeners:
                self.iListeners.remove(listener)

        if len(self.iPauseListeners) > 0:
            for listener in self.iPauseListeners:
                self.iPauseListeners.remove(listener)

    @abc.abstractmethod
    def addTarget(self, shape):
        """
        Sets the target for animation to run on. Multiple targets can also be assigned if subclass implements so.
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

    @abc.abstractmethod
    def canRunReversed(self):
        """
        Tells if the animation can be run in reversed manner.
        :return: Boolean

        @see runReversed()
        """
        return False

    @abc.abstractmethod
    def runReversed(self):
        """
        Method to allow animation to be run in reverse manner. Subclasses can provide support for that.
        :return: None
        """
        pass
