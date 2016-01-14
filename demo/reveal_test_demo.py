__author__ = "Samvid Mistry"

import sys
from PySide.QtGui import *
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
        test1 = MTestComponent()
        layout.addWidget(test1)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
