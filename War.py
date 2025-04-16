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
        # Define Our Widgets
        for i in ["dealerLabel", "playerLabel", "dealerHeaderLabel", "playerHeaderLabel", "dealerHandLabel", "playerHandLabel"]:
            self.i = self.findChild(QLabel, i) 
        # Define The War Specific Widgets
        for i in range(1,7):
            setattr(self, f"cWar_{i}", self.findChild(QLabel, f"cWar_{i}"))

        # Define The Buttons
        for i in ["shuffleButton", "dealButton"]:
            self.i = self.findChild(QPushButton, i)
        # Shuffle Cards
        self.shuffle()
        # Click buttons
        self.shuffleButton.clicked.connect(self.shuffle)
        self.dealButton.clicked.connect(self.dealCards)
        # Show The App
        self.show()
        
    def shuffle(self):
        # Define Game Variables / Reset Them
        self.deck = [f"{y}_of_{x}" for x in ["diamonds", "clubs", "hearts", "spades"] for y in range(2, 15)]
        self.dealer = []
        self.player = []
        # Deals The Deck
        try:
            while True:
                # Grab A Random Card For Dealer
                card = random.choice(self.deck)
                # Remove That Card From The Deck
                self.deck.remove(card)
                # Add That Card To Dealers List
                self.dealer.append(card)
                # Output Card To Screen
                pixmap = QPixmap(f'images/cards/{card}.png')
                self.dealerLabel.setPixmap(pixmap)
                    
                # Grab A Random Card For Dealer
                card = random.choice(self.deck)
                # Remove That Card From The Deck
                self.deck.remove(card)
                # Add That Card To Players List
                self.player.append(card)
                # Output Card To Screen
                pixmap_2 = QPixmap(f'images/cards/{card}.png')
                self.playerLabel.setPixmap(pixmap_2)
        # After Deck is Delt Initializes Card Counts
        except:
            self.setWindowTitle("The Game Of War")
            self.dealerHandLabel.setText(str(len(self.dealer)))
            self.playerHandLabel.setText(str(len(self.player)))
    
    def dealCards(self):
        # Deals And Scores Cards
        try:
            # Sets War Specific Cards To Display None
            for i in ["cWar_1", "cWar_2", "cWar_3", "cWar_4", "cWar_5", "cWar_6"]:
                getattr(self,i).setPixmap(QPixmap())
            # Grab a Card For players
            dcard = self.dealer[0]
            pcard = self.player[0]
            # Remove losing card from losers deck
            self.dealer.remove(dcard)
            self.player.remove(pcard)
            # Output Dealer Card To Screen
            pixmap = QPixmap(f'images/cards/{dcard}.png')
            self.dealerLabel.setPixmap(pixmap)
            # Output Player Card To Screen
            pixmap_2 = QPixmap(f'images/cards/{pcard}.png')
            self.playerLabel.setPixmap(pixmap_2)
            # Score The Cards On Screen
            self.Score(pcard, dcard, [pcard, dcard])
            #Update Players Hands Label
            self.dealerHandLabel.setText(str(len(self.dealer)))
            self.playerHandLabel.setText(str(len(self.player)))
        # Someone Has Won / Lost
        except:
            self.setWindowTitle("Game Over")
            
    def Score(self, pcard, dcard, spoils):
        # Player Won So They Recieve Both Cards
        if int(pcard[:2].strip('_')) > int(dcard[:2].strip('_')):
            self.dealerHeaderLabel.setText("Dealer Loses")
            self.playerHeaderLabel.setText("Player Wins")
            self.player.extend(spoils)
        # If The Cards Are Equal We Go Into War
        elif int(pcard[:2].strip('_')) == int(dcard[:2].strip('_')):
            self.War(spoils)
        # Dealer Won So They Recieve Both Cards
        else:
            self.dealerHeaderLabel.setText("Dealer Wins")
            self.playerHeaderLabel.setText("Player Loses")
            self.dealer.extend(spoils)
    
    def War(self, previous):
        # Displays The Next 3 Cards For Each Player
        self.cWar_1.setPixmap(QPixmap(f'images/cards/{self.player[0]}.png'))
        self.cWar_2.setPixmap(QPixmap(f'images/cards/{self.player[1]}.png'))
        self.cWar_3.setPixmap(QPixmap(f'images/cards/{self.player[2]}.png'))
        self.cWar_4.setPixmap(QPixmap(f'images/cards/{self.dealer[0]}.png'))
        self.cWar_5.setPixmap(QPixmap(f'images/cards/{self.dealer[1]}.png'))
        self.cWar_6.setPixmap(QPixmap(f'images/cards/{self.dealer[2]}.png'))
        # Defining the War Variables
        spoils = self.dealer[:3] + self.player[:3] + previous
        pcard = self.player[2]
        dcard = self.dealer[2]
        # Removes The War Cards From Players Decks
        self.player = self.player[3:]
        self.dealer = self.dealer[3:]
        # Scores The Final Card Of Each Players War Specific Cards
        self.Score(pcard, dcard, spoils)
        
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()