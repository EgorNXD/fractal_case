import turtle

def squares(order, size):
    if order == 0:
        return
    else:
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.forward(size * 0.05)
        turtle.right(10)
        squares(order - 1, size * 0.8)


def main_squares(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-400, -100)
    turtle.down()

    squares(order, size)


def color_tree(order, size):
    turtle.colormode(255)
    cg = 255 - int(order * (250/6)) % 255
    turtle.color(0, cg, 0)
    if order == 0:
        turtle.forward(size)
    else:
        turtle.forward(size)
        turtle.right(45)
        color_tree(order - 1, size / 2)
        turtle.left(90)
        color_tree(order - 1, size / 2)
        turtle.right(45)
        turtle.backward(size)

def branch(order, size):
    if order == 0:
       turtle.left(180)
       return

    x = size/(order+1)
    for i in range(order):
        turtle.forward(x)
        turtle.left(45)
        branch(order-i-1, 0.5*x*(order-i-1))
        turtle.left(90)
        branch(order-i-1, 0.5*x*(order-i-1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


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
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-400, -100)
    turtle.down()

    koch(order, size)


def sf_koch(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-200, 200)
    turtle.down()

    koch(order, size/3)
    turtle.right(120)
    koch(order, size/3)
    turtle.right(120)
    koch(order, size/3)


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
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    mink(order, size)


def sun_mink(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0,1)
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
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    ice_1(order, size)


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
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    ice_2(order, size)


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
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()

    levi(order, size)


def hex(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        hex(order - 1, size / 3)
        turtle.left(120)
        hex(order-1, size / 3)
        turtle.right(60)
        hex(order - 1, size / 3)
        turtle.right(60)
        hex(order - 1, size / 3)
        turtle.right(60)
        hex(order - 1, size / 3)
        turtle.right(60)
        hex(order - 1, size / 3)
        turtle.left(120)
        hex(order - 1, size / 3)


def morehex(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0,1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-100, 200)
    turtle.down()

    hex(order, size)
    turtle.right(60)
    hex(order, size)
    turtle.right(60)
    hex(order, size)
    turtle.right(60)
    hex(order, size)
    turtle.right(60)
    hex(order, size)
    turtle.right(60)
    hex(order, size)



fractals = ['Квадраты', 'Двоичное дерево', 'Ветка', 'Кривая Коха', 'Снежинка коха', 'Кривая Миновского','Снежинка Миновского',
            'Ледяной 1', 'Ледяной 2', 'Кривая Леви', 'Шестиугольник']
for i in range(len(fractals)):
    print(i+1, fractals[i])
ans = int(input("Выберете фрактал:"))
order = int((input("Введите глубину рекурсии:")))
size = int(input("Введите размер:"))
if ans == 1:
    main_squares(order, size)
elif ans == 2:
    turtle.left(90)
    color_tree(order, size)
elif ans == 3:
    turtle.up()
    turtle.goto(0, -100)
    turtle.left(90)
    turtle.down()
    branch(order, size)
elif ans == 4:
    line_koch(order, size)
elif ans == 5:
    sf_koch(order, size)
elif ans == 6:
    line_mink(order, size)
elif ans == 7:
    sun_mink(order, size)
elif ans == 8:
    line_ice_1(order, size)
elif ans == 9:
    line_ice_2(order, size)
elif ans == 10:
    line_levi(order, size)
elif ans == 11:
    morehex(order, size)

turtle.up()
turtle.home()
turtle.done()
turtle.seth(0)