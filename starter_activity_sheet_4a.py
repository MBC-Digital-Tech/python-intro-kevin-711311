# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python

def square(): #will use loops in the next module, for now just following the instructions
    color('black', 'gray')
    begin_fill()
    forward (300) 
    right (90)
    forward (300) 
    right (90) 
    forward (300)
    right (90) 
    forward (300)
    right (90)
    end_fill()

    done()

def triangle():
    color('purple', 'blue')
    begin_fill()
    
    for counter in range(3):
        right(120)
        forward(200)

    end_fill()
    
    done()

def triangle_and_square():
    color('purple', 'blue')
    begin_fill()
    
    for counter in range(3):
        right(120)
        forward(200)

    end_fill()

    penup()
    forward(50)
    pendown()

    color('black', 'gray')
    begin_fill()
    forward (300) 
    right (90)
    forward (300) 
    right (90) 
    forward (300)
    right (90) 
    forward (300)
    right (90)
    end_fill()

    done()

def earth():
    color('green', 'yellow')
    begin_fill()
    circle(100)
    end_fill()
    
    left(90)
    penup()
    forward(25)
    right(90)
    pendown()
    
    color('orange')
    begin_fill()
    circle(75)
    end_fill()

    left(90)
    penup()
    forward(50)
    right(90)
    pendown()

    color('red')
    begin_fill()
    circle(25)
    end_fill()

    done()

def triangle_hexagon():
    
    for i in range(6):
        forward(200)
        right(120)
        forward(200)
        right(120)
        forward(200)
        right(120)
        right(60)

    done()

drawing = input("What do you want to draw? (square/triangle/triangle and square/earth/triangle hexagon) ").strip().lower()
if drawing == "square":
    square()
elif drawing == "triangle":
    triangle()
elif drawing == "triangle and square":
    triangle_and_square()
elif drawing == "earth":
    earth()
elif drawing == "triangle hexagon":
    triangle_hexagon()
else:
    print("This input is not on the drawing list!")