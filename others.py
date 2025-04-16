import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = f"images/cards/{rank}_of_{suit}.png"

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in ["diamonds", "clubs", "hearts", "spades"] for rank in range(2, 15)]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def add_cards(self, cards):
        self.hand.extend(cards)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player", self.deck.cards[26:])
        self.dealer = Player("Dealer", self.deck.cards[:26])
        self.playermsg = "Players Hand"
        self.dealersmsg = "Dealers Hand"
        self.war = False
        self.war_cards = []


    def Score(self, pcard, dcard, spoils):
        # Grabs The Number Value Of The Card
        pcard_value = int(pcard.rank)
        dcard_value = int(dcard.rank)
        print(dcard_value)
        print(pcard_value)
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
            winner.hand.extend(spoils)
            self.playermsg = player_text
            self.dealersmsg = dealer_text
    
    def War(self, previous):
        
        # Sets War To True
        self.war = True
        
        # Collect Spoils And Remove Cards From Decks
        self.war_cards = self.dealer.hand[:3] + self.player.hand[:3] + previous
        pcard = self.player.hand[2]
        dcard = self.dealer.hand[2]
        
        # Update Decks By Removing The War Cards
        self.player.hand = self.player.hand[3:]
        self.dealer.hand = self.dealer.hand[3:]
        
        # Score The Final War Card
        self.Score(pcard, dcard, self.war_cards)