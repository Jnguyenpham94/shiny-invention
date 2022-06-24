
import turtle

from soupsieve import select


class Person():
    def __init__(self) -> None:
        self = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(0, 0)


def moveup(self):
    y = self.ycor()
    y += 20
    self.sety(y)


def movedown(self):
    y = self.ycor()
    y -= 20
    self.sety(y)


def moveleft(self):
    x = self.xcor()
    x -= 20
    self.setx(x)


def moveright(self):
    x = self.xcor()
    x += 20
    self.setx(x)


# close window with a button press
def close():
    sc.bye()
    sc.mainloop()

def newscreen():
    sc = turtle.Screen()
    sc.title("One character")
    sc.bgcolor("white")
    sc.setup(width=500, height=500)

perp = Person()
sc = turtle.Screen()
sc.title("One character")
sc.bgcolor("white")
sc.setup(width=500, height=500)


# Keyboard bindings
sc.listen()
sc.onkeypress(moveup, "w")
sc.onkeypress(movedown, "s")
sc.onkeypress(moveleft, "a")
sc.onkeypress(moveright, "d")
sc.onkeypress(moveup, "Up")
sc.onkeypress(movedown, "Down")
sc.onkeypress(moveleft, "Left")
sc.onkeypress(moveright, "Right")
sc.onkeypress(close, "q")

while True:
    sc.update()
    