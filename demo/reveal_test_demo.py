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
        self.test1 = MTestComponent()
        cancel = QPushButton("Cancel Animation")
        cancel.clicked.connect(self.cancel_animation)
        layout.addWidget(self.test1)
        layout.addWidget(cancel)
        self.setLayout(layout)

    def cancel_animation(self):
        self.test1.trigger_cancel()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
