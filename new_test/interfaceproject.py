#!/usr/bin/env python3

import tkinter as tk
import sys
import random
from practice_sched import Schedule
s = Schedule()

win = tk.Tk()
win.title("Mikayla Smells")
win.geometry('800x480')

def clear():
    for widget in win.winfo_children():
        widget.destroy()
def add():
    add_button.pack_forget()
    PracticeButton.pack_forget()
    def enter():
        task = task_entry.get()
        notes = task_notes.get('1.0', tk.END)
        s.add(task,notes)

        task_entry.delete(0,tk.END)
        task_entry.destroy()
        task_notes.destroy()
        EnterButton.destroy()
        add_button.pack(side=tk.LEFT)
        PracticeButton.pack(side=tk.LEFT)

    task_entry = tk.Entry(text='task', width=50)
    task_entry.pack()
    task_notes = tk.Text()
    task_notes.pack()
    EnterButton = tk.Button(menu, text="Enter", command=enter)
    EnterButton.pack()

def practice():
    add_button.pack_forget()
    PracticeButton.pack_forget()
    def complete():
        print('task completed!')
        updated_notes = notes.get('1.0',tk.END)
        practice_item.notes = updated_notes
        practice_item.time = s.now()
        print(practice_item.index)
        s.storage.iloc[practice_item.index] = practice_item
        s.save()
        print(practice_item)
        print(practice_item)
        task.destroy()
        notes.destroy()
        complete_button.pack_forget()
        cancel_button.pack_forget()
        add_button.pack(side=tk.LEFT)
        PracticeButton.pack(side=tk.LEFT)
    def cancel():
        print('task cancelled :[')
        try:
            task.destroy()
            notes.destroy()
        except NameError:
            invalid.pack_forget()
            pass
        complete_button.pack_forget()
        cancel_button.pack_forget()
        add_button.pack(side=tk.LEFT)
        PracticeButton.pack(side=tk.LEFT)

    complete_button = tk.Button(menu, text='Complete', command=complete)
    cancel_button = tk.Button(menu, text='Cancel', command=cancel)
    complete_button.pack(side=tk.LEFT)
    cancel_button.pack(side=tk.LEFT)
        
    practice_item = s.practice()
    if practice_item is not None: # i.e. not none
        print(practice_item)
        task = tk.Label(text=practice_item.task.to_string(index=False), wraplength=500)
        notes = tk.Text()
        notes.insert('1.0', practice_item.notes.to_string(index=False).strip().replace('\\n','\n'))
        # ^ janky
        task.pack()
        notes.pack()
    else:
        add_button.pack_forget()
        complete_button.pack_forget()
        invalid.pack()

def exit():
    print('exit button pressed')
    win.quit()

menu = tk.Frame(master=win)
add_button = tk.Button(menu , text="Add", command=add)
#add_button.bind('<Button-1>',add)
add_button.pack(side=tk.LEFT)

PracticeButton = tk.Button(menu, text="Practice", command=practice)
PracticeButton.pack(side=tk.LEFT)
menu.pack()

add_frame = tk.LabelFrame(master=win, text='add frame')
add_frame.pack()

invalid = tk.Label(text='Not enough items to practice, add more and/or try again a different day')

exit_button = tk.Button(win,text='Exit',command=exit)
exit_button.pack(side=tk.BOTTOM)
#exit_button.bind('<Button-1>',exit)

tk.mainloop()
