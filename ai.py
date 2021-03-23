from GameRules import valid_moves
from copy import deepcopy
import numpy as np
import time
from minimax import minimaxAlphaBeta
from Players import other, BLUE_PLAYER, RED_PLAYER

class Agent:

    def __init__(self, player, depth, heur):
        self.name = str(player)
        self.player = player
        self.depth = depth
        self.heur = heur
        self.node_count = 0

    def move(self, board):
        tic = time.perf_counter()
        self.node_count = 0
        root = Node(deepcopy(board), self.player, None, None)

        self.tree_build(root)

        #print("Three of player: "+self.name)
        #self.printTree(root)
        if self.node_count < 50:
            self.node_count = 0
            self.depth += 1
            print("Increment depth to " + str(self.depth))
            root = Node(deepcopy(board), self.player, None, None)
            self.tree_build(root)
            self.printTree(root)
        index = minimaxAlphaBeta(root, self.depth, float("-inf"), float("inf"), True, None, self.player, self.heur)

        toc = time.perf_counter()
        print(f"Agent tree building and move took {toc - tic:0.4f} seconds")

        return index

    def printTree(self, node, level = 0):
        print("Depth: "+str(level), (node.startPos, node.endPos, node.player))
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
        if depth == self.depth + 1:
            return

        if depth%2 != 0:
            player = self.player
        else:
            player = other(self.player)

        my_marbles_positions = self.positions(node.state.get_board(), player)

        for src in my_marbles_positions:
            v_dst = valid_moves(node.state.get_board(), src, player)

            for dst in v_dst:
                if (player == RED_PLAYER and dst[0]<=src[0]) or (player == BLUE_PLAYER and dst[0]>=src[0]):
                    node.add_child(self.node_create(node, player, src, dst))
                    self.node_count += 1

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