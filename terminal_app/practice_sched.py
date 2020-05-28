#!/usr/bin/env python3

import os
import time
import random
import numpy as np
import csv

def Add():
    comment = input("\nEnter new item to add to add to practice rotation: \n")
    newnote = input("Enter a note to help (e.g. where you last left off): \n")
    command = "echo '"+comment+"@0@"+str(time.time())+"@"+str(newnote)+"' >> schedule.csv"
    os.system(command)
    Menu()
    exit(0)


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
