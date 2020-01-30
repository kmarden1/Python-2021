#coin flip


import random
def heads():
    print(
    """
                        HEADS
                     _.-'~~`~~'-._
                 .'`  B   E   R  `'.
                / I               T \
              /`       .-'~"-.       `\
             ; L      / `-    \      Y ;
            ;        />  `.  -.|        ;
            |       /_     '-.__)       |
            |        |-  _.' \ |        |
            ;        `~~;     \\        ;
             ;  INGODWE /      \\)P    ;
              \  TRUST '.___.-'`"     /
               `\                   /`
                 '._   1 9 9 7   _.'
                     `'-..,,,..-'`
                        """)

def tails():
    print(
    """
                        TAILS
                    _.-'~~`~~'-._
                 .'`  B   E   R  `'.
                / I               T \
              /`       .-'~"-.       `\
             ; L      / `-    \      Y ;
            ;        />  `.  -.|        ;
            |       /_     '-.__)       |
            |        |-  _.' \ |        |
            ;        `~~;     \\        ;
             ;  INGODWE /      \\)P    ;
              \  TRUST '.___.-'`"     / 
               `\                   /`
                 '._   1 9 9 7   _.'
                     `'-..,,,..-'`
                     """)

for i in range(0,50):
    num = random.randint(1,2)
    print(num)
    if num == 1:
        heads()

    elif num == 2:
             tails()

     
        
    
 
    
