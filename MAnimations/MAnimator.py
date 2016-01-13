__author__ = "MaitreyaBuddha"

import abc
from threading import Thread
from PySide.QtCore import Signal, QObject


class MAnimator(QObject):
    __metaclass__ = abc.ABCMeta

    # Various signals which will be emitted from inside the animate function
    # in the subclass
    start_signal = Signal()
    pause_signal = Signal()
    end_signal = Signal()
    resume_signal = Signal()
    cancel_signal = Signal()

    def __init__(self):
        QObject.__init__(self)

        # Indicates that the animation is paused in between
        self.__paused = False

        # Indicates that the animation have been started
        self.__started = False

        # Indicates that the animation is currently running
        self.__running = False

        # Indicates that the animation can be run in reverse
        self.__run_reversed = False

        # Indicate that the animation is canceled
        self.__cancel = False

        # Indicates that the animation is ended
        self.__end = False

        # Stores the start delay of the animation in seconds
        self.__start_delay = 0

        # Stores the duration in which the animation should be completed
        self.__duration = 0

        # Holds the shapes to which animation should be applied
        self.__shapes = []

    def start(self):
        """
        This method is called by the user to start the animation on a shape
        after setting the delay. It starts the thread of animate() function
        and passes the list of shapes as an argument.
        :return: None
        """
        self.started = True
        t = Thread(target=self.animate, args=(self.__shapes,))
        t.start()

    @abc.abstractmethod
    def animate(self, shape):
        """
        This method must contain the core animation logic and should also
        emit appropriate signals at appropriate point in the execution
        in the overridden method.
        :param shape: list
        :return: None
        """
        raise NotImplementedError

    def cancel(self):
        """
        This method sets the __cancel flag to True. Canceling the animation
        includes setting the values of the shape to the values which were set
        before the animation started.
        This flag should be continuously checked and appropriate action must
        be taken inside the animate().
        :return: None
        """
        self.canceled = True

    def end(self):
        """
        This method sets the __end flag to True. Ending the animation includes
        setting the values of the shape to the final values which would have
        been there if animation was completed successfully.
        This flag should be continuously checked and appropriate action must
        be taken inside the animate().
        :return: None
        """
        self.ended = True

    def pause(self):
        """
        This method sets the the __paused flag to True(pauses the animation)
        if it's not already paused and is running.
        This flag should be continuously checked and appropriate action must
        be taken inside the animate().
        :return: None
        """
        if self.running and not self.paused:
            self.paused = True

    def resume(self):
        """
        This method sets the __paused flag to False(resumes the animation)
        if it is paused.
        :return: None
        """
        if self.__paused:
            self.__paused = False

    def add_target(self, shape):
        """
        This method adds a target MShape object to the __shapes list which
        is passed to the animate() thread.
        Each shape in __shapes should be processed and updated individually.
        :param shape: MShape : The shape on which animation is to be done.
        :return: None
        """
        self.__shapes.append(shape)

    def removeTarget(self, shape):
        """
        This method removes the specified shape from the __shapes list.
        :param shape: MShape : Shape to be removed from the __shapes list.
        :return: bool : Whether or not the shape was found or not.
        """
        try:
            self.__shapes.remove(shape)
            return True
        except ValueError:
            return False

    @property
    def started(self):
        """

        :return: bool
        """
        return self.__started

    @started.setter
    def started(self, started):
        self.__started = started

    @property
    def canceled(self):
        return self.__cancel

    @canceled.setter
    def canceled(self, cancel):
        self.__cancel = cancel

    @property
    def ended(self):
        return self.__end

    @ended.setter
    def ended(self, end):
        self.__end = end

    @property
    def paused(self):
        return self.__paused

    @paused.setter
    def paused(self, paused):
        self.__paused = paused

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, is_it):
        self.__running = is_it

    @property
    def start_delay(self):
        return self.__start_delay

    @start_delay.setter
    def start_delay(self, delay):
        self.__start_delay = delay / 1000

    @property
    def can_run_reversed(self):
        return self.__run_reversed

    @can_run_reversed.setter
    def can_run_reversed(self, can):
        self.__run_reversed = can
