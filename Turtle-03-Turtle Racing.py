import random
import turtle
import time

# BEGIN PART 1
screen = turtle.Screen()

track = turtle.Turtle()
track.hideturtle()
track.pensize(3)
track.speed(0)
track.penup()

track.goto(-250,-100)
track.pendown()
track.goto(250,-100)
track.goto(250,-50)
track.goto(-250,-50)
track.goto(-250,0)
track.goto(250,0)
track.goto(250,50)
track.goto(-250,50)
track.goto(-250,100)
track.goto(250,100)
track.goto(250,-100)
track.goto(-250,-100)
track.goto(-250,100)
track.penup()

track.goto(0,150)
track.write('Turtle Race!', font=("Arial", 14, "normal"), align='center')
# END PART 1

# BEGIN PART 2
P1 = turtle.Turtle()
P1.penup()
P1.shape('turtle')
P1.color('red')
P1.speed(0)
P1.goto(-268,75)

P2 = turtle.Turtle()
P2.penup()
P2.shape('turtle')
P2.color('blue')
P2.speed(0)
P2.goto(-268,25)

P3 = turtle.Turtle()
P3.penup()
P3.shape('turtle')
P3.color('orange')
P3.speed(0)
P3.goto(-268,-25)

P4 = turtle.Turtle()
P4.penup()
P4.shape('turtle')
P4.color('purple')
P4.speed(0)
P4.goto(-268,-75)

P1x = -268
P2x = -268
P3x = -268
P4x = -268
# END PART 2

# BEGIN PART 3 
track.goto(0,125)
track.write('Ready...         ', font=("Arial", 14, "normal"), align='center')
time.sleep(random.randint(2,5))
track.write('                GO!', font=("Arial", 14, "normal"), align='center')
# END PART 3

# BEGIN PART 4
done = 0 
while done == 0:
    P1x = P1x + random.randint(3,10)
    P2x = P2x + random.randint(3,10)
    P3x = P3x + random.randint(3,10)
    P4x = P4x + random.randint(3,10)

    P1.setx(P1x)
    P2.setx(P2x)
    P3.setx(P3x)
    P4.setx(P4x)

    if P1x >= 232 or P2x >= 232 or P3x >= 232 or P4x >= 232:
        done = 1
# END PART 4
