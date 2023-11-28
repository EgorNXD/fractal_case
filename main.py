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
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-400, -100)
    turtle.down()

    koch(order, size)
    turtle.seth(0)



def sf_koch(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-200, 200)
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
        mink(order - 1, size / 4)
        turtle.left(90)
        mink(order - 1, size / 4)
        turtle.right(90)
        mink(order - 1, size / 4)
        turtle.right(90)
        mink(order - 1, size / 4)
        mink(order - 1, size / 4)
        turtle.left(90)
        mink(order - 1, size / 4)
        turtle.left(90)
        mink(order - 1, size / 4)
        turtle.right(90)
        mink(order - 1, size / 4)


def line_mink(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    mink(order, size)
    turtle.seth(0)

def sun_mink(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, 300)
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
        ice_1(order - 1, size / 2)
        turtle.left(90)
        ice_1(order-1, size / 4)
        turtle.right(180)
        ice_1(order - 1, size / 4)
        turtle.left(90)
        ice_1(order - 1, size / 2)

def line_ice_1(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    ice_1(order, size)
    turtle.seth(0)

def ice_2(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        ice_2(order - 1, size / 2)
        turtle.left(120)
        ice_2(order-1, size / 4)
        turtle.right(180)
        ice_2(order - 1, size / 4)
        turtle.left(120)
        ice_2(order - 1, size / 4)
        turtle.right(180)
        ice_2(order - 1, size / 4)
        turtle.left(120)
        ice_2(order - 1, size / 2)

def line_ice_2(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    ice_2(order, size)
    turtle.seth(0)

def levi(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        levi(order - 1, ((size**2) / 2)**(1/2))
        turtle.right(90)
        levi(order - 1, ((size**2) / 2)**(1/2))
        turtle.left(45)

def line_levi(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    levi(order, size)
    turtle.seth(0)

#line_ice_2(2, 800)
line_koch(7,1000)
#sun_mink(2, 1000)
#line_koch(3,100)

turtle.up()
turtle.home()
turtle.done()
