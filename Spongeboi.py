import turtle
import math

w = turtle.Screen()

def main():
	w.setup(600, 600)
	w.clear()
	t = turtle.Turtle()
	t.hideturtle()
	t2 = turtle.Turtle()
	t2.hideturtle()
	t.speed(100)
	t2.speed(100)
	t.screen.bgpic("/home/magickalwiz/Documents/sponge.png")
			
	
	
	

	
	
	
	fill_body(t)
	draw(t)
	draw_leg(t)
	draw_foot(t2)
	draw_clothes(t2)
	draw_arm(t)
	draw_l_hand(t)
	draw_spat(t)
	draw_r_hand(t)
	
	draw2(t)

	

	draw_left_eye(t)
	draw_right_eye(t)
	
	draw_right_pupil2(t)
	draw_left_pupil2(t)
	draw_left_pupil1(t)
	draw_right_pupil1(t)
	
	draw_right_mouth(t)
	draw_left_mouth(t)
	draw_tooth_left(t)
	draw_tooth_right(t)
	sponge_bob_nose(t)
	eye_lashleft_1(t)
	eye_lashleft_2(t)
	eye_lashleft_3(t)
	eye_lashright_1(t)
	eye_lashright_2(t)
	eye_lashright_3(t)
	
	
	
def fill_body(t):
	t.setpos(0,0)
	t.pendown()
	t.setheading(-90)
	t.pencolor('#e4f11c')
	t.begin_fill()
	t.fillcolor('#e4f11c')
	t.forward(20)
	t.right(90)
	t.forward(125)
	t.right(90)
	t.forward(250)
	t.right(90)
	t.forward(250)
	t.right(90)
	t.forward(250)
	t.right(90)
	t.forward(125)
	t.right(180)
	t.end_fill()

	
	
	t.begin_fill()
	t.fillcolor('#e4f11c')
	t.end_fill()
	

def draw(t):
	t.setpos(0,0)
	t.penup()
	t.back(125)
	t.right(90)
	t.forward(50)
	t.left(90)
	t.pendown()
	t.pencolor('#844528')
	t.forward(250)
	t.back(50)
	

def draw_leg(t):
	t.pencolor('#e4f11c')
	t.begin_fill()
	t.fillcolor('#e4f11c')
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
	
	t.pencolor('#e4f11c')
	t.begin_fill()
	t.fillcolor('#e4f11c')
	t.left(90)
	t.forward(175)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(175)
	t.end_fill()
	
		
def draw_foot(t2):
	t2.penup()
	t2.forward(70)
	t2.right(90)
	t2.forward(225)
	t2.left(90)
	t2.width(5)
	t2.pendown()
	t2.begin_fill()
	t2.fillcolor('#000000')
	t2.forward(26)
	for x in range(180):
		t2.forward(0.15)
		t2.right(1)
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
	for x in range(180):
		t2.forward(0.15)
		t2.left(1)
	t2.forward(28)
	t2.left(90)
	t2.forward(16)
	t2.end_fill()
	t2.penup()
	
	t2.width(1)
	t2.penup()
	t2.setposition(0,-10)
	t2.right(180)
	
def draw_clothes(t2):
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

	
	

def draw_arm(t):	
	t.penup()
	t.left(90)
	t.forward(60)
	t.right(90)
	t.forward(150)
	t.left(130)
	t.begin_fill()
	t.fillcolor('#e4f11c')
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
	
def draw_l_hand(t):
	t.right(180)
	t.begin_fill()
	t.fillcolor('#e4f11c')
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
			
def draw_spat(t):
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
	
	t.pencolor('#e4f11c')
	t.begin_fill()
	t.fillcolor('#e4f11c')
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
	t.pencolor('#e4f11c')
	t.setposition(0,-20)
	t.left(15)
	
def draw_r_hand(t):
	t.right(100)
	t.forward(205)
	t.left(90)
	t.forward(30)
	t.right(90)
	
	t.pendown()
	t.begin_fill()
	t.fillcolor('#e4f11c')
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
	t.pencolor('#000000')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


def draw_left_eye(t):
  t.pendown()
  t.penup()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.setpos(-25,180)
  t.pendown()
  t.circle(15)
  t.end_fill()
  
def draw_right_eye(t):
  t.penup()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.setpos(25,180)
  t.pendown()
  t.circle(15)
  t.end_fill()
  
