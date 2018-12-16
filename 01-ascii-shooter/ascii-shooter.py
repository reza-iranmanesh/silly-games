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

aircraft_col = int(ROWS / 2)
aircraft_row = 1
enemy_col = int(ROWS / 2)
enemy_row = int(COLUMNS - 1)
canvas = [[EMPTY_FIELD for i in range(COLUMNS)] for j in range(ROWS)]
canvas[aircraft_col][aircraft_row] = AIRCRAFT
canvas[enemy_col][enemy_row] = ENEMY
bullets = []
enemy_slow_down_counter = 0


def start_the_game():
    time.sleep(0.03)

    # subprocess.call('clear', shell=True)
    print("%c[2J%c[;H" % (chr(27), chr(27)))

    move_enemy()
    won = move_bullet()
    draw(won)

    if won:
        print('YOU WIN!!!!!!!!')
        exit(0)


def draw(won=False):
    if won:
        canvas[enemy_col][enemy_row] = EXPLOSION
    for row in canvas:
        for item in row:
            print(item, end='')
        print('')
    print('', flush=True)


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
        if bullet[0] == enemy_col and bullet[1] == enemy_row:
            won = True
    return won


def move_enemy():
    global enemy_slow_down_counter
    enemy_slow_down_counter += 1
    if enemy_slow_down_counter % ENEMY_SLOW_DOWN_FACTOR != 0:
        return

    move_step = random.choice([-1, 1])
    global enemy_col
    global enemy_row
    canvas[enemy_col][enemy_row] = EMPTY_FIELD
    enemy_col = (enemy_col + move_step + ROWS) % ROWS
    canvas[enemy_col][enemy_row] = ENEMY


def fire():
    bullets.append([aircraft_col, aircraft_row + 1])


def go_down():
    global aircraft_col
    canvas[aircraft_col][aircraft_row] = EMPTY_FIELD
    aircraft_col = (aircraft_col + 1) % ROWS
    canvas[aircraft_col][aircraft_row] = AIRCRAFT


def go_up():
    global aircraft_col
    canvas[aircraft_col][aircraft_row] = EMPTY_FIELD
    aircraft_col = (aircraft_col - 1 + ROWS) % ROWS
    canvas[aircraft_col][aircraft_row] = AIRCRAFT


def read_key():
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


_thread.start_new_thread(read_key, ())
while True:
    start_the_game()
