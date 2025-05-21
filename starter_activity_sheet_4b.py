# week 4 Loops

from turtle import *
import webbrowser

def square():
    for counter in range(4):
        forward(100)
        right(90)

#square()
#left(45)
#square()
    done()

def triangle():
    color('brown')
    begin_fill()
    
    for counter in range(3):
        forward(80)
        right(120)

    end_fill()

    done()

def pentagon():
    color('grey', 'black')
    begin_fill()

    for counter in range(5):
        right(72)
        forward(200)

    end_fill()

    done()

def hexagon():
    color('orange', 'red')
    begin_fill()

    for counter in range(6):
        right(60)
        forward(70)

    end_fill()

    done()

def envelope():
    for counter in range(2):
        right(90)
        forward(120)
        right(90)
        forward(198)

    right(90)

    right(45)
    forward(140)
    right(90)
    forward(140)
    right(135)

    done()

drawing = input("What do you want to draw? (square/triangle/pentagon/hexagon/envelope) ").strip().lower()
if drawing == "square":
    square()
elif drawing == "triangle":
    triangle()
elif drawing == "pentagon":
    pentagon()
elif drawing == "hexagon":
    hexagon()
elif drawing == "envelope":
    envelope()
else:
    print("This input is not on the drawing list!")