import random
from heuristics import heuristics

class Agent:
    def __init__(self):
        self.name = self.spawn()
    
    def spawn(self):
        return "Agent Smith " + str(random.randint(100, 200))

    def turn(self, board):
        # print("I see this board")
        board.print_board()