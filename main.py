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

    koch(order, size/3)
    turtle.right(120)
    koch(order, size/3)
    turtle.right(120)
    koch(order, size/3)
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

    mink(order, size)
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


def ice_1(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        ice_1(order - 1, size / 3)
        turtle.left(90)
        ice_1(order-1, size / 6)
        turtle.right(180)
        ice_1(order - 1, size / 6)
        turtle.left(90)
        ice_1(order - 1, size / 3)

def line_ice_1(order, size):
    turtle.clearscreen()
    turtle.speed(100)
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()

    ice_1(order, size)
    turtle.seth(0)

def ice_2(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        ice_1(order - 1, size / 3)
        turtle.left(90)
        ice_1(order-1, size / 6)
        turtle.right(180)
        ice_1(order - 1, size / 6)
        turtle.left(90)
        ice_1(order - 1, size / 3)

def line_ice_2(order, size):
    turtle.clearscreen()
    turtle.speed(100)
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()

    ice_2(order, size)
    turtle.seth(0)

line_ice_2(0, 500)
#sun_mink(2, 1000)
#line_koch(3,100)

turtle.up()
turtle.hideturtle()
turtle.home()
turtle.done()
