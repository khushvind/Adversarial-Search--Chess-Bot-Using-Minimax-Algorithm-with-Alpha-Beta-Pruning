# Adversarial Search: Chess Bot Using Minimax Algorithm with Alpha-Beta Pruning

This repository contains a basic chess bot that utilizes the Minimax strategy with Alpha-Beta Pruning to make optimal moves in a game of chess. It is designed to demonstrate how game-playing agents can be created using classic adversarial search algorithms.

## Files in the Repository

### 1. `simulation.py`
This file contains the simulation logic to run the chess game. It sets up the game environment, processes the moves, and simulates the interactions between the user and the chess bot.

### 2. `minimax.py`
The `minimax.py` file implements the Minimax algorithm with Alpha-Beta Pruning. This algorithm evaluates the game tree, assuming both the bot and the opponent play optimally. The pruning technique optimizes the search process by reducing the number of nodes evaluated in the tree.

### 3. `chess_bots.py`
This file defines two functions for different types of chess bots:
- `chess_bot_minimax`: A bot that makes moves based on the Minimax algorithm with Alpha-Beta pruning.
- `chess_bot_random`: A simple bot that picks moves randomly (useful for testing or comparison).

### 4. `Chessbot.ipynb`
This Jupyter Notebook demonstrates how to use the chess bot
- An interactive Jupyter Notebook demonstrating the capabilities of the chess bot.   
- Includes examples of simulations, bot-vs-bot and bot-vs-random bot matches


## Libraries Used
The project uses the following Python libraries:

- **`chess`**: A popular library for working with chess logic. It provides the necessary functions to represent chessboards, make moves, and validate the game's state.
- **`random`**: Used in the `chess_bot_random` function to make random moves, allowing the bot to act unpredictably for testing or comparison.
- **`IPython.display`**: To display SVG representations of the chessboard visually
- **`ipywidgets`**: A library for creating interactive widgets in Jupyter Notebooks. It is used in the notebook to add buttons and controls for user interaction

