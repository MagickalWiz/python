import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(1000)

#bottom
draw_circle(tommy, "#000000", 50, 25, 0)
draw_circle(tommy, "#d9d9d9", 50, 0, 0)
draw_circle(tommy, "#cccccc", 50, -25, 0)
draw_circle(tommy, "#bfbfbf", 50, -50, 0)

#left
draw_circle(tommy, "#b3b3b3", 50, -50, 25)
draw_circle(tommy, "#a6a6a6", 50, -50, 50)
draw_circle(tommy, "#999999", 50, -50, 75)
draw_circle(tommy, "#8c8c8c", 50, -50, 100)

#top
draw_circle(tommy, "#808080", 50, -25, 100)
draw_circle(tommy, "#737373", 50, -0, 100)
draw_circle(tommy, "#666666", 50, 25, 100)
draw_circle(tommy, "#595959", 50, 50, 100)

#right
draw_circle(tommy, "#4d4d4d", 50, 50, 75)
draw_circle(tommy, "#404040", 50, 50, 50)
draw_circle(tommy, "#262626", 50, 50, 25)
draw_circle(tommy, "#ffffff", 50, 50, 0)
