#couldn't convert string to float with the word two

# Geometry Homework
#9/19

#kaden Marden
def intro():
    print("""
    tri=1
    pSquare=2
    aSquare=3
    circle=4
    cube=5
    quit = 6""")

def triangle():
    print("Area of Triangle")

        






def pSquare():
    print(" Perimeter of square\n")
    length = input("Length of square\n")
    heightsq = input("Height of square\n")
    perimeter_of_square = float(length)*2+float(heightsq)*2
    print(perimeter_of_square)
    square_shape = str.format("""
                 ______
                l      l
                l      l {0}
                l      l
                l______l
                       {1}
    Perimeter of this square is: {2}
    """, heightsq, length, perimeter_of_square)

    print(square_shape)

def aSquare():
    print("Area of square")
    print("Area in square feet")
    length = float(input("Length of square\n"))
    heightsq = float(input("Height of square\n"))
    area_of_square = length * heightsq
    square_shape = str.format("""
                 ______
                l      l
                l      l {0}
                l      l
                l______l
                       {1}
    Area of this square is: {2}
    """, heightsq, length, area_of_square)

    print(square_shape)

def circle():
    radius = input("Radius of circle\n")
    circumferance = 2*3.14*float(radius)
    print(circumferance)
    print("cir. of circle--")
    circ_shape= str.format("""
             , - ~ ~ ~ - ,
         , '              ' ,
       ,                     ,
      ,                       ,
     ,                         ,
     ,          ---------------,{0}
     ,                         ,
      ,                       ,
       ,                     ,
         ,                  ,  
           ' - , _  _  _  ,'
    Circumference of this circle is: {1:.2f}""", radius, circumferance)

    print(circ_shape)

def cube():
    print("volume of cube --")
    side = input("side of cube")
    volume = float(side)*float(side)*float(side)
    volume_square = str.format ("""

               _______________________                         
             /                      /l
           /                      /  l
         /                      /    l
       /                      /      l
     /______________________/        l    
    l                      l         l
    l                      l         l
    l                      l         l    
    l                      l         l
    l                      l         l
    l                      l       /
    l                      l    /
    l                      l  /
    l______________________l/
                            {0}
    Volume of this cube is: {1}
    """, side, volume)

    print(volume_square)

def menu():
    while True:
        ask=input("What do you want to find, tri, Psquare, Aspuare, circle, or cubed")
        if ask == "1":
            triangle()
        elif ask == "2":
            pSquare()
        elif ask == "3":
            aSquare()
        elif ask == "4":
            circle()
        elif ask == "5":
            cube()
        elif ask == "6":
            quit()

menu()
        else ("not valid")
