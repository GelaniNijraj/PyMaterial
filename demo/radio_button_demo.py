__author__ = 'MaitreyaBuddha'

import sys
from PySide.QtGui import *
from MComponents.MRadioButton import MRadioButton
from MUtilities import MColors


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyMaterial RadioButtons")
        self.setGeometry(100, 100, 300, 200)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_DARK)
        self.setPalette(p)

    def addComponents(self):
        layout = QVBoxLayout()
        layout.addWidget(MRadioButton())
        # h1 = QHBoxLayout()
        # h2 = QHBoxLayout()
        # h3 = QHBoxLayout()
        # radio = MRadioButton("plugged_in", "Only when plugged in")
        # radio.check()
        # radio.setDisabled()
        # layout.addWidget(radio)
        # layout.addWidget(MRadioButton("poop", "Poop is surely not the best"))
        # layout.addWidget(MRadioButton("pizza", "But pizzas are"))
        # btn = QPushButton("Uncheck")
        # btn.clicked.connect(radio.unset)
        # layout.addWidget(btn)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
