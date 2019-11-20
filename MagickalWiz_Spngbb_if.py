import turtle
import time
import math

def draw_animate(t,x,y,done):
	thecolor = "#e4f11c"
	for i in range(0,2):
		t.penup()
		t.goto(x,y)
		t.back(125)
		t.right(90)
		t.forward(50)
		t.left(90)
		t.pendown()
	
		t.pencolor(thecolor)
		if (done == 0):
			thecolor = "#000000"
			print("done ", done)
			time.sleep(3)
			t.screen.bgpic("img/spongebob-background.png")
			done = 1
		t.forward(250)
		t.back(50)
		

def draw(t,thecolor):
	t.penup()
	t.goto(0,0)
	t.seth(0)
	t.back(125)
	t.right(90)
	t.forward(50)
	t.left(90)
	t.pendown()
	t.pencolor('#844528')
	t.forward(250)
	t.back(50)
	

def draw_leg(t,thecolor):
	t.pencolor(thecolor)
	t.begin_fill()
	t.fillcolor(thecolor)
	t.right(90)
	t.forward(175)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(175)
	t.left(90)
	t.end_fill()
	t.pencolor('#844528')
	t.forward(130)
	
	t.pencolor(thecolor)
	t.begin_fill()
	t.fillcolor(thecolor)
	t.left(90)
	t.forward(175)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(175)
	t.end_fill()
	
		
def draw_foot(t2,thecolor):
	t2.seth(0)
	t2.penup()
	t2.setpos(0,0)
	t2.forward(70)
	t2.right(90)
	t2.forward(225)
	t2.left(90)
	t2.width(5)
	t2.pendown()
	t2.begin_fill()
	t2.fillcolor('#000000')
	t2.forward(26)
	for x in range(45):
		t2.forward(0.6)
		t2.right(4)
	t2.forward(28)
	t2.right(90)
	t2.forward(16)
	t2.end_fill()
	
	t2.penup()
	t2.left(90)
	t2.forward(135)
	t2.pendown()
	t2.begin_fill()
	t2.fillcolor('#000000')
	t2.forward(26)
	for x in range(45):
		t2.forward(0.6)
		t2.left(4)
	t2.forward(28)
	t2.left(90)
	t2.forward(16)
	t2.end_fill()
	t2.penup()
	
	t2.width(1)
	t2.penup()
	t2.setposition(0,-10)
	t2.right(180)
	
def draw_clothes(t2,thecolor):
	t2.penup()
	t2.left(90)
	t2.back(125)
	t2.pencolor('#ffffff')
	t2.begin_fill()
	t2.fillcolor('#ffffff')
	t2.pendown()
	t2.forward(250)
	t2.right(90)
	t2.forward(10)
	t2.right(90)
	for x in range(43):
		t2.forward(2)
		t2.left(1)
	
	t2.right(43)
	t2.forward(95)
	t2.right(43)
	for x in range(43):
		t2.forward(2)
		t2.left(1)
	t2.right(90)
	t2.forward(10)
	
	t2.end_fill()
	t2.penup()
	t2.pencolor('#000000')
	t2.setpos(0,-10)
	t2.right(180)
	t2.showturtle()

	


def draw_arm(t,thecolor):
	t.penup()
	t.left(90)
	t.forward(60)
	t.right(90)
	t.forward(150)
	t.left(130)
	t.begin_fill()
	t.fillcolor(thecolor)
	t.pendown()
	for x in range(45):
		t.forward(3)
		t.right(-1)

	t.forward(30)
	t.left(90)
	t.forward(5)
	t.left(90)
	for x in range(55):
		t.forward(3)
		t.right(0.7)
	t.end_fill()
	t.right(-135)
	t.forward(5)
	t.back(230)

def draw_l_hand(t,thecolor):
	t.right(180)
	t.begin_fill()
	t.fillcolor(thecolor)
	for x in range(80):
		t.forward(2.5)
		t.left(1)
	
	t.right(90)
	t.forward(5)
	t.right(90)
	
	for x in range(80):
		t.forward(2.5)
		t.right(1)
	t.end_fill()
	
	t.right(90)
	t.forward(5)
	t.right(90)
	
	for x in range(80):
		t.forward(2.5)
		t.left(1)
	t.left(90)
	t.forward(10)
	t.right(90)
	
	t.begin_fill()
	t.right(85)
	t.forward(5)
	t.left(15)
	t.forward(5)
	t.left(80)
	t.forward(10)
	t.left(70)
	t.forward(15)
	t.left(90)
	t.forward(15)
	t.left(100)
	t.forward(20)
	t.end_fill()
			
