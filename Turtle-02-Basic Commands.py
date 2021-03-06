import turtle

myScreen = turtle.Screen()
myTurtle  = turtle.Turtle()

myTurtle.forward(50)
myTurtle.left(45)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.backward(50)

myTurtle.penup()
myTurtle.right(135)
myTurtle.forward(200)
myTurtle.pendown()

myTurtle.forward(50)
myTurtle.left(90)
myTurtle.color('blue')
myTurtle.forward(50)
myTurtle.left(90)
myTurtle.color('red')
myTurtle.forward(50)
myTurtle.left(90)
myTurtle.color('green')
myTurtle.forward(50)
myTurtle.right(90)

myTurtle.penup()
myTurtle.forward(50)
myTurtle.stamp()
myTurtle.forward(50)
myTurtle.shape('turtle')
myTurtle.stamp()
myTurtle.forward(50)
myTurtle.shape('circle')
myTurtle.stamp()
myTurtle.forward(50)
myTurtle.shape('arrow')
myTurtle.stamp()
