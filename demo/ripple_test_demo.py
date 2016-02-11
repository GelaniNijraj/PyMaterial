__author__ = "Samvid Mistry"

import sys
from PySide.QtGui import *
from PySide.QtCore import *
from MUtilities import MColors
from MComponents.MTestComponent import MTestComponent


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Reveal test")
        self.setGeometry(100, 100, 500, 500)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_DARK)
        self.setPalette(p)

    def addComponents(self):
        layout = QGridLayout()
        self.test1 = MTestComponent()
        # self.test1.animate().fade(100).scale(50).start()
        cancel = QPushButton("Start Animation")
        cancel.clicked.connect(self.start_animation)
        layout.addWidget(self.test1)
        layout.addWidget(cancel)
        self.setLayout(layout)

    def start_animation(self):
        self.test1.animate().duration(5000).reveal("show").start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
