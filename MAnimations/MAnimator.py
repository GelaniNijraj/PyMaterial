__author__ = "MaitreyaBuddha"

import abc
import time
from threading import Thread
from PySide.QtCore import Signal
from MUtilities import MShape


class MAnimator():
    __metaclass__ = abc.ABCMeta

    iStartSignal = Signal(str)
    iPauseSignal = Signal(str)
    iEndSignal = Signal(str)
    iResumeSignal = Signal(str)

    __paused = False

    __started = False

    __running = False

    __run_reversed = False

    __cancel = False
    __end = False

    __start_delay = 0

    __duration = 0

    __shapes = []

    __threads = []

    def start(self):
        self.started = True
        for s in self.__shapes:
            t = Thread(target=self.animate, args=(s,))
            t.start()
            self.__threads.append(t)

    @abc.abstractmethod
    def animate(self, shape):
        raise NotImplementedError

    def cancel(self):
        self.canceled = True

    def end(self):
        self.ended = True

    def pause(self):
        if self.running and not self.paused:
            self.paused = True

    def resume(self):
        if self.__paused:
             self.__paused = False

    def addTarget(self, shape):
        self.__shapes.append(shape)

    def removeTarget(self, shape):
        try:
            self.__shapes.remove(shape)
            return True
        except ValueError:
            return False

    @property
    def started(self):
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
        self._duration = duration

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
        self.__start_delay = delay/1000

    @property
    def can_run_reversed(self):
        return self.__run_reversed

    @can_run_reversed.setter
    def can_run_recersed(self, can):
        self.__run_reversed = can
