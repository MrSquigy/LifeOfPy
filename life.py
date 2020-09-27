import argparse
import os
import random
import time
import sys

# Cell appearance
alive_cell = "#"
dead_cell = " "


def count_neighbours(board: list[list[int]], cell: tuple[int, int]) -> int:
    """Return the number of alive neighbours for a given cell."""

    neighbours = []
    alive_count = 0

    # Get co ords of all neighbours
    if cell[0] != 0:  # Not on the first row
        neighbours.append((cell[0] - 1, cell[1]))

        if cell[1] != 0:  # Not in the first column
            neighbours.append((cell[0] - 1, cell[1] - 1))

        if cell[1] != len(board[0]) - 1:  # Not in the last column
            neighbours.append((cell[0] - 1, cell[1] + 1))

    if cell[1] != 0:  # Not in the first column
        neighbours.append((cell[0], cell[1] - 1))

    if cell[0] != len(board) - 1:  # Not in the last row
        neighbours.append((cell[0] + 1, cell[1]))

        if cell[1] != len(board[0]) - 1:  # Not in the last column
            neighbours.append((cell[0] + 1, cell[1] + 1))

        if cell[1] != 0:  # Not in the first column
            neighbours.append((cell[0] + 1, cell[1] - 1))

    if cell[1] != len(board[0]) - 1:  # Not in the last column
        neighbours.append((cell[0], cell[1] + 1))

    # Count alive cells
    for cell in neighbours:
        if board[cell[0]][cell[1]] == 1:
            alive_count += 1

    return alive_count


def next_board_state(board: list[list[int]]) -> list[list[int]]:
    """Return the next board state given some state."""

    new_board = []
    for i, row in enumerate(board):
        new_board.append([])
        for n, cell in enumerate(row):
            num_neighbours = count_neighbours(board, (i, n))
            if cell == 1:  # Alive
                if num_neighbours <= 1:
                    new_board[i].append(0)  # Underpopulation
                elif 2 <= num_neighbours <= 3:
                    new_board[i].append(1)  # I will survive... hey hey
                elif num_neighbours > 3:
                    new_board[i].append(0)  # Overpopulation
            elif cell == 0:  # Dead
                if num_neighbours == 3:
                    new_board[i].append(1)  # Reproduction
                else:
                    new_board[i].append(0)

    return new_board


def render(board: list[list[int]]) -> None:
    """Render the game board to console."""

    os.system("cls") if os.name == "nt" else os.system("clear")
    border = "." + "-" * len(board[0]) + "."
    print(border)

    for row in board:
        cell_row = "|"
        for cell in row:
            cell_row += alive_cell if cell == 1 else dead_cell

        print(cell_row + "|")

    print(border)


def random_state(width: int, height: int, spawn_rate: float) -> list[list[int]]:
    """Return a random board state."""

    return [
        [1 if random.random() <= spawn_rate else 0 for _ in range(width)]
        for _ in range(height)
    ]


def load_state(file_name: str) -> list[list[int]]:
    """Load and return a saved game state from a file."""

    stored_state = []
    board = []

    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name) as f:
            stored_state = f.read().splitlines()
    else:
        print(f"Error: File '{file_name}' does not exist")
        sys.exit()

    for stored_row in stored_state:
        row = [int(cell) for cell in stored_row]
        board.append(row)

    return board


if __name__ == "__main__":
    random.seed()

    parser = argparse.ArgumentParser(description="Display the game of life.")
    parser.add_argument(
        "--w",
        "--width",
        dest="width",
        type=int,
        help="the width of the game world",
        default=100,
    )
    parser.add_argument(
        "--h",
        "--height",
        dest="height",
        type=int,
        help="the height of the game world",
        default=35,
    )
    parser.add_argument(
        "--r",
        "--rate",
        dest="spawn_rate",
        type=float,
        help="the rate at which cells spawn in the initial state",
        default=0.5,
    )
    parser.add_argument(
        "--l", "--load", dest="file_name", type=str, help="load a world from a file",
    )

    args = parser.parse_args()

    # Get initial board
    board: list[list[int]]
    if args.file_name is not None:
        board = load_state(args.file_name)
    else:
        board = random_state(args.width, args.height, args.spawn_rate)

    while True:
        render(board)
        time.sleep(0.8)
        board = next_board_state(board)

