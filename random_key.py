import random

keys = list('ABCDEFG')
sharps = ['F#','G#','A#','C#','D#']
flats = ['Bb','Ab','Gb','Eb','Db']

keys_and_sharps = keys+sharps
keys_and_flats = keys+flats

print('<Enter> for a new key')

while True:
    input()
    selection_pool = random.choice([keys_and_sharps, keys_and_flats])
    note = random.choice(selection_pool)
    print(note)
