#this code is not compleated pls compleate it ashutosh raghuwanshi

import random
import time
from tkinter import Tk,Button,DISABLED

def show_symbol(x,y):
    global first
    global previousx,previousy
    buttons[x,y]['text']=button_symbols[x,y]
    button[x,y].update_ideltask()






win=Tk()
win.resizable(width=False,height=False)

first=True
previousx=0
previousy=0

buttons={}
button_symbols={}
symbol=[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u2718',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u2718',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716']
random.shuffle(symbol)

for x in range(6):
    for y in range(4):
        button=Button(command=show_symbol(x,y),width=3,height=3)
        button.grid(column=x,row=y)
        buttons[x,y]=button
        button_symbols=symbol.pop()


win.mainloop()
