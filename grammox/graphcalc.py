
# graphing calculater

import matplotlib.pyplot as plt
from tkinter import *


# enter a equation and get the graph of it
# e.g: 5x+3
# plots the graph for it


def parseout_slope(string):
	digits = ['0','1','2','3','4','5','6','7','8','9']
	slopeM = ''
	for x in range(len(string)):
		if string[x] in digits:
			slopeM += string[x]
		else:
			if string[x] == '+' or string[x] == '-':
				pass
			else:
				break
	return int(slopeM)

def parseout_intercept(string):
	digits = ['0','1','2','3','4','5','6','7','8','9']
	yIntercept = ''
	operatorPos = 0
	for x in range(len(string)):
		# check if the element is a operator
		if string[x] == '+' or string[x] == '-':
			# ignore if the 1st element is a operator
			if string[0] == '+' or string[0] == '-':
				pass
			operatorPos = x
	# slice the string and convert to int
	yIntercept = int(string[operatorPos+1:])
	return yIntercept

def equation_parser(string = None):	
	slope = parseout_slope(string)
	intercept = parseout_intercept(string)
	#print(slope,intercept)
	xl = [i for i in range(10)]
	y = [slope*x+intercept for x in xl]
	showPlot(xl,y)
	
def showPlot(xl,y):
	plt.scatter(xl,y)   
	plt.plot(xl,y)
	plt.show()

class TkApp():

	def __init__(self,app):
		self.app = app
		self.app.title('Grammox')
		self.app.geometry("200x300+300+200")
		self.app.resizable(0,0)
		self.app.config(bg = "black")
		self.equation_tab = Entry(self.app,width = 21)
		self.equation_tab.grid(column = 0,row = 1,padx = 5,pady = 5, ipadx = 3,ipady = 3)
		self.show_graph_btn = Button(self.app,text = "Show Graph",cursor='hand2',command=self.ShowGraph,width = 19,bd = 0,bg = "grey",fg = 'white')
		self.show_graph_btn.grid(column = 0,row = 2,padx = 5,pady = 5,ipadx = 3,ipady = 3)
		# get the equation
		self.eq = str(self.equation_tab.get())

	def ShowGraph(self):
		equation_parser(self.eq)





#equation_parser()

WApp = Tk()
win = TkApp(WApp)
WApp.mainloop()
