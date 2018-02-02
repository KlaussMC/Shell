from tkinter import *
from shell.shell import *

root = Tk()

Lines = []

altKey = False
ctrlKey = False
shiftKey = False

root.minsize(720, 360)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

Main = Frame(background='#151515')
Main.grid(row=0, column=0, sticky=N+S+W+E)

Main.grid_columnconfigure(0, weight=1)
Main.grid_rowconfigure(0, weight=1)

l = Label(Main, text="$", background="#151515", foreground="#a00", font=("Consolas", 14))
l.grid(row=0, column=0, sticky=N+W)
Lines.append(l)

line = Entry(root, background="#333", foreground="#a00", bd=0, font=("Consolas", 14))
line.grid(row=1, column=0, ipadx=5, ipady=5, sticky=E+W)

root.bind("<Button-1>", line.focus())
root.bind("<key>")

def updateOutput():
	# global Lines
	# global Main
	# Main.destroy()
	#
	# Main = Frame(background='#151515')
	# Main.grid(row=0, column=0, sticky=N+S+W+E)
	#
	# Main.grid_columnconfigure(0, weight=1)
	#
	# for i in range(len(Lines)):
	# 	Main.grid_rowconfigure(i, weight=1)
	# 	Lines[i].grid(row=i, column=0, sticky=N+W)

	global Lines
	global Main
	Main.destroy()
	Main = Main = Frame(background='#151515')
	Main.grid(row=0, column=0, sticky=N+S+W+E)

	for i in range(len(Lines)):
		Main.grid_rowconfigure(i, weight=1)
		Lines[i].grid(row=1, column=0, sticky=N+W)

def keyup(e):
	global ctrlKey
	global shiftKey
	global altKey
	key = e.keycode

	if (key == 16):
		shiftKey = False
	if (key == 17):
		ctrlKey = False
	if (key == 18):
		altKey = False

def keydown(e):
	global ctrlKey
	global shiftKey
	global altKey
	key = e.keycode

	global Lines
	if (key == 13):
		l = Label(Main, text=loop(line.get()), background="#333", foreground="#eee", font=("Consolas", 14))
		# l.grid(row=(len(Lines) - 1), column=0, sticky=N+W)
		Lines.append(l)
		updateOutput()

def resetKeys():
	shiftKey = False
	altKey = False
	ctrlKey = False

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

root.mainloop()
