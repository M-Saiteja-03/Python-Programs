from tkinter import *

window = Tk()
window.minsize(400, 400)


def click_a():
    a['bg'] = 'red'


def click_b():
    b['bg'] = 'blue'


def click_c():
    c['bg'] = 'green'


def click_d():
    d['bg'] = 'yellow'


a = Button(command=click_a, width=27, height=13)
a.grid(row=0, column=0)
b = Button(command=click_b, width=27, height=13)
b.grid(row=0, column=1)
c = Button(command=click_c, width=27, height=13)
c.grid(row=1, column=0)
d = Button(command=click_d, width=27, height=13)
d.grid(row=1, column=1)
window.mainloop()