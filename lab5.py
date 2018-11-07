#problem 1
# import tkinter as tk
# from tkinter import simpledialog

# #Then when ever you want to ask the user for input use this code
# greeting = simpledialog.askstring("Input","Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())

# if greeting in ["Arrr!"] :
# 	print("Go away, pirate.")
# elif():
# 	print("Greetings, hater of pirates!")

#problem 2

# import tkinter as tk
# from tkinter import simpledialog



# year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

# if year <= 1900 :
#     print ("Woah, that's the past!")
# elif year > 1900 and year < 2020:
#     print ("That's totally the present!")
# else:
#     print ("Far out, that's the future!!")

# problem 3


# class Person():
# 	def __init__(self, first_name, last_name):
#     		self.first = first_name
#     		self.last = last_name
# 	def speak(self):
#   		print("My name is " +  self.first + " " + self.last )

# me = Person("Brandon", "Walsh")
# you = Person("Ethan", "Reed")

# me.speak()
# you.speak()

#problem 4


import tkinter as tk
from tkinter import simpledialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average
