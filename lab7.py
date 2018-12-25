import turtle
from turtle import *
import random 
import math
turtle.colormode(255)


high = 300
low = -300
right = 300
left = -300

class Ball (Turtle):
	def __init__(self,radius, color,speed,dx,dy,) :
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx = dx
		self.dy = dy

	def move(self):
		self.pu()

		self.goto(self.xcor() + self.dx , self.ycor() + self.dy)

		if self.xcor() < left or self.xcor() > right :
			self.dx = -self.dx
		
		if self.ycor() > high or self.ycor() < low :
			self.dy = -self.dy
		

	def random_color(self):
		r=random.randint(0,255)
		b=random.randint(0,255) 
		g=random.randint(0,255)
		self.color(r,b,g)

	
#  code to creat two ball objects here 


def check_collision(b1 , b2):

	x1 = b1.xcor()
	x2 = b2.xcor()
	y1 = b1.ycor()
	y2 = b2.ycor()


	if  math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)) >= b1.radius + b2.radius :
		print ( " There is no collision ")
		return False
	else :
		print ( " There is a collision " )
		return True


b1 = Ball( 25 , "red" , 0 ,1,1,)
b2 = Ball( 20 , "blue" , 0 ,2,2,)

while True:
	b1.move()
	b2.move()

	collide = check_collision(b1 , b2)
	if collide  == True :
		b1.random_color()
		b2.random_color()

turtle.mainloop()





