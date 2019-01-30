import turtle 
import time 
import random
import math 
from ball import *


turtle.tracer(2)
turtle.hideturtle()
gameover =  turtle.clone()
gameover.pu()
gameover.hideturtle()
gameover.goto(50,50)

RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2


# creating the Balls

MY_BALL = Ball(0,0,3,3,50,"red")

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

# move all balls
def move_all_balls():
	for ball in BALLS :
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)






# check for ball collisions 

def colide(ball_a,ball_b):
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()


	if ball_a == ball_b :
		return False

	if  math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)) + 10 <= ball_a.r + ball_b.r :
		print ( " There is a collision ")
		return True
	else :
		print ( " There is no collision " )
		return False

		




# check collisions for all balls

def check_all_balls_collisions():
	for ball_a in BALLS :
		for ball_b in BALLS:
			

			if colide(ball_a,ball_b):
				relocating(ball_a,ball_b)
				# ball_a.r += ball_b.r 
				# r1 = ball_a.r 
				# r2 = ball_b.r





#  relocating the smaller ball

def relocating(ball_1 , ball_2) :

	while r > 100 :
		return False

	X_coordinate = random.randint( -SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	Y_coordinate = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	X_axis_speed = 0 
	while X_axis_speed == 0 :
			X_axis_speed = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX)  
	Y_axis_speed = 0
	while Y_axis_speed == 0 :	
			Y_axis_speed = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX) 
	Raduis = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS) 
	Color = (random.random(), random.random(), random.random())


	if ball_2.r > ball_1.r :

		ball_1.goto(X_coordinate,Y_coordinate)
		ball_1.dx = X_axis_speed 
		ball_1.dy = Y_axis_speed
		ball_1.r = Raduis
		ball_1.color(Color)
		ball_1.shapesize(ball_1.r/10)

		ball_2.shapesize(ball_2.r/10)

		ball_2.r += 5
	else:
		ball_2.goto(X_coordinate,Y_coordinate)
		ball_2.dx = X_axis_speed 
		ball_2.dy = Y_axis_speed
		ball_2.r = Raduis
		ball_2.color(Color)
		ball_2.shapesize(ball_2.r/10)

		ball_1.shapesize(ball_1.r/10)

		ball_1.r += 5








def check_myball_collision():
	for new_ball in BALLS :
			
		if colide(MY_BALL,new_ball):
			print("collision")

			if MY_BALL.r <= new_ball.r :
				return False
			else:
				X_coordinate = random.randint( -SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				Y_coordinate = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				X_axis_speed = 0 
				while X_axis_speed == 0 :
						X_axis_speed = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX)  
				Y_axis_speed = 0
				while Y_axis_speed == 0 :	
						Y_axis_speed = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX) 
				Radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS) 
				Color = (random.random(), random.random(), random.random())

				new_ball.r = Radius
				new_ball.shapesize(new_ball.r/10)
				new_ball.goto(X_coordinate,Y_coordinate)
				new_ball.dx = X_axis_speed 
				new_ball.dy = Y_axis_speed
				new_ball.color(Color)

				MY_BALL.r += 5
				MY_BALL.shapesize(MY_BALL.r/10)

	return True




def movearound(event):

	X_coordinate = event.x - SCREEN_WIDTH
	Y_coordinate = SCREEN_HEIGHT - event.y
	MY_BALL.goto(X_coordinate, Y_coordinate)
	while MY_BALL.r > 100 :
		return False



turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



while RUNNING:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2
	move_all_balls()
	check_all_balls_collisions()
	RUNNING = check_myball_collision()
	turtle.update()
	time.sleep(SLEEP)

if RUNNING == False :
	gameover.write("GAME OVER :0 " , True , font= ("Spenser", 30 , "bold"))

time.sleep(3)

