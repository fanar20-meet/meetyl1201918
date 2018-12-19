import turtle
from turtle import *
import random 
import math

class Ball (Turtle):
	def __init__(self,radius, color,speed,dx,dy) :
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx = dx
		self.dy = dy

	def move(self):
		b1.pu()
		b2.pu()
		self.goto(self.xcor() + self.dx , self.ycor() + self.dy)


#  code to creat two ball objects here 


def check_collision(b1 , b2):
	if  math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)) >= b1.radius + b2.radius :
		print ( " There is no collision ")

	else :
		print ( " There is a collision " )


		
def reverse(b1,b2) :
 	if  math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)) < b1.radius + b2.radius :
 		return (b1.pos() * -1)



b1 = Ball( 25 , "red" , 0 ,1,1)
b2 = Ball( 20 , "blue" , 0 ,1,1)

x1 = b1.xcor()
x2 = b2.xcor()
y1 = b1.ycor()
y2 = b2.ycor()


while True:
	b1.move()
	b2.move()

check_collision(b1 , b2)


turtle.mainloop()
