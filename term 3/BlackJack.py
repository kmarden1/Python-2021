class Card(object):
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    SUITS = ("♤", "♡", "♢", "♧")

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = str.format("""
         ----------
        | {0}        |
        | {1}        |
        |          |
        |         {1}|
        |         {0}|
         ----------
        """, self.rank, self.suit)


        else:
            rep = """  ----------
| xxxxxxxxxx |
| xxxxxxxxxx |
| xxxxxxxxxx |
| xxxxxxxxxx |
| xxxxxxxxxx |
  ----------   """
        return rep

    def flip(self):
            self.is_face_up = not self.is_face_up



class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = " "
            for card in self.cards:
                rep += str(card)+ " "
        else:
            rep = "Empty Handed"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, other_hand, card):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """A deck of playing strings. this class has the following methods
    def populate."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(hand, top_card)
                else:
                    print("Out of Cards, Brother!")

