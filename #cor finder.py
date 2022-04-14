#cor finder
import turtle

wn = turtle.Screen()
wn.title("cor finder")
wn.bgcolor("skyblue")
wn.setup(width=800, height=600)

cor = turtle.Turtle()
cor.speed(0)
cor.shape("square")
cor.color("red")
cor.shapesize(stretch_wid=1, stretch_len=1)
cor.penup()
cor.goto(0,0)

def cor_up():
    y = cor.ycor()
    y += 20
    cor.sety(y)

def cor_down():
    y = cor.ycor()
    y -= 20
    cor.sety(y)

def cor_right():
    x= cor.xcor()
    x += 20
    cor.setx(x)

def cor_left():
    x= cor.xcor()
    x -= 20
    cor.setx(x)
def cor_print():
    print("X:   Y:")
    print(cor.xcor(), cor.ycor())

wn.listen()
wn.onkeypress(cor_up, "w")
wn.onkeypress(cor_down, "s")
wn.onkeypress(cor_right, "d")
wn.onkeypress(cor_left, "a")
wn.onkeypress(cor_print, "p")

while True:
    wn.update()