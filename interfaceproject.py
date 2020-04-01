#!/usr/bin/env python3

import tkinter as tk
import sys
import random

win = tk.Tk()
win.title("Mikayla Smells")
win.geometry('800x480')

def clear():
    for widget in win.winfo_children():
        widget.destroy()
def add():
    task_title = tk.Entry(text='title', width=50)
    task_title.pack()
    task_text = tk.Text()
    task_text.pack()
    task_title = task_title.get()
    print(task_title)
    tk.mainloop()

def practice():
    task = tk.Label(text=f'{random.random()}')
    task.pack()

def exit():
    print('exit button pressed')
    win.quit()

menu = tk.Frame(master=win)
AddButton = tk.Button(menu , text="Add", command=add)
#AddButton.bind('<Button-1>',add)
AddButton.pack(side=tk.LEFT)

PracticeButton = tk.Button(menu, text="Practice", command=practice)
PracticeButton.pack(side=tk.LEFT)
menu.pack()

ExitButton = tk.Button(win,text='Exit',command=exit)
ExitButton.pack(side=tk.BOTTOM)
#ExitButton.bind('<Button-1>',exit)

tk.mainloop()
