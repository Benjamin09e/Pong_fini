import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Bengy")
wn.bgcolor("black")
wn.setup(width=700, height=500)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-300, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(300, 0)


#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
#ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("skyblue")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 5
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 5
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 5
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 5
    paddle_b.sety(y)






# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "q")
wn.onkeypress(paddle_a_down, "z")

wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "m")




# Main game loop
while True:
    wn.update()



    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 240 :
        ball.sety(240)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -230 :
        ball.sety(-230)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -340:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))


    # paddle and ball Collision

    if (ball.xcor() > 280 and ball.xcor() < 290) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(280)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -280 and ball.xcor() > -290) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-280)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # AI paddle
    if paddle_b.ycor() < ball.ycor():
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor():
        paddle_b_down()

    if paddle_a.ycor() < ball.ycor():
        paddle_a_up()

    elif paddle_a.ycor() > ball.ycor():
        paddle_a_down()

