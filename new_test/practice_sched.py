#!/usr/bin/env python3
import pandas as pd
import os
import datetime as dt
import time
import csv

class Schedule():
    def __init__(self, storage=None):
        self.path = './schedule.csv'
        if os.path.isfile(self.path) == False:
            self.storage = pd.DataFrame(columns=['task', 'count', 'time','notes'])
            print("You currently have no practice items: let's add stuff now")
        else:
            self.storage = pd.read_json(self.path)
            #self.storage.time = pd.to_datetime(self.storage.time, format='%Y-%m-%d %H:%M:%S')
            print('df loaded')
            print(self.storage.head())
        pd.options.display.max_colwidth = 999
        self.storage.style.set_properties(**{'white-space': 'pre-wrap',})

    def save(self):
        self.storage.to_json(self.path) 

    def now(self): # quick function to return 'now'
        return str(pd.to_datetime(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def add(self, task, note):
        task.replace('@','at') # '@' is my separator value, so can't have that input
        note.replace('@','at')
        self.storage = self.storage.append([{'task':task, 'count':1, 
                                'time':self.now(), 'notes':note}],ignore_index=True)
        print(self.now())
        #self.storage.to_csv(self.path, sep='@', index=False)
        self.save()

    def practice(self):
        today = pd.Timestamp.today().strftime('%Y-%m-%d')
        #last_item = self.storage[self.storage.time == self.storage.time.max()]
        # the above is an attempt to make it more general, i.e. don't assume
        # the last item in thecsv is the most recent
        last_item = self.storage.shape[0]
        print("Last Item:", last_item)
        choices_df = self.storage[(self.storage.time < today) & (self.storage.index != last_item)]
        if choices_df.shape[0] < 2:
            return None
        print('LENGTH:', choices_df.shape[0])
        largest = choices_df['count'].max()
        weights = largest -  choices_df['count']
        weights = weights / weights.sum()
        choice = choices_df.sample(1, weights=weights)        
        print('\n\n CHOICES REMAINING:')
        print(choices_df.shape[0])
        print(self.storage.shape[0])
        print(choices_df)
        return choice
