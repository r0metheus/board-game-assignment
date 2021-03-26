# Chinese Checkers AI - Group 33

Team:
* Claus Lønkjær - s160108
* Leonardo Zecchin - s203509
* Francesco Romeo - s210222
* Nicolò Sponziello - s210226

## Install instructions
The project is build using Python and some additional libraries:
* Pygame
* Numpy
* Scipy

To install all the dependencies:
```
pip install -r requirements.txt
```

## Project structure
The project is split into different files that can be divided into 2 main areas:
* game: files that contain the implementation of the game
* ai: files that contains the implementation of the AI

### Game implementation
The game implementation is contained into the following modules:
* Cell: class that describe a cell of the board
* GameBoard: class that abstract the board of the game and allow to interact with it
* GameRules: implementation of all the rules for the game
* Players: contain players declaration and utility functions

### AI implementation
The AI implementation is contained in the files:
* ai: class implementation of the agent that interact with the game
* minimax: implementation of the minimax algorithm

## Run instructions
The game can be run in two different configuration:
* ai_vs_ai: two ai play against each other
* ai_vs_human: an ai plays againt the human player

To start the game run the command:
```
python3 ai_vs_ai.py
```
or 
```
python3 ai_vs_human.py
```