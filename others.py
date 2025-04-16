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
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_cards(self, cards):
        self.hand.extend(cards)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def play_round(self):
        player_card = self.player.hand.pop(0)
        dealer_card = self.dealer.hand.pop(0)
        winner = self.determine_winner(player_card, dealer_card)
        self.handle_winner(winner, player_card, dealer_card)

    def determine_winner(self, player_card, dealer_card):
        if player_card.rank > dealer_card.rank:
            return "Player"
        elif player_card.rank < dealer_card.rank:
            return "Dealer"
        else:
            return "War"