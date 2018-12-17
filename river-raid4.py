#!/usr/bin/python
from tkinter import *
import time

AIRCRAFT_SPEED = 5


def keyup(e):
    print('up', e.char)


def keydown(e):
    print('down', e.char)
    if e.char == 'j':
        go_left()
    if e.char == 'l':
        go_right()


def go_left():
    c.move(oval, - AIRCRAFT_SPEED, 0)


def go_right():
    c.move(oval, AIRCRAFT_SPEED, 0)


def bind_keys(canvas):
    canvas.bind("<KeyPress>", keydown)
    canvas.bind("<KeyRelease>", keyup)
    canvas.pack()
    canvas.focus_set()


gui = Tk()
var = IntVar()
gui.geometry("800x800")
c = Canvas(gui, width=800, height=800)
c.pack()
oval = c.create_oval(5, 5, 60, 60, fill='blue')
a = 5
b = 5
bind_keys(c)

for x in range(0, 100):
    c.move(oval, a, b)
    gui.update()
    time.sleep(.01)
gui.title("First title")
gui.mainloop()

# root = Tk()
# frame = Frame(root, width=100, height=100)
