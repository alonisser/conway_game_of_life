# Conway game of life

You can read about it [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Dilemma

How should we handle "edge of the board cells"? The original rules handle the board as "infinite" but computers are not really infinite
and an "auto growing" board would make implementation a bit more complex so for now we'll handle "out of board" cells boarding
the "edge of board" cells as "dead"

## Future considerations

* Using sparse representation of the board

## Follow the process

* Developed by TDD, see different steps with git tags v1 => v9

## What's next

1. Implement a UI using curses or something else
2. User input
3. Discovering patterns

## Tech:
* python 3 + curses lib
* pytest for testing



## Install
```bash
# Preferably in a virtualenv
pip install requirements.txt
```
