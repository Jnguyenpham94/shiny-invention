
import turtle
from numpy import vectorize

from soupsieve import select


class Player():
    def __init__(self) -> None:
        self.user = turtle.Turtle()
        self.user.speed(0)
        self.user.shape("square")
        self.user.color("red")
        self.user.penup()
        self.user.goto(0, 0)


perp = Player()


def moveup():
    y = perp.user.ycor()
    y += 20
    perp.user.sety(y)


def movedown():
    y = perp.user.ycor()
    y -= 20
    perp.user.sety(y)


def moveleft():
    x = perp.user.xcor()
    x -= 20
    perp.user.setx(x)


def moveright():
    x = perp.user.xcor()
    x += 20
    perp.user.setx(x)


# close window with a button press
def close():
    sc.bye()
    sc.mainloop()


def newscreen():
    sc = turtle.Screen()
    sc.title("One character")
    sc.bgcolor("white")
    sc.setup(width=500, height=500)


sc = turtle.Screen()
sc.title("One character")
sc.bgcolor("white")
sc.setup(width=500, height=500)

view = turtle.Turtle()
view.speed(0)
view.color("red")
view.penup()
view.hideturtle()
view.goto(200, 200)

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
    xloc = perp.user.xcor()
    yloc = perp.user.ycor()

    # TODO: FIND WAY TO NEATLY UPDATE LOCATION
    view.write("{}, {}".format(xloc, yloc))

    # hit border then...
    if perp.user.xcor() > 250:
        perp.user.setx(-250)
    if perp.user.xcor() < -250:
        perp.user.setx(250)
    if perp.user.ycor() > 250:
        perp.user.sety(-250)
    if perp.user.ycor() < -250:
        perp.user.sety(250)