def draw_spat(t,thecolor):
	t.pencolor('#000000')
	t.fillcolor('#000000')
	t.begin_fill()
	t.forward(15)
	t.left(90)
	t.forward(8)
	t.left(90)
	t.forward(15)
	t.end_fill()
	t.penup()
	t.forward(20)
	
	t.pendown()
	t.begin_fill()
	t.forward(20)
	t.right(90)
	t.forward(5)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(18)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(5)
	t.right(90)
	t.forward(20)
	t.end_fill()
	
	t.pencolor(thecolor)
	t.begin_fill()
	t.fillcolor(thecolor)
	t.right(45)
	t.forward(20)
	t.left(45)
	t.forward(5)
	t.left(90)
	t.forward(20)
	t.end_fill()
	
	t.penup()
	t.pencolor('#ffffff')
	t.forward(5)
	t.left(90)
	t.forward(55)
	t.pendown()
	t.back(15)
	t.penup()
	t.left(90)
	t.forward(5)
	t.right(90)
	t.pendown()
	t.forward(15)
	t.penup()
	t.left(90)
	t.forward(5)
	t.right(90)
	t.pendown()
	t.back(15)
	t.penup()
	t.back(40)
	t.left(90)
	t.forward(15)
	
	t.penup()
	t.pencolor(thecolor)
	t.setposition(0,-20)
	t.left(15)
	
def draw_r_hand(t,thecolor):
	t.right(100)
	t.forward(205)
	t.left(90)
	t.forward(30)
	t.right(90)
	
	t.pendown()
	t.begin_fill()
	t.fillcolor(thecolor)
	t.left(80)
	t.forward(20)
	t.left(70)
	t.forward(10)
	t.left(40)
	t.forward(10)
	t.left(70)
	t.forward(15)
	t.left(20)
	t.forward(10)
	t.left(80)
	t.forward(15)
	t.right(165)
	t.forward(15)
	t.right(15)
	t.end_fill()
	
	t.penup()
	t.setposition(0,0)
	t.left(95)
	t.showturtle()
	
def draw_body(t,thecolor):
	t.color(thecolor)
	t.up()
	t.goto(-100, 215)
	#t.down()
	t.forward(200)
	t.right(90)
	t.forward(250)
	t.right(90)
	t.forward(200)
	t.right(90)
	t.forward(250)
	t.down()
	t.begin_fill()
	t.fillcolor(thecolor)
	drawSinWave(t, t.position()[1], False)
	drawSidewaysSinWave(t, t.position()[0], False)
	drawSinWave(t, t.position()[1], True)
	drawSidewaysSinWave(t, t.position()[0], True)
	t.end_fill()

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


def main():
	w = turtle.Screen()
	w.setup(600, 600)
	w.clear()
	t = turtle.Turtle()
	t.hideturtle()
	t2 = turtle.Turtle()
	t2.hideturtle()
	t.speed(100)
	t2.speed(100)
	t.screen.bgpic("img/spongebob-background.png")
	
	done = 0
	x = 0;y = 0
	
	#draw_animate(t,x,y,done)
	
	while (done < 4):
		if (done == 0):
			thecolor = "#FFF763"
		elif (done == 1):
			thecolor = "#FFFF00"
		elif (done == 2):
			thecolor = "#FF7F00"
		else:
			thecolor = "#00FF00"
		draw(t,thecolor)
		draw_leg(t,thecolor)
		draw_foot(t2,thecolor)
		draw_clothes(t2,thecolor)
		draw_arm(t,thecolor)
		draw_l_hand(t,thecolor)
		draw_spat(t,thecolor)
		draw_r_hand(t,thecolor)
		draw_body(t,thecolor)
		done = done + 1
		print(done)
		
	w.exitonclick()

	
if __name__ == '__main__':
	main()
