import turtle as tu

a = tu.Turtle()
a.penup()
a.goto(0, -150)
a.pendown()
a.left(90)
a.speed(0)


def drawn(l):
    if l < 5:
        return
    else:
        a.forward(l)
        a.left(30)
        drawn(4*l/5)
        a.right(60)
        drawn(4*l/5)
        a.left(30)
        a.backward(l)

drawn(100)