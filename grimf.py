import turtle
import random
import math
from turtle import *



turtle.register_shape("DEMONS.gif")
turtle.register_shape("RAVEN.gif")
turtle.register_shape("grimfBG.gif")
turtle.bgpic("grimfBG.gif")


RUNNING = True 
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2

number_of_bullets = 1
BULLETS = []

NUMBER_OF_ENEMIES = 5
ENEMIES = []
ENEMY_RAD = 10



MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5


turtle.tracer(100,1)




class Character(Turtle):
	def __init__(self, x, y, dx, dy, r, shape,color):
		Turtle.__init__(self)
		self.pu()
		self.shape(shape)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.color(color)

		current_x = self.xcor()
	

	def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_enemy = new_x + self.r
		left_side_enemy = new_x - self.r
		up_side_enemy = new_y + self.r
		down_side_enemy = new_y - self.r

		if (right_side_enemy >= SCREEN_WIDTH) or (left_side_enemy <= -SCREEN_WIDTH):
			self.dx = -1 * self.dx

		if (up_side_enemy >= SCREEN_HEIGHT) or (down_side_enemy <= -SCREEN_HEIGHT) :
			self.dy = -1 * self.dy
		self.goto(new_x,new_y)





Raven = Character(0,0,0.7,0.7,35,"RAVEN.gif","red")

class bullet(Turtle):
	def __init__(self,x,y,dx,dy,r,shape,color):
		Turtle.__init__(self)
		self.ht()
		self.x = x 
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color("yellow")
		self.pu()      
		self.goto(x,y)
		self.showturtle()
		turtle.pu()



	def bullets_collision(self,SCREEN_WIDTH , SCREEN_HEIGHT):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_bullet = new_x + self.r
		left_side_bullet = new_x - self.r
		up_side_bullet = new_y + self.r
		down_side_bullet = new_y - self.r
		self.SCREEN_WIDTH = SCREEN_WIDTH
		self.SCREEN_HEIGHT = SCREEN_HEIGHT
		self.goto(new_x,new_y)



		if left_side_bullet < -SCREEN_WIDTH or right_side_bullet > SCREEN_WIDTH :
			self.clear()
			self.ht()
		
		if up_side_bullet > SCREEN_HEIGHT or down_side_bullet < -SCREEN_HEIGHT :
			self.clear()
			self.ht()




def enemies_bullets_collision(enemy,new_bullet):
	x1 = enemy.xcor()
	x2 = new_bullet.xcor()
	y1 = enemy.ycor()
	y2 = new_bullet.ycor()

	if math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)) + 10 <= enemy.r + new_bullet.r :
		enemy.clear()
		enemy.ht()
		print("there is a collision")

def all_enebull_colli():
	for enemy in ENEMIES:
		for bullet in BULLETS:
			enemies_bullets_collision(enemy, bullet)







# creating enemies 


for enemy in range(NUMBER_OF_ENEMIES):


	x = random.randint( -SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS) 
	dx = 0.5 
	dy = 0.5
	enemycolor = "green"
	r = 30
	enemyshape = "DEMONS.gif"

	new_enemy = Character(x,y,dx,dy,r,enemyshape,enemycolor)


	ENEMIES.append(new_enemy)




def move_enemies():
	for enemy in ENEMIES :
		enemy.move(SCREEN_WIDTH,SCREEN_HEIGHT)



# making Ravan move 

UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right"
SPACE_PRESS = "space"
direction = "hope" 


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
SPACE = 4

def up():
	print("up!")
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
def space() :
	for i in range(number_of_bullets):
		bullx = Raven.xcor()
		bully = Raven.ycor()
		bulldx = Raven.dx
		bulldy = Raven.dy
		bullcolor = "yellow"
		bullr = 20
		bullshape = "circle"

		new_bullet = bullet(bullx,bully,bulldx*1.5,bulldy*1.5,bullr,bullshape,bullcolor)


		BULLETS.append(new_bullet)



turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(space,SPACE_PRESS)


turtle.listen()
s = 1
# f = 50




def move_Raven():


	global direction
	my_pos = Raven.pos()
	x_pos = my_pos[0]
	y_pos = my_pos[1]

	if direction == RIGHT:
		Raven.goto( x_pos + s , y_pos)
		Raven.dx = 1
		Raven.dy = 0

	elif direction == LEFT:
		Raven.goto( x_pos - s , y_pos)
		Raven.dx = -1
		Raven.dy = 0

	elif direction == UP:
		Raven.goto( x_pos , y_pos + s)
		Raven.dx = 0
		Raven.dy = 1

	elif direction == DOWN:
		Raven.goto( x_pos , y_pos -s)
		Raven.dx = 0
		Raven.dy = -1



		current_x = Raven.xcor()
		new_x = current_x + Raven.dx
		current_y = Raven.ycor()
		new_y = current_y + Raven.dy
		right_side_Raven = new_x + Raven.r
		left_side_Raven = new_x - Raven.r
		up_side_Raven = new_y + Raven.r
		down_side_Raven = new_y - Raven.r

		if (right_side_Raven >= SCREEN_WIDTH) or (left_side_Raven <= -SCREEN_WIDTH):
			Raven.dx = -1 * Raven.dx

		if (up_side_Raven >= SCREEN_HEIGHT) or (down_side_Raven <= -SCREEN_HEIGHT) :
			Raven.dy = -1 * Raven.dy



def move_bullets():
	for bullet in BULLETS:
		bullet.bullets_collision(SCREEN_WIDTH, SCREEN_HEIGHT)


turtle.listen()


while True:
	
	move_Raven()
	move_bullets()
	turtle.update()
	# shooting()
	turtle.update()
	all_enebull_colli()
	move_enemies()

turtle.done()

