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
def draw_circle_rec(radius, depth):
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
        draw_circle_rec(radius / 2, depth - 1)
        turtle.penup()
        turtle.backward(radius * 2)
        turtle.pendown()
        draw_circle_rec(radius / 2, depth - 1)
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
def alternate_color(depth):
    print("current depth: ", depth)
    if depth % 2 == 0:
        turtle.pencolor("#0000b3")
    else:
        turtle.pencolor("#ff4dff")


'''
Draws the circles but with alternating colors.
'''
def draw_circles_alternating(radius, depth):
    if depth==0:
        pass
    else:
        alternate_color(depth)
        turtle.circle(radius)
        turtle.penup()
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius/2)
        turtle.right(90)
        turtle.pendown()
        alternate_color(depth)
        draw_circles_alternating(radius / 2, depth - 1)
        alternate_color(depth)
        turtle.penup()
        turtle.backward(radius * 2)
        turtle.pendown()
        alternate_color(depth)
        draw_circles_alternating(radius / 2, depth - 1)
        alternate_color(depth)
        turtle.penup()
        turtle.right(90)
        turtle.forward(radius/2)
        turtle.left(90)
        turtle.forward(radius)
        turtle.pendown()


'''
Main function.
'''
def main():
    turtle.speed(0)
    # draw_circle_1(100)
    # draw_circle_2(100)
    # draw_circle_rec(100, 5)
    # draw_circles_alternating(100, 5)
    turtle.done()

main()