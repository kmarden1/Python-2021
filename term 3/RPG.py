import random



WARRIOR ="""             ,dM
                        dMMP
                       dMMM'
                       \MM/
                       dMMm.
                      dMMP'_\---.
                     _| _  p ;88;`.
                   ,db; p >  ;8P|  `.
                  (``T8b,__,'dP |   |
                  |   `Y8b..dP  ;_  |
                  |    |`T88P_ /  `\;
                  :_.-~|d8P'`Y/    /
                   \_   TP    ;   7`\\
        ,,__        >   `._  /'  /   `\_
        `._   ---~~~~------|`\\ '
           ~~~-----~~~'\__[|;' _.-'  `\\
                   ;--..._     .-'-._     ;
                  /      /`~~"'   ,'`\_ ,/
                 ;_    /'        /    ,/
                 | `~-l         ;    /
                 `\    ;       /\.._|
                   \    \      \     \\
                   /`---';      `----'
                  (     /
                   `---'
"""


HUNTER:"""
            I_-_ '
            I(")_____.
           <\. ,----~
           :/_(
           ( ,)
            uU
            lL
"""


MAGE:"""
                  .'* *.'
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \
           / _ \ - | - /_  \
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._
 _.-'       |      BBb       '-.  '-.
(________mrf\____.dBBBb.________)____)
"""


class Hero(object):
    playerRace = ["Alienboy", "Chuckycheese", "African Warlord", "Chinese King", "Native American",
                  "Plain old joe"]
    classList = ["Warrior", "Hunter", "Henchman",]

    def __init__(self):
        self.alive = True
        self.level = 1
        self.xp = 0
        self.name = input("What is your Name")
        self.xp = 0
        self.levelup = 90 + (self.level * 100)
        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.healAct = self.maxHealth
        self.defe = 10
        self.atk = 10
        self.luck = random.randint(1, 10)
        self.stamina = random.randint(1, 10)
        self.ig = random.randint(1, 10)
        self.race = random.choice(Hero.playerRace)
        print(Hero.playerRace)
        y = input("What Race would you like to be?")
        if y in Hero.playerRace:
            self.playerRace = y
        else:
            ("please try again")

        print(Hero.classList)
        x = input("Choose your Class.")
        if x in Hero.classList:
            self.classList = x
        else:
            self.classList = random.choice(Hero.classlist)
            self.playerClass
            self.inventory = []
            self.inventoryMax = 10
            self.head = []
            self.chest = []
            self.legs = []
            self.boots = []
            self.gloves = []

    def __pRaces__(self):
        if self.playerRace == "Alienboy":
            print("Wack")
        elif self.playerRace == "Chuckycheese":
            print("weird flex")
        elif self.playerRace == "African Warlord":
            print("ok,ok")
        elif self.playerRace == "Chinese King":
            print("wow")
        elif self.playerRace == "Native American":
            print("Best one")
        elif self.playerRace == "Plain old joe":
            print("I mean ok")
        return self.playerRace

    def setMods(self):
        if self.classList == "Warrior":
            self.healthMod += 3
            self.iq += 50
            self.defe += 15
            self.atk += 8
            print(WARRIOR)
        elif self.classList == "Hunter":
            self.healthMod += 2.5
            self.iq += 75
            self.defe += 5
            self.atk += 4
            print(HUNTER)
        elif self.classList == "Henchman":
            self.healthMod += 100
            self.iq += 40
            self.defe += 20
            self.atk += 10
        elif self.classList == "Fake Mage":
            print("You're no hero")
            print(MAGE)
        elif self.classList == "Kid":
            self.healthMod += 50
            self.iq += 1
            self.defe += 5
            self.atk += 10
        return self.classList

    def __str__(self):
        self.rep =("Name:" + self.name + "Class:" + self.classList + "Race:" + self.playerRace)
        return self.rep

    def pickRace(self):
        while True:
            try:
                print(Hero.playerRace)
                x = input("Pick your Race")
                if x in Hero.playerRace:
                    return x
            except:
                print("Please choose a race KID")

    def enterName(self):
        while self.name == "":
            x = input("what would you like to name this Character?")
            return x

    #def die(self,Winner):
        #self.isalive = False
        #dropXp = 10 * self.level
        #winner.givexp(dropXp)

    def levelUp(self):
        if self.xp >= self.levelUp():
            self.level += 1
            remainingxp = self.xp - self.levelUp
            self.xp = remainingxp
            self.levelUp = 90 + (self.levelUp * 10)
            self.healthMod += self.level
            self.maxHealth = self.level * self.healthMod
            self.healAct = self.maxHealth


    def levelUp(self):
        pass


    def addXp(self):
        pass

# def popInv(self):
#     x = random.randint(0, 3)
#     for i in range(x):
#         return x
#
#
# def equipGloves(self):
#     if len(self.gloveseq) < 1
#         for i in self.inventory:
#             x = type(i)
#             if "Gloves" in str(x):
#                 print("You've equiped it")
#                 print(i)
#                 self.gloveseq.append(i)
#                 self.inventory.remove(i)
#







# def addToInv(self,item):
#     if len(self.inventory) < 10
#         self.inventory.append(item)
#     else:
#         print("you may have to many items in Inventory")
#         return





# class Gloves (Armor):
#     WEAPONS = ["Gun","Sword","staff","Stinky Gun"]
#     def __init__(self):
#         super(Weapon, self).__init__("Weapons")
#         self.weaponType = wType
#         self.damage = 0
#         self.stamina = 0
#         self.agi = 0
#         self.iq = 0
#         self.luck = 0
#
#   def __str__(self):
#       return """
#       weaponType: {}
#       Rarity Level: {}
#       Damage: {}
#       Luck: {}
#       stamina: {}
#       IQ: {}
#       Agility: {}
#       """.format(self.weaponType, self.rarityLevel;, self.damage, self.luck, self.stamina, self.iq, self.agi)




hero1 = Hero()
print(hero1)



