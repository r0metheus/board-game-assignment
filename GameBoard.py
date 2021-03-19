from GameRules import valid_moves
from Players import PLAYER_2, PLAYER_1
import numpy as np

class GameBoard:
    def __init__(self):
        self.board = self.build_board()

    def build_board(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
        #setup players
        #player AI
        board[0][6] = PLAYER_2
        board[1][5] = PLAYER_2
        board[1][6] = PLAYER_2
        board[2][5] = PLAYER_2
        board[2][6] = PLAYER_2
        board[2][7] = PLAYER_2
        board[3][4] = PLAYER_2
        board[3][5] = PLAYER_2
        board[3][6] = PLAYER_2
        board[3][7] = PLAYER_2


        #player A
        board[16][6] = PLAYER_1
        board[15][5] = PLAYER_1
        board[15][6] = PLAYER_1
        board[14][5] = PLAYER_1
        board[14][6] = PLAYER_1
        board[14][7] = PLAYER_1
        board[13][4] = PLAYER_1
        board[13][5] = PLAYER_1
        board[13][6] = PLAYER_1
        board[13][7] = PLAYER_1

        return board

    def print_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                print(self.board[row][col], end=" ")
            print("\n")

    def move(self, src, dest, player):
        if self.board[dest[0]][dest[1]] == 0 or self.board[src[0]][src[1]] == 0:
            return False
        if self.board[src[0]][src[1]] == 1:
            return False
        if dest not in valid_moves(self.board, src, player):
            return False
        self.board[dest[0]][dest[1]], self.board[src[0]][src[1]] = self.board[src[0]][src[1]], self.board[dest[0]][dest[1]]
        return True

    def get_board(self):
        return self.board

    def clear_hints(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == -1:
                    self.board[row][col] = 1
