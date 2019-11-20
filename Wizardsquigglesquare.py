import turtle
import math

def main():
	w = turtle.Screen()
	w.setup(600, 600)
	w.clear()
	w.bgcolor("#ff7f00")
	
	t = turtle.Turtle()
	t.speed(100)
	t.hideturtle()
	draw(t)

def draw_body(t):
	t.color("#FFF763")
	t.up()
	t.goto(-150, 200)
	#t.down()
	t.forward(200)
	t.right(90)
	t.forward(250)
	t.right(90)
	t.forward(200)
	t.right(90)
	t.forward(250)
	t.down()
	drawSinWave(t, t.position()[1], False)
	drawSidewaysSinWave(t, t.position()[0], False)
	drawSinWave(t, t.position()[1], True)
	drawSidewaysSinWave(t, t.position()[0], True)

def drawSinWave(t, y, reverse):
	if reverse == False:
		for x in range(0, 200):
			t.goto(t.position()[0] + 1, 6 * math.sin(.001 * (t.position()[0] * 150)) + y)
	else:
		for x in range(0, 200):
			t.goto(t.position()[0] - 1, 6 * math.sin(.001 * (t.position()[0] * 150) + 55) + y)

def drawSidewaysSinWave(t, x, reverse):
	if reverse == False:
		for y in range(0, 230):
			t.goto(6 * math.cos(.001 * (t.position()[1] * 150) + 20) + x, t.position()[1] - 1)
	else:
		for y in range(0, 225):
			t.goto(6 * math.cos(.001 * (t.position()[1] * 150)) + x, t.position()[1] + 1)

if __name__ == '__main__':
	main()
