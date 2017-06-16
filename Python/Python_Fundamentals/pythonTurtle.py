# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
turtle.pencolor('red')
turtle.speed(1)
side_length = 200
turtle.backward(side_length/2)
turtle.left(60)
turtle.forward(side_length)
turtle.right(120)
turtle.forward(side_length)
turtle.left(60)
turtle.backward(side_length)
