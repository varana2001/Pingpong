import turtle as t

playerA = 0
playerB = 0

window = t.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

left_paddle = t.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=1, stretch_len=4)
left_paddle.penup()
left_paddle.goto(-350, 0)
left_paddle.speed(0)

right_paddle = t.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=1, stretch_len=4)
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle.speed(0)

ball = t.Turtle()
ball.color("green")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.4
ballydirection = 0.4

pen = t.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ballydirection *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerA, playerB), align="center", font=("Arial", 24, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerA, playerB), align="center", font=("Arial", 24, "normal"))

    if (340 > ball.xcor() > 330) and (right_paddle.ycor() + 40 > ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(330)
        ballxdirection *= -1

    if (-340 < ball.xcor() < -330) and (left_paddle.ycor() + 40 > ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-330)
        ballxdirection *= -1
