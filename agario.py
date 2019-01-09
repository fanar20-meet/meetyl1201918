import turtle 
import time 
import random
from ball import Ball


turtle.tracer(0)
turtle.hideturtle()

RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2



MY_BALL = Ball(0,0,3,3,5,"red")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range(NUMBER_OF_BALLS) :
	# create random values for new ball - x, y, dx, dy, r, color

	x = random.randint( -SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS) 
	dx = 0 
	while dx == 0 :
		dx = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX) 
	dy = 0 
	while dy == 0 :
		dy = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
	r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS) 
	color = (random.random(), random.random(), random.random())


	new_ball = Ball (x,y,dx,dy,r,color)  #use the random values we just created(random.random(), random.random(), random.random()

BALLS.append(new_ball)




def move_all_balls()
	for ball in BALLS :
		self.move()



turtle.mainloop()



