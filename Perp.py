# testing some basic game stuff with turtle

import turtle


# interactable player
class Player():
    def __init__(self):
        self.user = turtle.Turtle()
        self.user.speed(0)
        self.user.shape("classic")
        self.user.color("red")
        self.user.penup()
        self.user.goto(0, 0)


# vertical walls
class verticalwall():
    def __init__(self) -> None:
        self.wall = turtle.Turtle()
        self.wall.penup()
        self.wall.shape("square")
        self.wall.shapesize(stretch_wid=6, stretch_len=2)


# horizontal walls
class horizontalwall():
    def __init__(self) -> None:
        self.wall = turtle.Turtle()
        self.wall.penup()
        self.wall.shape("square")
        self.wall.shapesize(stretch_wid=2, stretch_len=6)


perp = Player()


def moveup():
    y = perp.user.ycor()
    y += 10
    perp.user.sety(y)


def movedown():
    y = perp.user.ycor()
    y -= 10
    perp.user.sety(y)


def moveleft():
    x = perp.user.xcor()
    x -= 10
    perp.user.setx(x)


def moveright():
    x = perp.user.xcor()
    x += 10
    perp.user.setx(x)


# close window with a button press
def close():
    sc.bye()
    sc.mainloop()

# make a new screen with basic stuff


def newscreen():
    sc = turtle.Screen()
    sc.title("One character")
    sc.bgcolor("white")
    sc.setup(width=500, height=500)


# prints location of user in top-right corner
def location():
    view.undo()
    view.setpos(160, 220)
    view.write("{}".format(perp.user.pos()))


sc = turtle.Screen()
sc.title("One character")
sc.bgcolor("white")
sc.setup(width=500, height=500)

view = turtle.Turtle()
view.speed(0)
view.color("red")
view.penup()
view.hideturtle()
view.setposition(170, 200)

goal = turtle.Turtle()
goal.color("green")
view.penup()
view.goto(200, -80)
view.setposition(200, -80)

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
sc.onkeypress(location, "f")
sc.onkeypress(close, "q")

vertical1 = verticalwall()
vertical1.wall.setposition(-200, 200)
vertical2 = verticalwall()
vertical2.wall.setposition(200, -200)
horizontal1 = horizontalwall()
horizontal1.wall.setposition(-160, 150)
horizontal2 = horizontalwall()
horizontal2.wall.setposition(160, -150)

# basic event loop for game
while True:
    sc.update()

    # hit border then go to opposite side
    if perp.user.xcor() > 250:
        perp.user.setx(-250)
    if perp.user.xcor() < -250:
        perp.user.setx(250)
    if perp.user.ycor() > 250:
        perp.user.sety(-250)
    if perp.user.ycor() < -250:
        perp.user.sety(250)

    # TODO: goal hit causes crash
    if perp.user.xcor() == 200 and perp.user.ycor() == -80:
        view.setposition(125, 125)
        view.write("GOAL REACHED")
