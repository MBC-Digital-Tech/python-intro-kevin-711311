from turtle import *

def draw_square(length):
    for counter in range(4):
        forward(length)
        right(90)
    
def square():
    length = int(input("What do you want your side length to be? "))
    draw_square(length)
    done()

def draw_triangle(length):
    for counter in range(3):
        forward(length)
        right(120)

def triangle():
    length = int(input("What do you want your side length to be? "))
    draw_triangle(length)
    done()

def draw_polygon(sides, length):
    angle = 360 / sides
    for counter in range(sides):
        forward(length)
        right(angle)

def polygon():
    sides = int(input("How many sides does your polygon have? "))
    length = int(input("What do you want your side lengths to be? "))
    draw_polygon(sides, length)
    done()

drawing = input("What do you want to draw? (square/triangle/polygon) ").strip().lower()
if drawing == "square":
    square()
elif drawing == "triangle":
    triangle()
elif drawing == "polygon":
    polygon()
else:
    print("This input is not on the drawing list!")