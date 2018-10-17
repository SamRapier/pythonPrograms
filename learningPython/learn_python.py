# Learning to use python
# These are the basic commands

# Using strings
def usingStrings():
	print('cocatination')
	print('you must use a comma to concatonate numbers: ', 15)
	print('Hey Hi\'a there')    

# Maths
# exponent
def maths():
	print('\nExponents')
	print(4**5)  # this is 4 to the power 5




# While loop
def whileLoops():
	condition = 1
	print('\nWhile loop example')
	while condition < 10:
		print(condition)
		condition += 1


# For loops
def forLoops():
	print('\nFor loops')
	Garage = "Ferrari", "Jaguar", "Porche", "Mini", "BMW"
	for car in Garage:
		print(car)

	print('For loop that is like a counter')
	for x in range(1,12):
		print(x)


# If statements
def ifStatements():
	print('\nif loops')
	x = 5
	y = 10
	if x > y:
		print('x is greater than y')
	elif x < y:
		print('y is greater than x')
	else:
		print('x = y')


# Function
def functions():
	print('\nfunctions')
	def example_function(num1, num2):
		print('num1: ', num1)
		z = num1 + num2
		print(z)

	example_function(3, 5)
	example_function(num2 = 8, num1 = 12)



# Input
def take_inputs():
	print('\nInputs')
	var_input = input('Enter some text: ')
	print('text entered: ', var_input)


# Interacting with files
def fileInteraction():
	text = ('Testing saving to a file. \nNew line!')

	# tells python that you are opening a file
	saveFile = open('exampleFile.txt', 'w')
	# writes to the file
	saveFile.write(text)
	# remember to close the file or problems could arise
	saveFile.close()

	# Appending files
	appendText = ('\nNew information in the example text document')
	appendFile = open('exampleFile.txt', 'a')
	appendFile.write(appendText)
	appendFile.close()

	# Reading from files
	readMe = open('exampleFile.txt','r').read()
	print(readMe)

	# this will instead read the file into a python list. 
	readMe = open('exampleFile.txt','r').readlines()
	print(readMe)

# Classes
class calculator:
	
	def addition(x,y):
		added = x + y
		print(added)
		
	def subtraction(x,y):
		sub = x - y
		print(sub)

	def multiplication(x,y):
		mult = x * y
		print(mult)

	def division(x,y):
		div = x / y
		print(div)

def usingClasses():
	calculator.addition(4,8)
	calculator.subtraction(9,3)
	calculator.multiplication(7,5)
	calculator.division(2,6)



# Using the statistics module
def statisticsModule():
	print('\nStatistic module')
	import statistics

	example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

	x = statistics.mean(example_list)
	print(x)

	y = statistics.median(example_list)
	print(y)

	z = statistics.mode(example_list)
	print(z)

	a = statistics.stdev(example_list)
	print(a)

	b = statistics.variance(example_list)
	print(b)


# List manipulation
def listManipulation():
	print('\nLists/arrays')
	# lists are like arrays in other programming languages
	# there are also tuples in python which are similar to lists but you cannot change them
	x = [4, 7, 8, 2, 3, 9, 10, 2, 1, 2]

	# to add to the end of a list use append
	x.append(2)
	print(x)

	# you can insert data into the index that you want
	x.insert(3, 12)
	print(x)

	# removes the first instance of the value in the list 
	x.remove(12)
	print(x)

	# you can search a list
	print(x.index(2))       # this shall return the index of where the first instance of that value appears

	# you can count how many of a particular value there are
	print(x.count(2))

	# there is a sort function as well
	x.sort()
	print(x)

	x.reverse()
	print(x)


# Multidimentional lists/arrays
def multidimentionalLists():
	print('\nMultidimentional lists')

	x = [
			[
				[5,6],
				[9,8]
			],
			[
				[3,7],
				[2,1]
			],
			[
				[4, 10],
				[9, 5]
			]
		]

	print(x)
	print(x[1])
	print(x[2][1][0])

# CSV(comma seperated variables)
# Also showing of error handling using try and except
def csvExample():
	print('\nReading CSV files')
	import csv
	with open('exampleCSV.csv') as csvFile:
		readCSV = csv.reader(csvFile, delimiter=',')
		colours = []
		dates = []
		for row in readCSV:
			date = row[0]
			colour = row[3]

			colours.append(colour)
			dates.append(date)
		
		print(dates)
		print(colours)

		# try an excecute this block of code
		try:
			whatColour = input('What color do you wish to know the date of?: ')

			if whatColour in colours:
				colourIndex = colours.index(whatColour.lower())
				theDate = dates[colourIndex]
				print('The date of ',whatColour,'is: ',theDate)
			
			else:
				print('The colour you entered was not found or is not a colour')

		# if there is an error in that block of code, run the exception
		# if there is no error, ingore this exception
		except Exception as err:
			print(err)

		print('continuing')



# Multi-line printing
def multiLinePrinting():
	print('''
	This 
	is
	a
	multi-line
	print
	''')

	print('''
	=================
	|               |
	|               |
	|      BOX      |
	|               |
	|               |
	=================
	''')

