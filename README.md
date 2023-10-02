# Project Description: Tic Tac Toe Game

## Overview

This project involves the development of a classic Tic Tac Toe game using Python and the PyQt5 library for the graphical user interface (GUI). The game is designed for two players and features a 3x3 grid where players take turns to place their symbols (X or O) in an attempt to win the game. The project consists of several modules to handle game logic, GUI, and end-game messages.

## Key Features

### Game Logic (algorithm.py)

- **Tic Tac Toe Class**: The `tic_tac_toe` class is responsible for managing the game's state and logic. It includes methods for checking the game's status, making moves, and printing the game grid.

### Graphical User Interface (GUI)

#### Game Grid (gui.py)

- **Grid Layout**: The GUI presents a 3x3 grid of buttons representing the game board.
- **Symbols**: Players can click on buttons to place their symbols (X or O) on the grid.
- **Font**: The buttons use a large font size for clear symbol display.

#### End Game Message (endgamegui.py)

- **Message Display**: This module provides a message display area to show the game outcome, such as who won or if it's a tie.
- **Font**: Large font size for clear message presentation.

### Main Application (main.py)

- **GUI Integration**: The main application integrates the game grid and end game message display using a `QStackedWidget`.
- **Window Setup**: It sets up the main window, sets its size, and specifies the window title.

## Implementation

The game logic is encapsulated in the `tic_tac_toe` class within the `algorithm.py` module. The graphical user interface is created using PyQt5 in two parts: the game grid (gui.py) and the end game message display (endgamegui.py). The main application (main.py) handles GUI integration and player interaction.

## How to Play

1. Run the application (main.py).
2. Players take turns clicking on the grid buttons to place their symbols (X or O).
3. The game checks for a win or tie condition.
4. If a player wins or it's a tie, the end game message is displayed.
5. Players can restart the game from the end game message screen.

## Conclusion

The Tic Tac Toe game project provides an interactive and enjoyable gaming experience for two players. It serves as an educational project for Python GUI development with PyQt5 and reinforces fundamental programming concepts like game logic and user interface design.
