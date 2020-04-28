import time
from curses import wrapper

import numpy as np

from generation import generate_random_generation, resolve_next_generation


def play_life(stdscr, new_generation):
    rounds = 1
    stdscr.clear()
    title = build_title(new_generation, rounds)
    board_str = np.array2string(new_generation)
    stdscr.addstr(title + board_str)
    is_alive = True

    while is_alive:
        time.sleep(2)
        new_generation = resolve_next_generation(new_generation)
        title = build_title(new_generation, rounds)
        stdscr.clear()
        stdscr.refresh()
        board_str = np.array2string(new_generation)
        stdscr.addstr(title + board_str)

        stdscr.refresh()
        is_alive = new_generation.sum() > 0
        rounds = rounds + 1
    stdscr.addstr("Game over, everything that has a beginning has an end you've played %s rounds" % rounds)
    stdscr.refresh()


def build_title(new_generation, rounds):
    return 'New generation live cells: %s round: %s \n' % (new_generation.sum(), rounds)


if __name__ == "__main__":
    x_size = input("What is the x size of the board: ")
    y_size = input("What is the y size of the board: ")
    number_of_live_cells = input("What is the expected number of live cells: ")

    x_size = int(x_size)
    y_size = int(y_size)
    number_of_live_cells = int(number_of_live_cells)
    if number_of_live_cells > x_size * y_size or number_of_live_cells < 0:
        print("Number of live cells is illegal, should be a positive number smaller or equal to the board size")
        exit(1)
    initial_generation = generate_random_generation(x_size, y_size, number_of_live_cells)
    wrapper(func=play_life, new_generation=initial_generation)
