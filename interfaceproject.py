#!/usr/bin/env python3

from tkinter import *
import sys

win = Tk()
win.title("Mikayla Smells")
win.geometry('800x480')


def add():
	added=input("type something: ")
	print(added)
	mainloop()

def exit():
	print('exit button pressed')
	win.quit()

AddButton = Button(win,text="Add",command=add)
AddButton.pack()
#AddButton.bind('<Button-1>',add)

ExitButton = Button(win,text='Exit',command=exit)
ExitButton.pack(side=BOTTOM)
#ExitButton.bind('<Button-1>',exit)

mainloop()
