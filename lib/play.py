import curses
import time

import numpy as np

from generation import resolve_next_generation


def play_life(stdscr, new_generation):
    rounds = 1
    stdscr.clear()
    title = build_title(new_generation, rounds)
    board_str = np.array2string(new_generation)
    stdscr.addstr(title + board_str)
    is_alive = True

    while is_alive:
        time.sleep(1)
        new_generation = resolve_next_generation(new_generation)
        title = build_title(new_generation, rounds)
        stdscr.clear()
        stdscr.refresh()
        board_str = np.array2string(new_generation)
        stdscr.addstr(title + board_str)

        stdscr.refresh()
        is_alive = new_generation.sum() > 0
        rounds = rounds + 1
    stdscr.addstr("\n Game over, everything that has a beginning has an end. You've played %s rounds" % rounds,
                  curses.A_BLINK)
    stdscr.refresh()

    stdscr.addstr("\n \n Exit with any key", curses.A_BOLD)
    stdscr.getch()


def build_title(new_generation, rounds):
    return 'New generation live cells: %s round: %s \n' % (new_generation.sum(), rounds)



