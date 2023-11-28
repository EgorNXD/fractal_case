import turtle


def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)


def line_koch(order, size):
    turtle.clearscreen()
    turtle.speed(100)
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()

    koch(order, size)
    turtle.seth(0)



def sf_koch(order, size):
    turtle.clearscreen()
    turtle.speed(100)
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.up()
    turtle.goto(-400, 200)
    turtle.down()

    koch(order, size)
    turtle.right(120)
    koch(order, size)
    turtle.right(120)
    koch(order, size)
    turtle.seth(0)


def mink(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        mink(order - 1, size / 8)
        turtle.left(90)
        mink(order - 1, size / 8)
        turtle.right(90)
        mink(order - 1, size / 8)
        turtle.right(90)
        mink(order - 1, size / 8)
        mink(order - 1, size / 8)
        turtle.left(90)
        mink(order - 1, size / 8)
        turtle.left(90)
        mink(order - 1, size / 8)
        turtle.right(90)
        mink(order - 1, size / 8)


def line_mink(order, size):
    turtle.clearscreen()
    turtle.speed(100)
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()

    mink(size, order)
    turtle.seth(0)

def sun_mink(order, size):
    turtle.clearscreen()
    turtle.speed(100)
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.up()
    turtle.goto(-400, 200)
    turtle.down()

    mink(order, size)
    turtle.right(90)
    mink(order, size)
    turtle.right(90)
    mink(order, size)
    turtle.right(90)
    mink(order, size)
    turtle.seth(0)



turtle.up()
turtle.hideturtle()
turtle.home()
turtle.done()
