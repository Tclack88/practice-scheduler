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
    AddButton.pack_forget()
    PracticeButton.pack_forget()
    def notes():
        def submit():
            submit_button.destroy()
            task_notes.destroy()
            note_label.destroy() 
            AddButton.pack(side=tk.LEFT)
            PracticeButton.pack(side=tk.LEFT)
        note_label = tk.Label(text='edit note or keep the same')
        note_label.pack()

        task_notes = tk.Text()
        task_notes.pack()
        task_notes.insert(tk.END,'old notes')
        note = task_notes.get('1.0', tk.END)
        submit_button = tk.Button(menu, text = 'submit notes', command=submit)
        submit_button.pack()
    def enter():
        title = task_title.get()
        print(repr(title))

        text = task_text.get('1.0', tk.END)
        print(repr(text))

        task_title.delete(0,tk.END)
        task_title.destroy()
        task_text.destroy()
        EnterButton.destroy()
        notes()

    #add_frame = tk.LabelFrame(master=win, text='add frame')
    #add_frame.pack()
    task_title = tk.Entry(text='title', width=50)
    task_title.pack()
    task_text = tk.Text()
    task_text.pack()
    EnterButton = tk.Button(menu, text="Enter", command=enter)
    EnterButton.pack()
    #tk.mainloop()

def practice():
    AddButton.pack_forget()
    PracticeButton.pack_forget()
    def complete():
        print('task completed!')
        task.destroy()
        complete_button.pack_forget()
        cancel_button.pack_forget()
        AddButton.pack(side=tk.LEFT)
        PracticeButton.pack(side=tk.LEFT)
    def cancel():
        print('task cancelled :[')
        task.destroy()
        complete_button.pack_forget()
        cancel_button.pack_forget()
        AddButton.pack(side=tk.LEFT)
        PracticeButton.pack(side=tk.LEFT)

    complete_button = tk.Button(menu, text='Complete', command=complete)
    cancel_button = tk.Button(menu, text='Cancel', command=cancel)
    complete_button.pack(side=tk.LEFT)
    cancel_button.pack(side=tk.LEFT)
        
        
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

add_frame = tk.LabelFrame(master=win, text='add frame')
add_frame.pack()

ExitButton = tk.Button(win,text='Exit',command=exit)
ExitButton.pack(side=tk.BOTTOM)
#ExitButton.bind('<Button-1>',exit)

tk.mainloop()
