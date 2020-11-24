#Simple Pong game in Python 3
#Original source: https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org

#Imports
import turtle
import os


#Game screen configurations
#Creating game screen
game_screen = turtle.Screen()

#Game title
game_screen.title("Pong by RafaelxFernandes")

#Game screen background color
game_screen.bgcolor("black")

#Game screen size
game_screen.setup(width = 800, height = 600)

#Stops game screen from updating
game_screen.tracer(0)

#Scores
score_a = 0
score_b = 0


#Game objects
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.x = 0.2
ball.y = 0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))


#Functions
#Paddle A
#Move paddle A up
def paddle_a_up():

    #Get Y coordinate and adds 20 pixels
    y = paddle_a.ycor()
    y += 20

    #Set new Y coordinate
    paddle_a.sety(y)

#Move paddle A down
def paddle_a_down():

    #Get Y coordinate and subtracts 20 pixels
    y = paddle_a.ycor()
    y -= 20

    #Set new Y coordinate
    paddle_a.sety(y)


#Paddle B
#Move paddle B up
def paddle_b_up():

    #Get Y coordinate and adds 20 pixels
    y = paddle_b.ycor()
    y += 20

    #Set new Y coordinate
    paddle_b.sety(y)

#Move paddle B down
def paddle_b_down():

    #Get Y coordinate and subtracts 20 pixels
    y = paddle_b.ycor()
    y -= 20

    #Set new Y coordinate
    paddle_b.sety(y)


#Keyboard binding
game_screen.listen()

#Paddle A
game_screen.onkey(paddle_a_up, "w")
game_screen.onkey(paddle_a_down, "s")

#Paddle B
game_screen.onkey(paddle_b_up, "Up")
game_screen.onkey(paddle_b_down, "Down")


#Main game loop
while True:

    #Every time the loop runs, it updates the screen
    game_screen.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)

    #Border checking
    #Top border
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.y *= -1
        os.system("aplay bounce.wav&")

    #Bottom border
    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.y *= -1
        os.system("aplay bounce.wav&")

    #Right border
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball.x *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    #Left border
    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball.x *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    #Paddle and ball collisions
    #Paddle A
    if((ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < (paddle_a.ycor() + 40) and ball.ycor() > (paddle_a.ycor() - 40)):
        ball.setx(-340)
        ball.x *= -1
        os.system("aplay bounce.wav&")

    #Paddle B
    if((ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < (paddle_b.ycor() + 40) and ball.ycor() > (paddle_b.ycor() - 40)):
        ball.setx(340)
        ball.x *= -1
        os.system("aplay bounce.wav&")    