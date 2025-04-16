# Imports
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic 
import sys
import random

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
        self.deck = [f"{y}_of_{x}" for x in ["diamonds", "clubs", "hearts", "spades"] for y in range(2, 15)]
        random.shuffle(self.deck) 
        
        # Deals Half To Dealer Half To Player
        self.dealer, self.player = self.deck[:26], self.deck[26:] 
        
        self.setWindowTitle("The Game Of War")
        self.dealerHandLabel.setText(str(len(self.dealer)))
        self.playerHandLabel.setText(str(len(self.player)))
        
        for i in ["playerLabel", "dealerLabel"]:
                getattr(self,i).setPixmap(QPixmap())
                
    def dealCards(self):
        
        # Clears War Cards
        for i in [self.cWar_1, self.cWar_2, self.cWar_3, self.cWar_4, self.cWar_5, self.cWar_6]:
            i.setPixmap(QPixmap())
        
        # Deals and Scores Both Players Cards
        try:
            
            # Grab a Card For players
            dcard = self.dealer.pop(0)
            pcard = self.player.pop(0)
            
            # Displays Cards
            self.dealerLabel.setPixmap(QPixmap(f'images/cards/{dcard}.png'))
            self.playerLabel.setPixmap(QPixmap(f'images/cards/{pcard}.png'))
            
            # Score The Cards On Screen
            self.Score(pcard, dcard, [pcard, dcard])
            
            # Update Hand Label
            self.dealerHandLabel.setText(str(len(self.dealer)))
            self.playerHandLabel.setText(str(len(self.player)))
        
        # Someone Has Won / Lost
        except IndexError:
            self.setWindowTitle("Game Over")
            
    def Score(self, pcard, dcard, spoils):
        # Grabs The Number Value Of The Card
        pcard_value = int(pcard[:2].strip('_'))
        dcard_value = int(dcard[:2].strip('_'))

        # Returns Who Won
        result = "Player Wins" if pcard_value > dcard_value else "Dealer Wins" if pcard_value < dcard_value else "War"
        
        # Updates Score Or Proceeds To War
        if result == "War":
            self.War(spoils)
        else:
            self.update_score(result, spoils)

    def update_score(self, result, spoils):
        
        # Initializes A Dictionary For Possible Win / Lose Scenarios
        actions = {
            "Player Wins": ("Dealer Loses", "Player Wins", self.player),
            "Dealer Wins": ("Dealer Wins", "Player Loses", self.dealer),
        }
        
        # Gives The Winner Both Cards
        dealer_text, player_text, winner = actions.get(result, (None, None, None))
        if dealer_text and player_text:
            self.dealerHeaderLabel.setText(dealer_text)
            self.playerHeaderLabel.setText(player_text)
            winner.extend(spoils)
    
    def War(self, previous):
        
        # Displays The Next 3 Cards For Each Player
        for i in range(3):
            getattr(self, f"cWar_{i+1}").setPixmap(QPixmap(f'images/cards/{self.player[i]}.png'))
            getattr(self, f"cWar_{i+4}").setPixmap(QPixmap(f'images/cards/{self.dealer[i]}.png'))
        
        # Collect Spoils And Remove Cards From Decks
        spoils = self.dealer[:3] + self.player[:3] + previous
        pcard = self.player[2]
        dcard = self.dealer[2]
        
        # Update Decks By Removing The War Cards
        self.player = self.player[3:]
        self.dealer = self.dealer[3:]
        
        # Score The Final War Card
        self.Score(pcard, dcard, spoils)
        
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()