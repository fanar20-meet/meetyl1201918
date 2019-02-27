import turtle 
import time 
import random
import math 
from ball import *


screen = turtle.Screen()
screen.setup(2000,1300)
screen.bgpic("bg.gif")
# time.sleep(2)
# screen.bgpic('image2.gif')

answer = screen.textinput("Welcome dear vampire!", "Are you ready to eat ?")

if answer is None or answer.lower().startswith('n'):
    print("Goodbye!")
    screen.clear()
    screen.bye()
else:
    print("Start!")



turtle.tracer(0,0)
turtle.hideturtle()
turtle.register_shape("Caleb.gif")
turtle.register_shape("trash.gif")
turtle.register_shape("hopi.gif")
turtle.register_shape("sad.gif")
turtle.register_shape("ah1.gif")
turtle.register_shape("aj.gif")
turtle.register_shape("avi.gif")

gameover =  turtle.clone()
gameover.pu()
gameover.hideturtle()
gameover.goto(50,50)

RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2


score = 0
turtle.pu()
turtle.color("white")
turtle.goto(0,400)
turtle.goto(0,400)    

t_score = 0
tr_score = turtle.clone()
tr_score.pu()
tr_score.color("white")
tr_score.goto(0,-400)
tr_score.goto(0,-400)

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
viru = []
humens = ["avi.gif" ,"Caleb.gif" , "hopi.gif", "sad.gif" , "ah1.gif" , "aj.gif"]



for i in range(NUMBER_OF_BALLS) :


	x = random.randint( -SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS) 
	dx = 0 
	while dx == 0 :
		dx = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX) 
	dy = 0 
	while dy == 0 :
		dy = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )

	# r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS) 
	
	r = 30
	color = (random.random(), random.random(), random.random())

	new_ball = Ball (x,y,dx,dy,r,color)

	
	new_ball.shape(random.choice(humens))


	BALLS.append(new_ball)


# creating virus
for i in range(NUMBER_OF_BALLS):

	x = random.randint( -SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS) 
	dx = 0 
	while dx == 0 :
		dx = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX) 
	dy = 0 
	while dy == 0 :
		dy = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )

	r = 30
	color = (random.random(), random.random(), random.random())

	virus = Ball(x,y,dx,dy,r,color)

	virus.shape("trash.gif")

	viru.append(virus)




# move all balls
def move_all_balls():
	for ball in BALLS :
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	for  vairus in viru:
		vairus.move(SCREEN_WIDTH,SCREEN_HEIGHT)






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
				r1 = ball_a.r 
				r2 = ball_b.r





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



			MY_BALL.r += 10
			MY_BALL.shapesize(MY_BALL.r/10)
			global score
			score += 1
			turtle.undo()
			turtle.write("instructors you ate :" + str(score),font = ("Arial", 25 , "normal"))

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


	for virus in viru :

		if colide(MY_BALL,virus):
			# return False
			MY_BALL.r = MY_BALL.r - 10
			MY_BALL.shapesize(MY_BALL.r/10)

			global t_score
			t_score += 1
			tr_score.undo()
			tr_score.write("trash you ate:" + str(score),font = ("Arial", 25 , "normal"))

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

			virus.r = Radius
			virus.shapesize(new_ball.r/10)
			virus.goto(X_coordinate,Y_coordinate)
			virus.dx = X_axis_speed 
			virus.dy = Y_axis_speed
			virus.color(Color)

	return True


UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right"

direction = "hope" 

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
def up():
	global direction 
	direction = UP 	    
def down():
	global direction
	direction = DOWN   

def left():
	global direction
	direction = LEFT    
	
def right():
	global direction 
	direction = RIGHT


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)



turtle.listen()
s = 8
          

 # def movearound(event):

# 	X_coordinate = event.x - SCREEN_WIDTH
# 	Y_coordinate = SCREEN_HEIGHT - event.y
# 	MY_BALL.goto(X_coordinate, Y_coordinate)
	


# turtle.getcanvas().bind("<Motion>", movearound)
def move():

	global direction
	my_pos = MY_BALL.pos()
	x_pos = my_pos[0]
	y_pos = my_pos[1]

	if direction == RIGHT:
		MY_BALL.goto( x_pos + s , y_pos)

	elif direction == LEFT:
		MY_BALL.goto( x_pos - s , y_pos)

	elif direction == UP:
		MY_BALL.goto( x_pos , y_pos + s)

	elif direction == DOWN:
		MY_BALL.goto( x_pos , y_pos -s)


turtle.listen()

 




while RUNNING:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2
	move_all_balls()
	check_all_balls_collisions()
	RUNNING = check_myball_collision()
	turtle.update()
	time.sleep(0.01)
	if MY_BALL.r > 100 or MY_BALL.r <= 22 :
		RUNNING = False

	current_x = MY_BALL.xcor()
	new_x = current_x + MY_BALL.dx
	current_y = MY_BALL.ycor()
	new_y = current_y + MY_BALL.dy
	right_side_ball = new_x + MY_BALL.r
	left_side_ball = new_x - MY_BALL.r
	up_side_ball = new_y + MY_BALL.r
	down_side_ball = new_y - MY_BALL.r

	if left_side_ball < -SCREEN_WIDTH or right_side_ball > SCREEN_WIDTH :
		RUNNING = False
		
	if up_side_ball > SCREEN_HEIGHT or down_side_ball < -SCREEN_HEIGHT :
		RUNNING = False
		
	move()

if RUNNING == False :
	gameover.color("white")
	gameover.write(" RIP vampire bro :( " , True , font= ("Spenser", 40 , "bold"))
	screen.bgpic("jk1.gif")
	turtle.update()

time.sleep(3)


 