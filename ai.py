import random
from GameRules import valid_moves
from heuristics import heuristic as h
from Players import PLAYERA, AI

class Agent:
    depth = 5   # review
    
    def __init__(self, board):
        self.name = "Agent Smith " + str(random.randint(100, 200))
        self.root = Node(board, PLAYERA)

    def turn(self, board):
        print("from the main")
        
    def tree_build(self):
        print("tree building")

class Node:
    def __init__(self, board, player):
        self.state = board
        self.value = self.evaluation()
        self.player = player
        self.children = []

    def evaluation(self):
        return h(self.state.get_board())

    def get_board(self):
        return self.state

    def add_children(self, node):
        self.children.append(node)
    
    def is_leaf(self):
        return len(self.children) == 0

