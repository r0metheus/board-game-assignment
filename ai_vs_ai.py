from pygame.constants import CONTROLLER_BUTTON_START
from GameRules import check_win, is_pebble, valid_moves
from Players import RED_PLAYER, BLUE_PLAYER, player_to_string
from GameBoard import GameBoard
import pygame
from Cell import Cell
import pygame
import sys
from ai import Agent
from heuristics import CLUSTERING, RANDOM, EUCLIDEAN, V_DISPLACEMENT, EMPTY_GOAL

BACKGROUND_COLOR = [250, 237, 192]

WIDTH = 700
HEIGHT = 700
RADIUS = 20
V_OFF = 50
H_OFF = 110
pygame.init()
pygame.display.set_caption('Chinese Checkers AI')
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(BACKGROUND_COLOR)

board = GameBoard()
# board.print_board()

hint_board = board.get_board().copy()

done = False

clock = pygame.time.Clock()

coll_rects = []


def create_coll(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 0:
                y = row * 34 + V_OFF
                if row % 2 == 0:
                    x = col * 40 + H_OFF
                else:
                    x = col * 40 + H_OFF + RADIUS
                x_rect = x - RADIUS // 2
                y_rect = y - RADIUS // 2
                coll_rects.append(Cell(row, col, x_rect, y_rect, RADIUS))


def clear_hints(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == -1:
                board[row][col] = 1


def draw_board(board, hints):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 0:
                y = row * 34 + V_OFF
                if row % 2 == 0:
                    x = col * 40 + H_OFF
                else:
                    x = col * 40 + H_OFF + RADIUS

                if board[row][col] == 1:
                    pygame.draw.circle(screen, [0, 0, 0], (x, y), RADIUS, width=1)
                elif board[row][col] == RED_PLAYER:
                    pygame.draw.circle(screen, [255, 0, 0], (x, y), RADIUS, width=0)
                elif board[row][col] == BLUE_PLAYER:
                    pygame.draw.circle(screen, [0, 0, 255], (x, y), RADIUS, width=0)

    for row in range(len(hints)):
        for col in range(len(hints[0])):
            if hints[row][col] == -1:
                y = row * 34 + V_OFF
                if row % 2 == 0:
                    x = col * 40 + H_OFF
                else:
                    x = col * 40 + H_OFF + RADIUS
                pygame.draw.circle(screen, (249, 215, 28, 127), (x, y), RADIUS, width=0)


create_coll(board.get_board())
selected = None

# CLUSTERING, RANDOM, EUCLIDEAN, V_DISPLACEMENT, EMPTY_GOAL
DEPTH = 2

agent_1 = Agent(RED_PLAYER, DEPTH, EUCLIDEAN)
agent_2 = Agent(BLUE_PLAYER, DEPTH, EMPTY_GOAL)

turn = RED_PLAYER
print(player_to_string(turn) + " begins the match")

# game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

    if turn == BLUE_PLAYER:
        results_2 = agent_2.move(board)
        print("BLUE_PLAYER: "+str(results_2[1]))
        board.move(results_2[1][0], results_2[1][1], BLUE_PLAYER)
        turn = RED_PLAYER
    elif turn == RED_PLAYER:
        results_1 = agent_1.move(board)
        print("RED_PLAYER: "+str(results_1[1]))
        board.move(results_1[1][0], results_1[1][1], RED_PLAYER)
        turn = BLUE_PLAYER

    winner = check_win(board.get_board())
    if winner != False:
        agent_1.endgame(winner)
        agent_2.endgame(winner)

        done = True

    screen.fill(BACKGROUND_COLOR)
    draw_board(board.get_board(), hint_board)
    pygame.display.update()

    clock.tick(60)
