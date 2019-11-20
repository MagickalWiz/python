import turtle

def main():
	w = turtle.Screen()
	w.setup(600, 600)
	w.clear()
	w.bgcolor("#ff7f00")
	t = turtle.Turtle()
	t.speed(10)
			
	draw(t)
	draw_leg(t)
	draw_arm(t)
	
	w.exitonclick()

def draw(t):
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
	
		
def draw_arm(t):	
	t.penup()
	t.left(90)
	t.forward(60)
	t.right(90)
	t.forward(200)
	t.left(130)
	
	t.pendown()
	t.forward(30)
	t.left(20)
	t.forward(30)	
	
	
if __name__ == '__main__':
	main()
