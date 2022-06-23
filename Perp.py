
import turtle

from soupsieve import select


class Person():
    def __init__(self) -> None:
        self = turtle.Turtle()
        self.shape("square")
        self.color("red")
        self.goto(250, 250)

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


perp = Person()
sc = turtle.Screen()
sc.title("One character")
sc.bgcolor("white")
sc.setup(width=500, height=500)


# Keyboard bindings
# TODO: hmm may need to make these global scope?
sc.listen()
sc.onkeypress(moveup, "w")
sc.onkeypress(movedown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
sc.onkeypress(close, "q")
