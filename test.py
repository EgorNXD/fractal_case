import turtle
turtle.clearscreen()
turtle.speed(100)
turtle.pencolor("black")
turtle.pensize(2)
order = 2
size = 300
turtle.up()
turtle.goto(-400, 0)
turtle.down()

'''первый'''
def squares(order, size):
    if order == 0:
        return None
    else:
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.forward(size * 0.05)
        turtle.right(10)
        squares(order - 1, size - 5)


def main_squares(order, size):
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.tracer(0, 1)
    turtle.pencolor("black")
    turtle.up()
    turtle.goto(-400, -100)
    turtle.down()

    squares(order, size)
    turtle.seth(0)



'''второй'''
# import turtle
#
# def color_tree(order, size):
#     turtle.colormode(255)
#     cg = 255 - int(order * (250/6)) % 255
#     turtle.color(0, cg, 0)
#     if order == 0:
#         turtle.forward(size)
#     else:
#         turtle.forward(size)
#         turtle.right(45)
#         color_tree(order - 1, size / 2)
#         turtle.left(90)
#         color_tree(order - 1, size / 2)
#         turtle.right(45)
#         turtle.backward(size)



'''трейтий'''
# from turtle import *
# def branch(order, size):
#     if order == 0:
#         left(180)
#         return
#
#     x = size/(order+1)
#     for i in range(order):
#         turtle.forward(x)
#         turtle.left(45)
#         branch(order-i-1, 0.5*x*(order-i-1))
#         turtle.left(90)
#         branch(order-i-1, 0.5*x*(order-i-1))
#         turtle.right(135)
#
#     turtle.forward(x)
#     turtle.left(180)
#     turtle.forward(size)
#     turtle.up()
#     turtle.goto(0,-100)
#     turtle.left(90)
#     turtle.down()
#     branch(5,400)

#turtle.left(90)
#color_tree(5, 200)
# branch(5, 200)
squares(5, 200)
main_squares(5, 200)
