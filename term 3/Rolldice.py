import random

def die1():
    print("""  -----
              |     |
              |  o  |
              |     |
               ----- """)

def die2():
    print("""-----
             |o  |
             |   |
             |  o|
             ----- """)

def die3():
    print("""-----
             |o  |
             | o |
             |  o|
             -----""")

def die4():
    print("""-----
             |o o|
             |   |
             |o o|
             -----""")

def die5():
    print("""-----
             |o o|
             | o |
             |o o|
             -----""")

def die6():
    print("""-----
             |o o|
             |o o|
             |o o|
             -----""")

for i in range(0,1):
    roll = random.randint(1,6)
    print(roll)
    if roll == 1:
        die1()
    elif roll == 2:
        die2()
    elif roll == 3:
        die3()
    elif roll == 4:
        die4()
    elif roll == 5:
        die5()
    elif roll == 6:
        die6()

