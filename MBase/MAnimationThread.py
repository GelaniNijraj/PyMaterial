from PySide.QtCore import QThread

import time


class MAnimationThread(QThread):
    """
    Single animation thread to run all the animations in the
    background.
    """
    def __init__(self):
        QThread.__init__(self)
        self.__methods = []
        self.__args = []
        self.__frame = 1

    def add_method(self, method, args=None):
        """
        Adds a method to the thread's execution list. Optional list of
        arguments or a single argument can be passed as a second
        argument.
        NOTE: The supplied method should return the value False when it
        has completed its execution so it can be removed from the list.
        :param method:
        :param args:
        :return:
        """
        self.__methods.append(method)
        self.__args.append(args)

    def run(self):
        """
        Runs all the methods in the list one by one every 1/t ms
        :return:
        """
        while True:
            time.sleep(1/60)
            cleanup_indices = []
            for i, method in enumerate(self.__methods):
                return_val = method(self.__args[i])
                # try:
                #     return_val = method(*self.__args[i])
                # except TypeError:
                #     try:
                #         return_val = method(self.__args[i])
                #     except TypeError:
                #         return_val = method()
                if return_val is False:
                    cleanup_indices.append(i)

            for i in cleanup_indices:
                self.__methods.pop(i)
                self.__args.pop(i)
