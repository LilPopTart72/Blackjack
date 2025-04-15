from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic 
import sys
import random

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

        # Shuffle Cards
        self.shuffle()
        
        # Click buttons
        self.shufflebutton.clicked.connect(self.shuffle)
        self.dealbutton.clicked.connect(self.dealCards)
        
        # Show The App
        self.show()
        
    def shuffle(self):
        global deck
        deck = [f"{y}_of_{x}" for x in ["diamonds", "clubs", "hearts", "spades"] for y in range(2, 15)]
        
        # Create Our Player
        global dealer, player
        dealer = []
        player = []
        
        # Grab a Random Card For Dealer
        card = random.choice(deck)
        # Remove That card From The Deck
        deck.remove(card)
        # Add That Card To Dealers Liist
        dealer.append(card)
        # Output Card To Screen
        pixmap = QPixmap(f'images/cards/{card}.png')
        self.Dealerlabel.setPixmap(pixmap)
            
        # Grab a Random Card For Dealer
        card = random.choice(deck)
        # Remove That card From The Deck
        deck.remove(card)
        # Add That Card To Dealers Liist
        player.append(card)
        # Output Card To Screen
        pixmap_2 = QPixmap(f'images/cards/{card}.png')
        self.Playerlabel.setPixmap(pixmap_2)
            
        self.setWindowTitle(str(len(deck)))
    
    def dealCards(self):
        try:
            # Grab a Random Card For Dealer
            card = random.choice(deck)
            # Remove That card From The Deck
            deck.remove(card)
            # Add That Card To Dealers Liist
            dealer.append(card)
            # Output Card To Screen
            pixmap = QPixmap(f'images/cards/{card}.png')
            self.Dealerlabel.setPixmap(pixmap)
            
            # Grab a Random Card For Dealer
            card = random.choice(deck)
            # Remove That card From The Deck
            deck.remove(card)
            # Add That Card To Dealers Liist
            player.append(card)
            # Output Card To Screen
            pixmap_2 = QPixmap(f'images/cards/{card}.png')
            self.Playerlabel.setPixmap(pixmap_2)
            
            self.setWindowTitle(str(len(deck)))
        except:
            self.setWindowTitle("Game Over")
    
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()