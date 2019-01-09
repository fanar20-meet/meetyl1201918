import turtle 


high = 300
low = -300
right = 300
left = -300

turtle.hideturtle()
class Ball (turtle.Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		turtle.Turtle.__init__(self)
		self.x = x 
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)

		turtle.pu()



	def move(self):
		
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x + self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y + self.r
		self.goto(new_x,new_y)



		if self.xcor() < left or self.xcor() > right :
			self.dx = -self.dx
		
		if self.ycor() > high or self.ycor() < low :
			self.dy = -self.dy
		


# b1 = Ball(0,0,50,50,5,"red")






turtle.mainloop()