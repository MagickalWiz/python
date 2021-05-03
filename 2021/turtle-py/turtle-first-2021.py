import turtle
import random

def drawRect(t,x,y,count):
	endNum = random.randint(0,25)
	t.goto(0,0)
	t.pendown()
	t.forward(x)
	t.right(90)
	t.forward(y)
	t.right(90)
	t.forward(x)
	t.right(90)
	t.forward(y)
	print(str(endNum) + '  -  ' + str(count))
	if(count != endNum):
		t.right(random.randint(10,90))
		x = x + random.randint(1,10)
		y = y + random.randint(1,5)
		randCol(t)
		drawRect(t,x,y,count = random.randint(0,25))
	else:
		print("DONE")

def randCol(t):
	randcolor = "#" + "%06x" % random.randint(0, 0xFFFFFF)
	t.color(randcolor)

def theFunction(t,x,y):
	t.pendown()
	count = 0
	drawRect(t,x,y, count)
	
def main():
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	t.speed(0)
	t.hideturtle()
	t.width(4)
	t.color('#bec2cb')
	x = 20;y = 10
	theFunction(t,x,y)
	twin.exitonclick()

if __name__ == '__main__':
	main()