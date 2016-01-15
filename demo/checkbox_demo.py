__author__ = "Samvid Mistry"

import sys
from PySide.QtGui import *
from MUtilities import MColors
from MComponents.MCheckbox import MCheckBox


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Reveal test")
        self.setGeometry(100, 100, 500, 500)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_LIGHT)
        self.setPalette(p)

    def addComponents(self):
        layout = QGridLayout()
        self.checkbox = MCheckBox()
        layout.addWidget(self.checkbox)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
