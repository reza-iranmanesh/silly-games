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
enemy = canvas.create_rectangle(300, 50, 320, 60, fill='green')
bullets = []

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
    move_bullet(bullet)

def move_bullet(bullet, start=0):
    print("start is: [%s]" % start)
    global enemy
    speed = 18
    if start > 1000:
        return
    canvas.move(bullet, 0, - speed)
    bullet_coords = canvas.coords(bullet)
    if enemy:
        enemy_coords = canvas.coords(enemy)
        if enemy_coords[3] > bullet_coords[1] and \
                (
                        enemy_coords[0] < bullet_coords[0] < enemy_coords[2] or
                        enemy_coords[0] < bullet_coords[2] < enemy_coords[2]
                ):
            canvas.delete(enemy)
            canvas.delete(bullet)
            enemy = None
            return
            pass
    gui.after(1, move_bullet, bullet, start + speed)

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

