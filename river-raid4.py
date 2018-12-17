#!/usr/bin/python
import _thread
from tkinter import *
import time

AIRCRAFT_SPEED = 20

gui = Tk()
var = IntVar()
gui.geometry("800x800")
canvas = Canvas(gui, width=800, height=800)
canvas.pack()
aircraft = canvas.create_rectangle(700, 700, 720, 702, fill='blue')

def keyup(e):
    print('up', e.char)


def move_keys_down(e):
    print('down', e.char)
    if e.char == 'j':
        go_left()
    if e.char == 'l':
        go_right()
    if e.char == ' ':
        # _thread.start_new_thread(fire_bullet, ())
        fire_bullet()

def fire_bullet():
    print("fire bullet!")
    bullet_width = 2
    bullet_height = 6
    aircraft_pos = canvas.coords(aircraft)
    bullet_x_start = aircraft_pos[0] + ((aircraft_pos[2] - aircraft_pos[0]) / 2) - bullet_width / 2
    bullet_x_end = bullet_x_start + bullet_width
    bullet_y_start = aircraft_pos[3]
    bullet_y_end = aircraft_pos[3] + bullet_height
    print ("[%s, %s] and [%s, %s]" % (bullet_x_start, bullet_y_start, bullet_x_end, bullet_y_end))
    bullet = canvas.create_rectangle(bullet_x_start, bullet_y_start, bullet_x_end, bullet_y_end, fill='red')
    for i in range(1000):
        # _thread.start_new_thread(canvas.move, (bullet, 0, -18))
        canvas.move(bullet, 0, -18)
        gui.update()


def go_left():
    canvas.move(aircraft, - AIRCRAFT_SPEED, 0)


def go_right():
    canvas.move(aircraft, AIRCRAFT_SPEED, 0)


def bind_keys(canvas):
    canvas.bind("<KeyPress>", move_keys_down)
    canvas.bind("<KeyRelease>", keyup)
    # canvas.pack()
    canvas.focus_set()


bind_keys(canvas)
gui.mainloop()

# root = Tk()
# frame = Frame(root, width=100, height=100)




# import tkinter as tk      # for python 2, replace with import Tkinter as tk
# import random
#
#
# class Ball:
#
#     def __init__(self):
#         self.xpos = random.randint(0, 254)
#         self.ypos = random.randint(0, 310)
#         self.xspeed = random.randint(1, 5)
#         self.yspeed = random.randint(1, 5)
#
#
# class MyCanvas(tk.Canvas):
#
#     def __init__(self, master):
#
#         super().__init__(master, width=254, height=310, bg="snow2", bd=0, highlightthickness=0, relief="ridge")
#         self.pack()
#
#         self.balls = []   # keeps track of Ball objects
#         self.bs = []      # keeps track of Ball objects representation on the Canvas
#         for _ in range(25):
#             ball = Ball()
#             self.balls.append(ball)
#             self.bs.append(self.create_oval(ball.xpos - 10, ball.ypos - 10, ball.xpos + 10, ball.ypos + 10, fill="saddle brown"))
#         self.run()
#
#     def run(self):
#         for b, ball in zip(self.bs, self.balls):
#             self.move(b, ball.xspeed, ball.yspeed)
#             pos = self.coords(b)
#             if pos[3] >= 310 or pos[1] <= 0:
#                 ball.yspeed = - ball.yspeed
#             if pos[2] >= 254 or pos[0] <= 0:
#                 ball.xspeed = - ball.xspeed
#         self.after(100, self.run)
#
#
# if __name__ == '__main__':
#
#     shop_window = tk.Tk()
#     shop_window.geometry("254x310")
#     c = MyCanvas(shop_window)
#
#     shop_window.mainloop()
