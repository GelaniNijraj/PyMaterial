import sys
from PySide.QtGui import *
from MComponents.MRadioButton import MRadioButton
from MUtilities import MColors
from MAnimations import MAnimator

__author__ = 'MaitreyaBuddha'


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyMaterial RadioButtons")
        self.setGeometry(100, 100, 300, 200)
        p = self.palette()
        p.setColor(self.backgroundRole(), MColors.BACKGROUND_DARK)
        self.setPalette(p)

    def addComponents(self):
        layout = QGridLayout()
        radio1 = MRadioButton()
        radio2 = MRadioButton()
        radio3 = MRadioButton()
        radio4 = MRadioButton()
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(radio3)
        layout.addWidget(radio4)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.addComponents()
    app.exec_()
    sys.exit()
