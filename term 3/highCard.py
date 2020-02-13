import BlackJack

def get_name():
    name = ""
    while name == "":
        name = input("Enter your name:")
    return name


total_players = int(input("how many players are playing"))
names = []
hands = []
for i in range(total_players):
    x = get_name()
    hand = BlackJack.Hand()
    hands.append(hand)
    names.append(x)
deck = BlackJack.Deck()
deck.populate()
deck.shuffle()
deck.deal(hands,1)

for hand in hands:
    print(hand)