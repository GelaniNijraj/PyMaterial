from PySide.QtGui import *

import sys

from MBase import *

# Setting up stuff
animation_thread = MAnimationThread()
value_animator = MValueAnimator(0, 100, 10000, 60)


class Demo:
    def __init__(self, va):
        self.frame = 1
        self.va = va

    def run_on_thread(self):
        try:
            print("Frame", self.frame, self.va.step())
            self.frame += 1
        except MFinalValueReachedException:
            print('Final value reached')
            return False

demo1 = Demo(value_animator)
demo2 = Demo(value_animator)

# Adding two methods to the animation thread list
animation_thread.add_method(demo1.run_on_thread)
animation_thread.add_method(demo2.run_on_thread)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    animation_thread.run()
    app.exec_()
    sys.exit()
