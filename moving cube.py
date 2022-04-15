import turtle

wn = turtle.Screen()
wn.title("moving cube yt")
wn.bgcolor("skyblue")
wn.setup(width=800, height=600)

cube = turtle.Turtle()
cube.speed(0)
cube.shape("square")
cube.color("red")
cube.shapesize(stretch_len=5, stretch_wid=5)
cube.penup()
cube.goto(0, 0)


def cube_up():
    y = cube.ycor()
    y += 20
    cube.sety(y)

def cube_down():
    y = cube.ycor()
    y -= 20
    cube.sety(y)

def cube_right():
    x = cube.xcor()
    x += 20
    cube.setx(x)

def cube_left():
    x = cube.xcor()
    x -= 20
    cube.setx(x)

wn.listen()
wn.onkeypress(cube_up, "w")
wn.onkeypress(cube_down, "s")
wn.onkeypress(cube_right, "d")
wn.onkeypress(cube_left, "a")

while True:
    wn.update()