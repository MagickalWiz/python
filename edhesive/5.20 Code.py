import turtle
import math
import random
x = 0

def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        turtle.screensize(canvwidth=100, canvheight=100, bg=None)
        w = turtle.Screen()
        t = turtle.Turtle()
        circles(t)
        w.exitonclick()
    finally:
        turtle.Terminator()
    
def circles(t):
	t.circle(10)
	t.left(90)
	t.circle(10)
	t.left(90)
	t.circle(10)
	t.left(90)
	t.circle(10)
	t.back(20)
	t.right(90)
	t.circle(20)
	t.right(90)
	for x in range(3):
		t.forward(50)
		t.left(120)
	for x in range(3):
		t.forward(50)
		t.right(120)


if __name__ == '__main__':
    main()