def draw_right_pupil2(t):
  t.penup()
  t.setpos(25,190)
  t.begin_fill()
  t.fillcolor('#00bfff')
  
  t.pendown()
  t.circle(5)
  t.end_fill() 
  
def draw_left_pupil2(t):
  t.penup()
  t.begin_fill()
  t.fillcolor('#00bfff')
  t.setpos(-25,190)
  t.pendown()
  t.circle(5)
  t.end_fill() 
  
  
def draw_left_pupil1(t):
  t.penup()
  t.begin_fill()
  t.fillcolor('#000000')
  t.setpos(-25,193)
  t.pendown()
  t.circle(3)
  t.end_fill()
  
  
def draw_right_pupil1(t):
  t.penup()
  t.begin_fill()
  t.fillcolor('#000000')
  t.setpos(25,193)
  t.pendown()
  t.circle(3)
  t.end_fill()


def draw_right_mouth(t):
  t.penup()
  t.pencolor('#000000')
  t.setpos(0,130)
  t.width(3)
  t.pendown()
  t.circle(100,25)
  t.setheading(0)
 
def draw_left_mouth(t):
  t.penup()
  t.setpos(0,130)
  t.pendown()
  t.circle(100,-25)
  t.setheading(0)

def draw_tooth_left(t):
  t.width(1)
  t.penup()
  t.setpos(-25,132)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.right(90)
  t.forward(20) 
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(18)
  t.end_fill()
  
def draw_tooth_right(t):
  t.penup()
  t.setpos(5,130)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#ffffff')
  t.right(180)
  t.forward(18) 
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(20)
  t.end_fill()
  
def sponge_bob_nose(t):
	t.penup()
	t.setpos(10,155)
	t.pendown()
	t.hideturtle()
	t.begin_fill()
	t.fillcolor('#e4f11c')
	t.right(90)
	for x in range(25):
		t.forward(2.5)
		t.right(1)
	for x in range(180):
		t.forward(0.1)
		t.right(1)
	for x in range(25):
		t.forward(2.5)
		t.left(1)
	t.end_fill()
	

def eye_lashleft_1(t):
	t.penup()	
	t.setpos(-30,205)
	t.pendown()
	t.right(90)
	t.forward(10)
	t.hideturtle()
	
	
def eye_lashleft_2(t):
	t.penup()	
	t.setpos(-40,200)
	t.pendown()
	t.left(10)
	t.forward(10)
	
	
def eye_lashleft_3(t):
	t.penup()	
	t.setpos(-15,205)
	t.pendown()
	t.right(30)
	t.forward(10)
	
	
def eye_lashright_1(t):
	t.penup()	
	t.setpos(20,205)
	t.pendown()
	t.left(15)
	t.forward(10)
		
	
def eye_lashright_2(t):
	t.penup()	
	t.setpos(30,205)
	t.pendown()
	t.right(20)
	t.forward(10)
	
	
def eye_lashright_3(t):
	t.penup()	
	t.setpos(10,200)
	t.pendown()
	t.left(36)
	t.forward(10)
	
	w.exitonclick()










def draw2(t):
	t.end_fill()
	t.up()
	
	t.color("#FFF763")
	t.fillcolor('#FFF763')
	t.width(5)
	t.goto(-125, 235)
	
	t.down()
	
	drawSinWave(t, t.position()[1], False)
	
	drawSidewaysSinWave(t, t.position()[0], False)
	
	drawSinWave(t, t.position()[1], True)
	
	drawSidewaysSinWave(t, t.position()[0], True)
	
	t.end_fill()
	t.penup()
	t.width(1)
	t.setpos(0,0)
	t.right(90)
	t.pendown()
	
	

def drawSinWave(t, y, reverse):
	if reverse == False:
		for x in range(0, 245):
			t.goto(t.position()[0] + 1, 6 * math.sin(.001 * (t.position()[0] * 150)) + y)
	else:
		for x in range(0, 245):
			t.goto(t.position()[0] - 1, 6 * math.sin(.001 * (t.position()[0] * 150) + 55) + y)

def drawSidewaysSinWave(t, x, reverse):
	if reverse == False:
		for y in range(0, 290):
			t.goto(6 * math.cos(.001 * (t.position()[1] * 150) + 25) + x, t.position()[1] - 1)
	else:
		for y in range(0, 297):
			t.goto(6 * math.cos(.001 * (t.position()[1] * 150) + 5) + x, t.position()[1] + 1)

if __name__ == '__main__':
	main()
