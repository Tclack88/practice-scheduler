# Scheduler

![https://github.com/Tclack88/blog/blob/gh-pages/assets/gui/gui_logo.png](https://github.com/Tclack88/blog/blob/gh-pages/assets/gui/gui_logo.png?raw=true)

Read more about the project [on my blog](https://tclack88.github.io/blog/code/2020/05/27/gui.html)

A simple terminal-based python script for determining what to practice next

EDIT: Tkinter GUI added

EDIT: PyQt QUI added

## some background

I play piano and am learning Jazz. There's just so much content and I'm not gonna be able to go back and readily recall what scale or chords to practice. Every time I learn something new I put it in here.

I used to do spaced-repetition, but that's NOT what this is, because that can get ahead of you then, over time, we lost motivation to catch up and stop. This is designed to continue where you left off.

Items to be practiced are emphasized on two criteria:
- It's been a while since you last practiced
- This item doesn't have that many "repetitions"

In other words, new things are given emphasis because they're not as "ingrained" as longer term stuff and stuff that hasn't been played in a while get's a weight in the selected practice item (which is chosen at random according to weights)


## Hopes for the future:

[ ] Multiple projects can be scheduled

[x] An interface
-tKinter GUI created (thinking of adding one for PyQt to allow drag and drop capability

~~(NOTE: I wrote this before I learned pandas, so this can probably be vastly improved)~~
^(pandas incorporated in tkinter)

[x] Improved interface with image drag and drop capabilities (PyQt?)
