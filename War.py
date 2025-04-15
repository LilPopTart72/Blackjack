from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic 
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the ui file
        uic.loadUi("deck.ui", self)
        self.setWindowTitle("The Game Of War")
        
        # define our widgets
        self.Dealerlabel = self.findChild(QLabel, "label")
        self.Playerlabel = self.findChild(QLabel, "label_2")
        self.DealerHeaderlabel = self.findChild(QLabel, "label_4")
        self.PlayerHeaderlabel = self.findChild(QLabel, "label_3")
        self.DealerHandlabel = self.findChild(QLabel, "label_5")
        self.PlayerHandlabel = self.findChild(QLabel, "label_6")

        self.shufflebutton = self.findChild(QPushButton, "pushButton")
        self.dealbutton = self.findChild(QPushButton, "pushButton_2")

        # Click buttons
        self.shufflebutton.clicked.connect(self.shuffle)
        self.dealbutton.clicked.connect(self.dealCards)
        
        # Show The App
        self.show()
        
        
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()