from PySide.QtCore import QThread

import time


class MAnimationThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.__methods = []
        self.__args = []

    def add_method(self, method, args):
        self.__methods.append(method)
        self.__args.append(args)

    def run(self):
        while True:
            time.sleep(1/60)
            for i, method in enumerate(self.__methods):
                method(self.__args[i])