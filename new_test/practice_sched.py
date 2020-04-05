#!/usr/bin/env python3
import pandas as pd
import os
import datetime as dt
import time
import random
import numpy as np
import csv


class Schedule():
    def __init__(self, storage=None):
        self.path = './schedule.csv'
        if os.path.isfile(self.path) == False:
            self.storage = pd.DataFrame(columns=['task', 'count', 'time','notes'])
            print("You currently have no practice items: let's add stuff now")
        else:
            self.storage = pd.read_csv(self.path, sep='@')
            print('df loaded')
            print(self.storage.head())

    def now(self): # quick function to return 'now'
        return pd.to_datetime(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def add(self, task, note):
        task.replace('@','at') # '@' is my separator value, so can't have that input
        note.replace('@','at')
        self.storage = self.storage.append([{'task':task, 'count':1, 
                                'time':self.now(), 'notes':note}],ignore_index=True)
        self.storage.to_csv(self.path, sep='@', index=False)

    def practice(self):
        today = pd.Timestamp.today().strftime('%Y-%m-%d')
        last_item = self.storage.time.max()
        choices_df = self.storage[(self.storage.time < today) & (self.storage.time != last_item)]

        largest = choices_df['count'].max()
        weights = largest -  choices_df['count']
        weights = weights / weights.sum()
        choice = choices_df.sample(1, weights=weights)        
        return choice

# return df.loc[choice.index] = choice


s = Schedule()
print(s.practice())

# milk - either 2 half-gallons (cardboard) or 1 gallon in plastic (2 half-gallons of plastic is MORE plastic than 1 gallon, so whichever minimizes that)

# chocolate (there's also I think 1 or 2 chocolate oranges in Chris' room)

# that chicken in a bag you said you had

# -sausages (the stuff that's already cooked and ready, like kielbasa)

# -dozen eggs

# -breakfast meat like bacon or frozen bratwurst from home

# -long lasting vegetables - carrots, sweet potato, radishes, etc.

# -mayo (if it uses olive oil as a base)

# -5 avocados

# -apples

# - random bars (kind, clif bar, or anything if it's available)


"""
def Practice():
    os.system('clear')
    total = 0
    choices = []
    weights = []
    timestamps = []
    notes = []
    os.system('touch tempcsvfile.csv')
    with open('schedule.csv') as infile, open('tempcsvfile.csv') as outfile:
        readCSV = csv.reader(infile,delimiter='@')
        for line in readCSV:
            #print(line[0],':::',line[1])
            total += int(line[1])
            choices.append(line[0])
            weights.append(int(line[1]))
            timestamps.append(float(line[2]))
            notes.append(line[3])

        weights = np.asarray(weights)
        largest = np.max(weights) + 1

        timestamps = np.asarray(timestamps)
        now = time.time()
        recent = np.argmin(now-timestamps)
        #setup to remove recently practiced material
        for i in range(len(choices)):
            weights[i]= largest - weights[i]
                
        weights = np.delete(weights,recent)
        #print(choices)
        del choices[recent]
        if len(choices) == 0:
            print("You have nothing to practice, or perhaps your list is empty\n (or you have just 1 item) \n (You don't need a practice manager for just one item bruh ;] ")
            exit(0)
            os.system('rm -f tempschedule.csv')
        #remove the most recently practiced to avoid repeating
        #the same thing twice in a row (can easily modify to
        #remove any practiced today. or within time frame (last hour?))
        newtotal = np.sum(weights)
        weights = weights/newtotal
        weights = list(weights)


        thechoice = np.random.choice(choices,p=weights)
        index = choices.index(thechoice)
        print('\n\n Your task to practice: \n\n',thechoice)
        print('\nNOTES:',notes[index])
        decision = input("\n\ncomplete task\t\t[c]\ncancel (without saving) [x]\t\n\t\t\t\t\t")
        while decision != 'c' and decision != 'x':
            decision = input ('invalid input, only c or x accepted, try again: ')
        if decision == 'x':
            Menu()
            exit(0)
        if decision == 'c':
            newnote = input("Enter notes to help for next time \n \
                    (e.g. where you last left off): ")
            if newnote == '':
                print("\nNo new notes entered, keeping old notes")
                newnote = notes[index]
                

    with open('schedule.csv') as infile, open('tempcsvfile.csv','w') as outfile:
        writer = csv.writer(outfile,delimiter='@')
        for row in csv.reader(infile,delimiter='@'):
        #it makes no sense that the reader isn't working down here, 
        #it works if placed above
            if row[0] != thechoice:
                writer.writerow(row)
            else:
                newline = row[0]+'@'+str(int(row[1])+1)+'@'+str(time.time())+'@'+newnote
                command = "echo '"+newline+"' >> tempcsvfile.csv"
    os.system(command)
    os.system('rm schedule.csv; mv tempcsvfile.csv schedule.csv') 
    Menu()
    exit(0)
        
def Menu():
    choice = input('\nWould you like to Add, Practice or Quit?\n\t\tenter a,p or q : ')
    while choice != 'a' and choice !='p' and choice !='q':
        choice = str(input('\nInvalid input, try again: a,p, or q: '))
    if choice == 'q':
        exit(0)
    elif choice == 'p':
        Practice()
        input("Press <enter> when done! ")
        Menu()
    elif choice == 'a':
        Add()
        Menu()



os.system('clear')

PATH='./schedule.csv'
if os.path.isfile(PATH) == False:
        print("You currently have no practice items: let's add stuff now")
        Add()

Menu()
"""
