#!/usr/bin/env python3
import pandas as pd
import os
import datetime as dt
import time

class Schedule():
    def __init__(self, storage=None):
        self.path = 'data/schedule.json'
        if os.path.isfile(self.path) == False:
            self.storage = pd.DataFrame(columns=['task', 'count', 'time','notes','image'])
            print("You currently have no practice items: let's add stuff now")
        else:
            self.storage = pd.read_json(self.path)
            self.storage.time = pd.to_datetime(self.storage.time, format='%Y-%m-%d %H:%M:%S')
            #self.storage.time = pd.to_datetime(self.storage.time)
            print('df loaded')
            #print(self.storage.head())
        pd.options.display.max_colwidth = 999
        self.storage.style.set_properties(**{'white-space': 'pre-wrap',})
        #print('\n\nTIME:\n\n',self.storage.time,'\n\n')
        #self.storage.time = pd.to_datetime(self.storage.time)

    def save(self):
        # Important! convert time col to string to maintain continuity of data
        self.storage.time = self.storage.time.apply(lambda s: str(s))
        self.storage.to_json(self.path) 

    def now(self): # quick function to return 'now'
        return str(pd.to_datetime(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    def add(self, task, note, image):
        self.storage = self.storage.append([{'task':task, 'count':1, 
            'time':self.now(), 'notes':note, 'image':image}],ignore_index=True)
        self.save()

    def practice(self):
        today = pd.Timestamp.today().strftime('%Y-%m-%d')
        last_item = self.storage[self.storage.time == self.storage.time.max()].index[0]
        choices_df = self.storage[(self.storage.time < today) & (self.storage.index != last_item)]
        if choices_df.shape[0] < 2:
            return None
        largest = choices_df['count'].max()
        smallest = choices_df['count'].min()
        if largest == smallest: 
            # All choices have the same  weight, choose now
            # to avoid division by 0 error below
            return choices_df.sample(1) 
        weights = largest -  choices_df['count']
        weights = weights / weights.sum()
        choice = choices_df.sample(1, weights=weights)        
        return choice