# Dictionaries
def dictionairesExample():
	print('\nDictionaries')
	# Dictionaries are defined with {} brackets
	exampleDictionary = {'Jack':15, 'Bob':22, 'Alice':12, 'Kevin':17}
	print(exampleDictionary)
	print(exampleDictionary['Jack'])

	# Add another item to the dictionary
	exampleDictionary['Tim'] = 16
	print(exampleDictionary)

	# updating the dictionary with new data
	exampleDictionary['Tim'] = 17
	print(exampleDictionary)

	# Delete an item in the dictionary
	del exampleDictionary['Tim']
	print(exampleDictionary)

	exDict = {'Jack':[15, 'blonde'], 'Bob':[22, 'brown'], 'Alice':[12, 'black'], 'Kevin':[17, 'ginger']}
	print(exDict['Jack'][1])


# Built in functions
def builtInFunctions():
	# Absolute value
	num1 = -5
	num2 = 5
	print(abs(num1))

	if (abs(num1) == num2):
		print('identical')

	# Max and min
	exList = [5,2,6,8,1,2]
	print(max(exList))
	print(min(exList))

	# Rounding
	x = 5.91285
	print(round(x))

	# Converting strings to integers or floating points
	intMe = '55'
	print(intMe)
	print(int(intMe))
	print(float(intMe))

	# Converting integers to strings
	strMe = 234
	print(strMe)
	print(str(strMe))



# OS Module
def osModule():
	import os
 
	# get current working directory
	currentDirectory = os.getcwd()      
	print(currentDirectory)

	# make a new directory
	os.mkdir('newDir')
	
	# renaming the directory after 2 seconds
	import time
	time.sleep(2)
	os.rename('newDir', 'newDir2')

	# removing the directory after 2 seconds
	time.sleep(2)
	os.rmdir('newDir2')


# SYS module
def sysModule():
	import sys

	# stderr should really only be used for errors
	sys.stderr.write('This is stderr text \n')
	sys.stderr.flush()

	# stdout can be used to output to the system
	sys.stdout.write('This is stdout text \n')

	# argv can be used to pass arguments into the python file using to command line
	# can be used to communicate between different languages
	print(sys.argv, '\n')

	# in the command line I typed in python learn_python.py "look at that!" 
	# and the output is just look at that!
	if len(sys.argv) > 1:
		print(sys.argv[1])
		# we are now passing through a number instead of "look at that!"
		print(float(sys.argv[1]) + 5)

	
# urllib Module
def urllibModule():
	import urllib.request
	import urllib.parse
	
	# x = urllib.request.urlopen('https://www.google.com')
	# print(x.read())

	
	url = 'http://pythonprogramming.net/search'
	values = {'q':'basic'}
	data = urllib.parse.urlencode(values)	
	data = data.encode('utf-8')
	req = urllib.request.Request(url,data)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	print(respData)
	

	try:
		x = urllib.request.urlopen('https://www.google.com/search?q=test')
		
		print(x.read())
	except Exception as err:
		print(str(err))

	try:
		url = 'https://www.google.com/search?q=test'

		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		req = urllib.request.Request(url, headers=headers)
		resp = urllib.request.urlopen(req)
		respData = resp.read()

		saveFile = open('withHeaders.txt', 'w')
		saveFile.write(str(respData))
		saveFile.close()

	except Exception as err:
		print(str(err))
	


# Regular Expressions with regex
def regularExpressions():
	# Identifiers:
	# \d 		any number
	# \D		anything but a number
	# \s 		space
	# \S		anything but a space
	# \w 		any character
	# \W		anything but a character
	# .		any character, except for a new line
	# \b		the whitespace around words
	# \.		a dot

	# Modifiers:
	# {x,y}	we're expecting x to y bits of data
	# +		match 1 or more
	# ?		match 0 or 1
	# *		match 0 or more
	# $		match the end of a string
	# ^		matching the beginning of a string
	# |		matches either, or
	# []		range or "variance"
	# {x}		expecting "x" amount

	# White Space Characters:
	# \n		new line
	# \s 		space
	# \t		tab
	# \e		escape
	# \f 		form feed
	# \r		return
	

	import re

	exampleString = '''
	Jessica is 15 years old, and Daniel is 27 years old.
	Edward is 97 and his grandfather, Oscar is 102.
	'''

	ages = re.findall(r'\d{1,3}', exampleString)
	names = re.findall(r'[A-Z][a-z]*', exampleString)

	print(ages)
	print(names)

	ageDict = {}
	x = 0
	for eachName in names:
		ageDict[eachName] = ages[x]
		x+=1

	print(ageDict)


# Parse a website using urllib and regex
def parseWebsite():
	import urllib.request
	import urllib.parse
	import re

	url = 'http://pythonprogramming.net/search'
	url2 = 'https://pythonprogramming.net/search/?q=basic'
	values = {'q':'basic'}
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8')
	req = urllib.request.Request(url, data)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

	for eachP in paragraphs:
		print(eachP)


