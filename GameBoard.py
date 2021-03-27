from GameRules import valid_moves
from Players import BLUE_PLAYER, RED_PLAYER
import numpy as np


class GameBoard:
    def __init__(self):
        # Must be changed to self.randomize_board() for random starting positions
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
        # setup players
        # player AI
        board[0][6] = BLUE_PLAYER
        board[1][5] = BLUE_PLAYER
        board[1][6] = BLUE_PLAYER
        board[2][5] = BLUE_PLAYER
        board[2][6] = BLUE_PLAYER
        board[2][7] = BLUE_PLAYER
        board[3][4] = BLUE_PLAYER
        board[3][5] = BLUE_PLAYER
        board[3][6] = BLUE_PLAYER
        board[3][7] = BLUE_PLAYER

        # player A
        board[16][6] = RED_PLAYER
        board[15][5] = RED_PLAYER
        board[15][6] = RED_PLAYER
        board[14][5] = RED_PLAYER
        board[14][6] = RED_PLAYER
        board[14][7] = RED_PLAYER
        board[13][4] = RED_PLAYER
        board[13][5] = RED_PLAYER
        board[13][6] = RED_PLAYER
        board[13][7] = RED_PLAYER

        return board

    def randomize_board(self):
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

        pieces_array = np.array([BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER, BLUE_PLAYER,
                                 BLUE_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER, RED_PLAYER])
        positions_list = np.empty((0, 2), int)
        for row in range(0, 13):
            for column in range(0, 16):
                if board[column][row] == 1:
                    pos = np.array([[column, row]])
                    positions_list = np.append(positions_list, pos, axis=0)
                else:
                    continue
        chosen_indexes = np.random.choice(len(positions_list), size=len(pieces_array), replace=False)

        # Place pieces on the board according to the chosen indexes
        for piece in range(0, 20):
            column = positions_list[chosen_indexes[piece]][0]
            row = positions_list[chosen_indexes[piece]][1]
            board[column][row] = pieces_array[piece]

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
