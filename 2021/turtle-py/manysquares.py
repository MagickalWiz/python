# recursion
import turtle


def square(t,d):
	t.pendown()
	t.begin_fill()
	for i in  range (0,4):
		t.fd(d)
		t.rt(90)
	t.end_fill()
	t.penup()
    

def main():
	#turtle.tracer(0,0)
	twin = turtle.Screen()
	t = turtle.Turtle()
	#twin.clear()
	count = 0
	for x in range (-400,401,25):
		for y in range (-400,401,25):
			t.penup()
			t.goto(x,y)
			thecolor = "#000000"
			if (count == 5):
				thecolor = "#0000ff"
			if(count > 7 and count < 15):
				thecolor = "#ff0000"
			t.color(thecolor)
			square(t,20)
			count = count + 1
			time.sleep(0.2)
			print(count)

	#turtle.update()
	twin.exitonclick()

if __name__=="__main__":
	main()

