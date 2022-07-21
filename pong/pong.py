import turtle
import winsound

window = turtle.Screen()
window.title("Pong by Maac")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyborad binding
window.listen()
window.onkeypress(paddleA_up, "w")
window.onkeypress(paddleA_down, "s")
window.onkeypress(paddleB_up, "Up")
window.onkeypress(paddleB_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *= -1
        scoreA += 10
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *= -1
        scoreB += 10
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() < -330 and ball.xcor() > -340 and ball.ycor() < paddleA.ycor()+50 and ball.ycor() > paddleA.ycor()-50:
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() > 330 and ball.xcor() < 340 and ball.ycor() < paddleB.ycor()+50 and ball.ycor() > paddleB.ycor()-50:
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)