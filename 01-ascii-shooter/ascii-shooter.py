#!/usr/bin/python
import _thread
import random
import time
import tty
import sys

COLUMNS = 50
ROWS = 10
ENEMY_SLOW_DOWN_FACTOR = 10

AIRCRAFT = '}'
ENEMY = 'X'
EXPLOSION = '*'
BULLET = '.'
EMPTY_FIELD = ' '
aircraft_x = int(ROWS / 2)
aircraft_y = 1

enemy_x = int(ROWS / 2)
enemy_y = int(COLUMNS - 1)

bullets = []

canvas = [[EMPTY_FIELD for i in range(COLUMNS)] for j in range(ROWS)]
canvas[aircraft_x][aircraft_y] = AIRCRAFT
canvas[enemy_x][enemy_y] = ENEMY

enemy_slow_down_counter = 0


def draw():
    global ENEMY
    time.sleep(0.03)

    # subprocess.call('clear', shell=True)
    print("%c[2J%c[;H" % (chr(27), chr(27)))

    move_enemy()
    won = move_bullet()
    if won:
        canvas[enemy_x][enemy_y] = EXPLOSION

    for row in canvas:
        for item in row:
            print(item, end='')
        print('')
    print('', flush=True)

    if won:
        print('YOU WIN!!!!!!!!')
        exit(0)


def move_bullet():
    won = False
    for counter, bullet in enumerate(bullets):
        if bullet[1] == COLUMNS:
            pass
        else:
            canvas[bullet[0]][bullet[1]] = EMPTY_FIELD
            bullet[1] += 1
            if bullet[1] != COLUMNS:
                canvas[bullet[0]][bullet[1]] = BULLET
        if bullet[0] == enemy_x and bullet[1] == enemy_y:
            won = True
    return won


def move_enemy():
    global enemy_slow_down_counter
    enemy_slow_down_counter += 1
    if enemy_slow_down_counter % ENEMY_SLOW_DOWN_FACTOR != 0:
        return

    move_step = random.choice([-1, 1])
    global enemy_x
    global enemy_y
    canvas[enemy_x][enemy_y] = EMPTY_FIELD
    enemy_x = (enemy_x + move_step + ROWS) % ROWS
    canvas[enemy_x][enemy_y] = ENEMY


def fire():
    bullets.append([aircraft_x, aircraft_y + 1])


def go_down():
    global aircraft_x
    canvas[aircraft_x][aircraft_y] = EMPTY_FIELD
    aircraft_x = (aircraft_x + 1) % ROWS
    canvas[aircraft_x][aircraft_y] = AIRCRAFT


def go_up():
    global aircraft_x
    canvas[aircraft_x][aircraft_y] = EMPTY_FIELD
    aircraft_x = (aircraft_x - 1 + ROWS) % ROWS
    canvas[aircraft_x][aircraft_y] = AIRCRAFT


def _key_detect():
    while True:
        print("")
        ch = getch()
        if ch == 'i':
            go_up()
        elif ch == 'k':
            go_down()
        elif ch == ' ':
            fire()
        elif ch == 'q':
            exit(0)


def getch():
    tty.setcbreak(sys.stdin)
    key = sys.stdin.read(1)  # key captures the key-code
    return key


_thread.start_new_thread(_key_detect, ())
while True:
    draw()

