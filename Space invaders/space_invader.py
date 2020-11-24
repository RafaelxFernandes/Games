# Simple Space Invaders game made in Python 3
# Original source:
# https://www.youtube.com/watch?v=crV6T3piwHQ

# Imports
import turtle
import os
import math
import random


# Set up the screen
window = turtle.Screen()
window.title("Space invaders by RafaelxFernandes")
window.bgcolor("black")
window.setup(width=700, height=800)
window.bgpic("space_invaders_background.gif")
window.tracer(0)

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)

for side in range(4):
    border.fd(600)
    border.lt(90)

border.hideturtle()

# Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
score_string = "Score: {}".format(score)
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# Player movements
def move_left():

    x = player.xcor()
    x -= player_speed

    if(x < -280):
        x = -280

    player.setx(x)

def move_right():
    
    x = player.xcor()
    x += player_speed

    if(x > 280):
        x = 280

    player.setx(x)

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 2

# Define bullet state
# Ready to fire
bullet_state = "ready"

def fire_bullet():

    # Declare bullet_state as a global if it needs changed
    global bullet_state 

    if(bullet_state == "ready"):
        os.system("aplay laser.wav&")
        bullet_state = "fire"

        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


# Choose a number of enemies
number_enemies = 30
enemies = []

for i in range(number_enemies):
    # Create enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_index = 0
    
for enemy in enemies:
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_index)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_index += 1

    if(enemy_index == 10):
        enemy_start_y -= 50
        enemy_index = 0

enemy_speed = 0.3


# Check bullet and enemy collision
def is_collision(turtle1, turtle2):

    distance = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(), 2) + math.pow(turtle1.ycor() - turtle2.ycor(), 2))

    if(distance < 15):
        return True
    else:
        return False


# Create keyboard bindings
window.listen()
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(fire_bullet, "space")


# Main game loop
while True:

    window.update()

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move the enemy back and down
        if(enemy.xcor() > 280 or enemy.xcor() < -280):
            
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1

        # Check for a collision between the bullet and the enemy
        if(is_collision(bullet, enemy)):
            os.system("aplay explosion.wav&")

            # Reset the bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)

            # Reset the enemy
            enemy.setposition(0, 10000)

            score += 10
            score_string = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        if(is_collision(player, enemy)):
            os.system("aplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if(bullet_state == "fire"):
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check if the bullet reached the top
    if(bullet.ycor() > 275):
        bullet.hideturtle()
        bullet_state = "ready"