from GameRules import valid_moves
from copy import deepcopy
import numpy as np
import time
from minimax import minimaxAlphaBeta
from Players import other, BLUE_PLAYER, RED_PLAYER, player_to_string
from statistics import mean
MAX_HISTORY = 5
from graphviz import Digraph
import uuid

class Agent:

    def __init__(self, player, depth, heur):
        self.name = player_to_string(player)
        self.player = player
        self.depth = depth
        self.heur = heur
        self.node_count = 0
        self.won = 0
        self.lost = 0
        self.gamemoves = 0
        self.history = []
        self.matchesmoveshistory = []
        self.movestiming = []

    def endgame(self, winner):
        self.history = []
        self.matchesmoveshistory.append(self.gamemoves)

        if self.player == winner:
            self.won += 1
        else:
            self.lost += 1

        #print("agent: "+self.name, ", won matches: "+str(self.won), ", lost matches: "+str(self.lost),
        #      ", match moves: "+str(self.gamemoves), ", avg moves: "+str(round(mean(self.matchesmoveshistory), 2)), ", avg time per move: "+str(round(mean(self.movestiming), 2)))

        self.gamemoves = 0

    def move(self, board):
        tic = time.perf_counter()
        self.node_count = 0
        root = Node(deepcopy(board), self.player, None, None)

        self.tree_build(root)

        #dot = Digraph(comment='Game Tree')
        #self.print_tree(root, None, None, dot)
        #print(dot.source)
        #dot.render('game-tree.gv', view=True)
        #exit(0)

        if self.node_count < 50:
            self.node_count = 0
            self.depth += 1
            root = Node(deepcopy(board), self.player, None, None)
            self.tree_build(root)

        index = minimaxAlphaBeta(root, self.depth, float("-inf"), float("inf"), True, None, self.player, self.heur)

        toc = time.perf_counter()
        print(f"Agent tree building and move took {toc - tic:0.4f} seconds")

        if len(self.history) == MAX_HISTORY:
            self.history.pop(0)

        self.history.append(index[1])

        self.gamemoves += 1
        self.movestiming.append(round(toc-tic, 2))

        #print(self.history)

        return index

    def print_tree(self, node, parent, name, dot, level=0):
        if level == 0:
            node_name = str(uuid.uuid4())
        else:
            node_name = name

        node_label = str((node.startPos, node.endPos, "MAX" if player_to_string(node.player) == "RED_PLAYER" else "MIN"))
        dot.node(name=node_name, label=node_label)

        for child in node.children:
            child_name = str(uuid.uuid4())
            self.print_tree(child, node, child_name, dot, level+1)
            dot.edge(node_name, child_name)

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
                #if (player == RED_PLAYER and dst[0]<=src[0]) or (player == BLUE_PLAYER and dst[0]>=src[0]):                # too strong constraint
                if (src, dst) not in self.history:                                                                          # this is preferable
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