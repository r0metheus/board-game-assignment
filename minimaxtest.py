from GameBoard import GameBoard
from minimax import minimaxAlphaBeta, minimax

class Node:
    def __init__(self, board, player, value, move):
        self.state = board
        self.value = value
        self.player = player
        self.startPos = value
        self.endPos = value
        self.children = []

    def get_board(self):
        return self.state

    def add_children(self, node):
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0

board = GameBoard()

root = Node(board, 1, float("-inf"), "a")
b=Node(board,2,2,"b")
c=Node(board,2,1,"c")
d=Node(board,1,3,"d")
e=Node(board,1,4,"e")
f=Node(board,1,0,"f")
g=Node(board,1,1,"g")
h = Node(board,2,1,"h")

d.add_children(h)
b.add_children(d)
b.add_children(e)
c.add_children(f)
c.add_children(g)
root.add_children(b)
root.add_children(c)

print(
    minimax(root, 2, True, None, None, ))
print(minimaxAlphaBeta(root,2,float("-inf"),float("inf"), True, None))