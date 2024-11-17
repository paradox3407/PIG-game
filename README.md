# Pig Dice Game

Welcome to the **Pig Dice Game**! This is a simple two-player game based on the classic card game "Pig," where players roll dice to accumulate points, aiming to be the first to score 50 points without rolling a 1.

## How to Play

- The game alternates between two players: Player 1 and Player 2.
- On each turn, a player can:
  - **Roll the dice**: Type `'r'` to roll a six-sided die.
    - If you roll a number other than 1, that number is added to your temporary score for the turn.
    - If you roll a 1, you lose all points for the current turn, and your turn ends immediately.
  - **End your turn**: Type `'e'` to add your temporary score for the turn to your total score and pass the turn to the other player.
  - **Quit the game**: Type `'q'` to exit the game.

- The game ends when a player reaches or exceeds 50 points or when a player quits.

## Rules

1. The first player to score **50 or more points** wins the game.
2. Rolling a **1** results in losing all points accumulated during that turn, and the turn ends.
3. Players can choose to end their turn at any time to save their accumulated points.

## Setup

This game is implemented in Python. To play it, you need Python installed on your system.

### Running the Game

1. Clone or download the game code.
2. Open a terminal or command prompt and navigate to the folder containing the script.
3. Run the game using the following command:

   ```bash
   python pig_game.py

