import turtle
turtle.register_shape("Caleb.gif") 
turtle.shape("Caleb.gif")
for i in range(100):
	turtle.forward(200)
	turtle.right(45)
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(50)
	turtle.goto(0,0)
	turtle.right(50)




turtle.mainloop()