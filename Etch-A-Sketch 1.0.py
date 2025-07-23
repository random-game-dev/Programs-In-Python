import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Etch-a-Sketch")
screen.bgcolor("white")

# Create the turtle (pen)
etchy = turtle.Turtle()
etchy.speed(0)
etchy.pensize(3)

# Movement functions
def go_up():
    etchy.setheading(90)
    etchy.forward(10)

def go_down():
    etchy.setheading(270)
    etchy.forward(10)

def go_left():
    etchy.setheading(180)
    etchy.forward(10)

def go_right():
    etchy.setheading(0)
    etchy.forward(10)

def clear_screen():
    etchy.clear()
    etchy.penup()
    etchy.home()
    etchy.pendown()

# Key bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(clear_screen, "space")

# Keep the window open
screen.mainloop()