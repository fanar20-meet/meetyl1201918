import turtle
import random

from turtle import Turtle
from random import randint

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

class square(Turtle):
	def __init__(self, Size ,color):
		Turtle.__init__(self)
		self.shapesize(Size)
		self.color(color)
		self.shape("square")
	def random_color(self):
		random_color()
		
square1 = square(5,"red")
square1.random_color() 
turtle.mainloop()