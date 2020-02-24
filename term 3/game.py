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

