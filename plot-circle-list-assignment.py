'''
Test this.
https://tritech-testsite.smapply.io/

Get the code: 10.183.1.26 code python
Plot circle data using python
x - Change the background color
x - Change the graph line colors
x - Change the plot line color
x - Change the plot dot color
x - Label the graph with text Plotting Circumference and Diameter
x - Label the axis with text (Circumference and Diameter)
x - Upload to github with your name initials or name attached (plot-circle-list-cwc.py

'''

import turtle
import math
w = turtle.Screen()
w.setup(600, 600)
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"
style = ('System', 20, 'bold')
small = ('System', 10, 'bold')

def grid(t):
	t.screen.bgpic("/home/magickalwiz/Documents/sponge.png")
	t.speed(100)
	t.width(2)
	t.pencolor('#003366')
	x = -200; y = -200
	while (x < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	
	x = -200; y = -200
	while (y < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	
	t.penup()
	t.setpos(0, 250)
	t.write('Circumference Graph', font=style, align='center')
	t.setpos(0,0)
	t.dot(6,'#003366')
	t.setpos(0,200)
	t.write('Y', font=small, align='center')
	t.setpos(208,-7)
	t.write('X', font=small, align='center')

def plotCircles(t):
	t.pencolor('#ffffff')
	t.speed(100)
	d =  [9, 5.5, 7.3, 3.75] 
	c =  [3*28.26,  3*17.27, 3*22.75, 3*11.5] 
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.penup()
	t.goto(-200,-200)
	t.pendown()
	t.dot(5, blue)
	t.penup()
	t.goto(dsorted[0],csorted[0])
	t.pendown()
	t.dot(5, blue)
	t.goto(dsorted[1],csorted[1])
	t.dot(5, blue)
	t.goto(dsorted[2],csorted[2])
	t.dot(5, blue)
	t.goto(dsorted[3],csorted[3])
	t.dot(5, blue)
	
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.hideturtle()
		grid(t)
		plotCircles(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''

'''
d =  [12.8, 1.8, 19.8, 8.7] 
c =  [3*12.8,  3*1.8, 3*19.7, 3* 8.7] 
'''
