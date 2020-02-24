import BlackJack

class Highcard(BlackJack.Deck):
    def __init__(self, rank, suit, value):
        super(highcard, self).__init__(rank, suit)
        self.value = value
    @property
    def value(self):
        if self.is_face_up:
            v = Highcard.RANKS.index(self.rank)+1
            if v == 1:
                v += 13
            else:
                v = None
            return v

class HighCardDeck(BlackJack.Card):
    def populate(self):
        for suit in Highcard.SUITS:
            for rank in Highcard.RANKS:
                self.cards.append(Highcard(rank,suit))

class HighCardHand(BlackJack.Hand):
    def __init__(self,name):
        super(Highcard, self).__init__()
        self.name = name
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.card:
            t += card.value
            return t
    def win(self):
        print(self.name)
        print("congrats "+self.name+" you won!")

    def loose(self):
        print(self.name)
        print("looser")

def get_name():
    name = ""
    while name == "":
        name = input("enter your name:")
    return name

total_players = int(input("How many players are player"))
hand = []
for i in range(total_players):
    x = get_name()
    hand = HighCardHand(x)
    hands.append(hand)

deck = HighCardDeck()
deck.populate()
deck.shuffle()
deck.deal(hands,1)

highcard = 0
for player in hands:
    print(player)
    if player.total > highcard:
        highcard = player.total
for player in hands:
    if player.total >= Highcard:
        player.win()
    else:
        player.lose()






