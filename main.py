import turtle


window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(800, 600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Player Movement Functions

def A_move_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def A_move_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def B_move_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def B_move_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Ball movement functions

def ball_move():
    ball.setx(ball.xcor() + ball.dx)
    ball.setx(ball.ycor() + ball.dy)


# Main game loop
running = True

while running:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    window.listen()


    turtle.onkeypress(A_move_up, "w")
    turtle.onkeypress(A_move_down, "s")
    turtle.onkeypress(B_move_up, "o")
    turtle.onkeypress(B_move_down, "l")

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if paddle_b.ycor() > 240:
        paddle_b.goto(350, 240)

    if paddle_b.ycor() < -240:
        paddle_b.goto(350, -240)

    if paddle_a.ycor() > 240:
        paddle_a.goto(-350, 240)

    if paddle_a.ycor() < -240:
        paddle_a.goto(-350, -240)

    # Paddle Working (Collisions)

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1

    if (ball.xcor() < - 340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1




