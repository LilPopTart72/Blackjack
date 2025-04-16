# Imports
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic 
import sys
import random
from others import *

# GUI Class For War
class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Load The Ui File
        uic.loadUi("deck.ui", self)
        
        # Initialize Widgets
        self.initialize_widgets()
            
        # Shuffle Cards
        self.shuffle()
        
        # Click buttons
        self.shuffleButton.clicked.connect(self.shuffle)
        self.dealButton.clicked.connect(self.dealCards)
        
        # Show The App
        self.show()
        
    def initialize_widgets(self):
        
        # Initialize Labels
        widget_names = ["dealerLabel", "playerLabel", "dealerHeaderLabel", "playerHeaderLabel", 
                        "dealerHandLabel", "playerHandLabel"] + [f"cWar_{i}" for i in range(1, 7)]
        for name in widget_names:
            setattr(self, name, self.findChild(QLabel, name))
        
        # Initialize Buttons
        for button_name in ["shuffleButton", "dealButton"]:
            setattr(self, button_name, self.findChild(QPushButton, button_name))
            
    def shuffle(self):
        
        # Sets Up The Deck And Shuffle
        self.game = Game()
        
        self.setWindowTitle("The Game Of War")
        self.dealerHandLabel.setText(str(len(self.game.dealer.hand)))
        self.playerHandLabel.setText(str(len(self.game.player.hand)))
        
        for i in ["playerLabel", "dealerLabel"]:
                getattr(self,i).setPixmap(QPixmap())
                
    def dealCards(self):
        
        # Deals and Scores Both Players Cards
        try:
            # Resets War Var
            if self.game.war == True:
                self.game.war = False
            # Grab a Card For players
            dcard = self.game.dealer.hand.pop(0)
            pcard = self.game.player.hand.pop(0)
            
            # Score The Cards On Screen
            self.game.Score(pcard, dcard, [pcard, dcard])

            # Updates the widgets
            self.Update(pcard, dcard)
        
        # Someone Has Won / Lost
        except IndexError:
            self.setWindowTitle("Game Over")
        
    def Update(self, pcard, dcard):
        # Update Hand Label
            self.dealerLabel.setPixmap(QPixmap(dcard.image))
            self.playerLabel.setPixmap(QPixmap(pcard.image))
            self.dealerHeaderLabel.setText(self.game.dealersmsg)
            self.playerHeaderLabel.setText(self.game.playermsg)
            self.dealerHandLabel.setText(str(len(self.game.dealer.hand)))
            self.playerHandLabel.setText(str(len(self.game.player.hand)))
            
            if self.game.war == True:
                # Displays The Next 3 Cards For Each Player
                for i in range(3):
                    getattr(self, f"cWar_{i+1}").setPixmap(QPixmap(self.game.war_cards[i+3].image))
                    getattr(self, f"cWar_{i+4}").setPixmap(QPixmap(self.game.war_cards[i].image))
            else:
                # Clears War Cards
                for i in [self.cWar_1, self.cWar_2, self.cWar_3, self.cWar_4, self.cWar_5, self.cWar_6]:
                    i.setPixmap(QPixmap())
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()