# Using the tkinter  module
def tkinterModule():
	import tkinter as tk
	from PIL import Image, ImageTk

	# We create our class, Window, and inherit from the Frame calss. 
	# Frame is a class from the tkinter module
	class Window(tk.Frame):

		# Define the settings upon initialisations
		def __init__(self, master = None):
			# These are the parameters that you want to send through to the frame class
			tk.Frame.__init__(self, master)

			# This is the reference to the master widges which is the tk window
			self.master = master

			# We then wasn to run init_window, which is our own function
			self.init_window()
		
		
		def init_window(self):
			# Giving the window some properties
			# changing the title of the master widget
			self.master.title("GUI")

			# Letting the widget take the full space of the root window
			self.pack(fill = tk.BOTH, expand = 1)
			

			# Making buttons using tkinter
			# Creating a button instance
			btnExample = tk.Button(self, text="button", command=self.btnExamplePress)

			# placing the button on the window
			btnExample.place(x = 0, y = 0)


			# Adding a menu bar to the widget
			# creating a menu instance
			menuExample = tk.Menu(self.master)
			self.master.config(menu=menuExample)


			# create the file object
			file = tk.Menu(menuExample)
			# adds a command to the file menu option naming it exit and it 
			# runs the clientExit command which is defined by us
			file.add_command(label = 'Exit', command = self.clientExit)
			file.add_command(label = 'Save', command = self.clientSave)			# Adds another command named save, it does nothing but is an example of how to do it

			# added "file" to our menu
			menuExample.add_cascade(label='File', menu = file)


			# create the edit object
			edit = tk.Menu(menuExample)
			# adds a command to the file menu option naming it undo 
			edit.add_command(label='Undo', command = self.clientUndo)
			edit.add_command(label='Show Image', command = self.showImage)
			edit.add_command(label='Show Text', command = self.showText)
			# Added "edit" to our menu
			menuExample.add_cascade(label='Edit', menu = edit)


		# This is the command that runs whent the button is clicked
		def btnExamplePress(self):
			print('Button has been pressed')

		def clientExit(self):
			exit()

		def clientSave(self):
			print('Save has been pressed')

		def clientUndo(self):
			print('Undo has been pressed')

		def showImage(self):
			load = Image.open('pic.png')
			render = ImageTk.PhotoImage(load)

			img = tk.Label(self, image=render)
			img.image = render
			img.place(x=0, y=40)

		def showText(self):
			text = tk.Label(self, text='Hello World')
			text.pack()


	root = tk.Tk()
	# Setting the size of the window
	root.geometry("600x600")
	app = Window(root)
	root.mainloop()

	

# Threading 
def threadingModule():
	import threading
	from queue import Queue
	import time

	q = Queue()

	# A special lock added to the printing fucntion so that two threads cannot print at the same time
	printLock = threading.Lock()
	
	def exampleJob(job):
		# This job is mimicing actual computing, the computing takes 0.5 seconds
		time.sleep(0.5)		

		# It then uses the printLock, so does not allow any other thread to print
		with printLock:
			# It then prints some information and then releases the printLock
			print(threading.current_thread().name, job)

	# This is the core function
	def threader():
		# This is an infinite loop
		while True:
			# It gets a task from the queue
			job = q.get()
			# Performs some computing task
			exampleJob(job)
			# Removes the task from the queue
			# It then releases the thread back so that it can perform another job
			q.task_done()




	# We have 10 workers / threads
	for x in range(10):
		# t is our thread, it runs through the function threader
		t = threading.Thread(target = threader)
		# The thread will die when the main thread dies
		t.daemon = True
		# The thread is started, this must come after daemon definition
		t.start()

	# taking note of when the task was started
	start = time.time()

	# We have 20 jobs
	for job in range(20):
		# We have 20 jobs so we put each job into the queue
		q.put(job)

	# block all taks until all of the processes in the queue have been processed
	# Wait until the thread terminated
	q.join()

	# If there were 20 tasks which each took 0.5s, and it was done on a single thread,
	# it would take 10s. The result outputed show that using 10 threads, it took just over 1s
	# so each thread was able to work simultaneously
	end = time.time()
	print('Entire job took: ', end - start)


def matplotlibModule():
	from matplotlib import pyplot as plt
	from matplotlib import style

	style.use('ggplot')

	x = [5,6,7,8]
	y = [2,7,3,10]

	plt.plot(x,y, 'c', label = 'line one', lineWidth  = 2)

	plt.title('Epic Chart')
	plt.ylabel('Y axis')
	plt.xlabel('X axis')

	plt.legend()
	plt.grid(True,color='k')

	

	plt.show()

def evalMethod():
	lstStr = "[2,6,2,4,87,1]"
	lstInt = eval(lstStr)

	print(lstStr)
	print(lstInt)
	print(lstInt[3])

	x = input("code: ")

	# You can run a function that has been input by the user
	y = eval(input("code: "))
	print(y)


def execMethod():
	print('ded')
	# A dangeros function

execMethod()