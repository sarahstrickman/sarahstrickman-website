import turtle
import math


'''
Draw a circle at depth 1
pre: turtle is facing east, pendown
post: turtle is in same location, facing east, pendown
'''
def draw_circle_1(radius):
    turtle.circle(radius)


'''
Draw circles at depth 2
pre: turtle is facing east, pendown
post: turtle is in same location, facing east, pendown
'''
def draw_circle_2(radius):
    turtle.circle(radius)
    turtle.penup()
    turtle.forward(radius)
    turtle.left(90)
    turtle.forward(radius/2)
    turtle.right(90)
    turtle.pendown()
    draw_circle_1(radius/2)
    turtle.penup()
    turtle.backward(radius * 2)
    turtle.pendown()
    draw_circle_1(radius/2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(radius/2)
    turtle.left(90)
    turtle.forward(radius)
    turtle.pendown()

'''
Draw circles recursively.
Pre: turtle is facing east, at bottom of circle
post: turtle is facing east, pen down
'''
def draw_circles(radius, depth):
    change_color(depth)
    if depth==0:
        pass
    else:
        turtle.circle(radius)
        turtle.penup()
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius/2)
        turtle.right(90)
        turtle.pendown()
        change_color(depth)
        draw_circles(radius / 2, depth - 1)
        change_color(depth)
        turtle.penup()
        turtle.backward(radius * 2)
        turtle.pendown()
        change_color(depth)
        draw_circles(radius / 2, depth - 1)
        change_color(depth)
        turtle.penup()
        turtle.right(90)
        turtle.forward(radius/2)
        turtle.left(90)
        turtle.forward(radius)
        turtle.pendown()


'''
Changes color based on depth of the circles.
Even depth is blue, odd depth is pink
'''
def change_color(depth):
    if depth % 2 == 0:
        turtle.pencolor("#0000b3")
    else:
        turtle.pencolor("#ff4dff")


'''
Main function.
'''
def main():
    turtle.speed(0)
    draw_circles(100, 5)
    turtle.done()

main()