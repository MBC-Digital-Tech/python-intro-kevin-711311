from turtle import *

## Task 1: Look at the following code and decide which picture it will generate.
# Then download it from the shared drive, then save and run it, to check.

def demo():
  pencolor("red")
  for counter in range (20):
    forward (150)
    right(100)
  done()

def hexagon():
  pencolor("blue")
  for counter in range(6):
    forward(100)
    right(60)

  done()

def sharp_circle():
  pencolor("blue")
  for counter in range(75):
    forward(200)
    right(95)

  done()

def flower():
  for counter in range(6):
    circle(50,120)
    left(60)
    circle(50,120)

  done()

def coloured_flower():
  for counter in range(3):
    fillcolor('purple')
    begin_fill()
    circle(50,120)
    left(60)
    circle(50,120)
    end_fill()

    fillcolor('blue')
    begin_fill()
    circle(50,120)
    left(60)
    circle(50,120)
    end_fill()
  
  done()

def triangle():
  for counter in range(3):
    forward(80)
    right(120)
  
  # had to remove done() for the triangle hexagon function to work

def triangle_hexagon():
  for counter in range(8):
     triangle()
     right(45)
    
  done()

drawing = input("What do you want to draw? (demo/hexagon/sharp circle/flower/coloured flower/triangle/triangle hexagon) ").strip().lower()
if drawing == "demo":
    demo()
elif drawing == "hexagon":
    hexagon()
elif drawing == "sharp circle":
    sharp_circle()
elif drawing == "flower":
    flower()
elif drawing == "coloured flower":
    coloured_flower()
elif drawing == "triangle":
    triangle()
elif drawing == "triangle hexagon":
    triangle_hexagon()
else:
    print("This input is not on the drawing list!")