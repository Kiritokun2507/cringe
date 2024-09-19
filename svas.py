import turtle

pen = turtle.Turtle()
pen.speed(999999)

def svaston():
    pen.forward(100)
    pen.right(90)
    pen.forward(50)

def svastonBasic():
    for i in range(4):
        svaston()
        pen.up()
        pen.setposition(0,0)
        pen.down()

while True:
    svastonBasic()
    pen.left(10)
    pen.clear()

input()