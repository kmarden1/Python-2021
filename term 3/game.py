def ask_yes_no(question):
    response = None
    while responce not in ("y", "n"):
        response = input(question).lower()
    return response
def ask_number(question, low ,high):
    response = None
    while response not in range(low, high)
        try:
            response = int(input(question))
        except:
            print("not a good number")
        return response

def get_name(question):
    name = ""
    while name == "":
        try:
            name = input(question)
        except:
            print("something went wrong")
        return name

class Player(object):
    """Player for a game"""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def card1():
    """Displays the card that was chosen"""
    card_p1()
    print("""
      You are a magician in King Arthur's court.
      You are in the fields just outside of Camelot when a
      black, snarling, cross-eyed, vicious-looking dragon roars overhead.""")
    print("""
      1. Beckon the dragon to partake in your afternoon tea party.
      2. Pull out your 9mm crossbow and clip his wings.
      """)
    card1Choice = input("Enter your choice: ")
    return card1Choice


def adventure():
    """determines what card you go to after card you chose"""
    while True:
        choice1 = card1()
        # card1 to card2
        if choice1 == "1":
            while True:
                choice2 = card2()
                # card2 to card4
                if choice2 == "1":
                    while True:
                        choice3 = card4()
                        # card4 to card8
                        if choice3 == "1":
                            while True:
                                choice4 = card8()
                                #card8 to end
                                if choice4.lower() == "y":
                                    adventure()
                                elif choice4.lower() == "n":
                                    quit()
                                else:
                                    print("That is not a valid choice.")
                                    continue

def intro():
    """Determines whether you start playing or not"""
    print("Welcome to King Arthur's Realm.")
    print("Ready to go on an adventure? [y/n]")
    start = input(": ")
    while True:
        if start.lower() == "n":
            print("Well, too bad. You're playing anyway.")
            adventure()
        if start.lower() == "y":
            print("Great! Let's get started.")
            adventure()
        else:
            print("That is not a valid choice.")
            intro()

intro()