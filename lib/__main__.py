from curses import wrapper

from generation import generate_random_generation
from play import play_life

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
