import random
from GameRules import valid_moves
from copy import deepcopy
from Players import PLAYERA, AI
import numpy as np
import time
from GameBoard import GameBoard
from minimax import minimax, minimaxAlphaBeta

max_depth = 3

class Agent:

    def __init__(self):
        self.name = "Agent Smith " + str(random.randint(100, 200))
        #self.root = Node(deepcopy(board), AI, None, None)

        #tic = time.perf_counter()
        #self.tree_build(self.root)
        #toc = time.perf_counter()
        #print(f"Tree built in {toc - tic:0.4f} seconds")

        #tic = time.perf_counter()
        #print(minimax(self.root, max_depth - 1, True, None))
        #toc = time.perf_counter()
        #print(f"Minimax returned in {toc - tic:0.4f} seconds")

        #tic = time.perf_counter()
        #print(minimaxAlphaBeta(self.root, max_depth - 1, float("-inf"), float("inf"), True, None))
        #toc = time.perf_counter()
        #print(f"Minimax w/ alpha-beta pruning returned in {toc - tic:0.4f} seconds")

    def move(self, board):
        tic = time.perf_counter()
        root = Node(deepcopy(board), AI, None, None)
        self.tree_build(root)
        index = minimaxAlphaBeta(root, max_depth - 1, float("-inf"), float("inf"), True, None)

        toc = time.perf_counter()
        print(f"Agent move took {toc - tic:0.4f} seconds")
        return index

    def printTree(self, node, level = 0):
        print(level*2*' ', (node.startPos, node.endPos, node.player))
        for child in node.children:
            self.printTree(child, level + 1)

    def node_create(self, parent, player, src, dst):
        new_board = deepcopy(parent.state)
        new_board.move(src, dst, player)

        return Node(new_board, player, src, dst)

    def positions(self, board, player):
        pos = []
        for index, value in np.ndenumerate(board):
            if value == player:
                pos.append(index)
        return pos

    def tree_build(self, node, depth = 1):
        self.subtree_build(node, depth)
        for child in node.children:
            self.tree_build(child, depth+1)

    def subtree_build(self, node, depth):
        if depth == max_depth:
            return

        if depth % 2 == 0:
            player = AI
        else:
            player = PLAYERA

        my_marbles_positions = self.positions(node.state.get_board(), player)

        for src in my_marbles_positions:
            v_moves = valid_moves(node.state.get_board(), src, player)

            for dst in v_moves:
                node.add_child(self.node_create(node, player, src, dst))

class Node:
    def __init__(self, board, player, start, end):
        self.state = board
        self.player = player
        self.startPos = start
        self.endPos = end
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0