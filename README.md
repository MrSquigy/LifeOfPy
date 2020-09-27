# Life of Py
![python 3.9](https://img.shields.io/badge/python-3.9-blue)

[Conway's game of life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) implemented in Python. There are some examples of organisms in the examples dir, all of which were taken from [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns).

## Usage
The default usage is `python life.py`, which simulates a random 100 x 35 world, with a spawn rate of 50%. You can specify each of these parameters using flags.

| Flag              | Description                                                                  |
| ----------------- | ---------------------------------------------------------------------------- |
| `--w`, `--width`  | Specify the width of the game world                                          |
| `--h`, `--height` | Specify the height of the game world                                         |
| `--r`, `--rate`   | Specify the spawn rate of cells <br> **Note:** This value is between 0 and 1 |
| `--l`, `--load`   | Load a game world from a file                                                |