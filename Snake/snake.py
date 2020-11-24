#Simple Snake game made in Python 3
#Original source: 
#https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ&ab_channel=TokyoEdTech

#Imports
import turtle
import time
import random


#Set up the screen
window = turtle.Screen()
window.title("Snake game by RafaelxFernandes")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #Turns off the screen updates

#Screen delay
delay = 0.1


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High score: 0", align="center", font=("Courier", 24, "normal"))

#Scores
score = 0
high_score = 0


#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "right"

#Snake additional body parts
segments = []


#Apples
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)


#Functions
#Go up
def go_up():
    if(head.direction != "down"):
        head.direction = "up"

#Go down
def go_down():
    if(head.direction != "up"):
        head.direction = "down"

#Go right
def go_right():
    if(head.direction != "left"):
        head.direction = "right"

#Go left
def go_left():
    if(head.direction != "right"):
        head.direction = "left"

#Move head
def move():
    
    if(head.direction == "up"):
        y = head.ycor()
        head.sety(y + 20)

    if(head.direction == "down"):
        y = head.ycor()
        head.sety(y - 20)
    
    if(head.direction == "right"):
        x = head.xcor()
        head.setx(x + 20)

    if(head.direction == "left"):
        x = head.xcor()
        head.setx(x - 20)


#Keyboard bindings
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")


#Main game loop
while True:

    window.update()

    #Check collisions with the borders
    if(head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
        
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "right"
        
        #Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        #Clear segment list
        segments = []


        #Reset the delay
        delay = 0.1

        #Reset score
        score = 0
        pen.clear()
        pen.write("Score: {}    High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    #Check if the snake ate the apple
    if(head.distance(apple) < 20):

        #Move the apple to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)

        #Add a segment to snake's body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lime")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase score
        score += 1

        #Check high score
        if(score > high_score):
            high_score = score

        pen.clear()
        pen.write("Score: {}    High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Move the segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):

        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #Move segments[0] to where the head is
    if(len(segments) > 0):

        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    #Move head
    move()

    #Check for collisions with snake's body
    for segment in segments:

        if(segment.distance(head) < 20):

            time.sleep(1)
            head.goto(0, 0)
            head.direction = "right"

            #Hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            #Clear segment list
            segments = []

            #Reset score
            score = 0
            pen.clear()
            pen.write("Score: {}    High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            #Reset the delay
            delay = 0.1

    #Adds delay to screen update
    time.sleep(delay)


#Turtle main loop
turtle.mainloop()