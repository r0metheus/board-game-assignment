from pygame.constants import CONTROLLER_BUTTON_START
from GameRules import check_win, valid_moves
from Players import PLAYERA, AI
from GameBoard import GameBoard
import pygame
from Cell import Cell
import pygame
import random
import sys

BACKGROUND_COLOR = [250, 237, 192]

WIDTH = 700
HEIGHT = 700
RADIUS = 20
V_OFF = 50
H_OFF = 110
pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(BACKGROUND_COLOR)


board = GameBoard()
board.print_board()

hint_board = board.get_board().copy()

done = False

clock = pygame.time.Clock()

coll_rects = []

turn = PLAYERA

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
                # if row % 2 == 0:
                #     pygame.draw.circle(screen, [0,255,0], (x, y), RADIUS, width=0)
                # else:
                #     pygame.draw.circle(screen, [255,0,0], (x, y), RADIUS, width=1)
                if board[row][col] == 1:
                    pygame.draw.circle(screen, [0,0,0], (x, y), RADIUS, width=1)
                elif board[row][col] == PLAYERA:
                    pygame.draw.circle(screen, [255,0,0], (x, y), RADIUS, width=0)
                elif board[row][col] == AI:
                    pygame.draw.circle(screen, [0,0,255], (x, y), RADIUS, width=0)
                
    for row in range(len(hints)):
        for col in range(len(hints[0])):
            if hints[row][col] == -1:
                y = row * 34 + V_OFF
                if row % 2 == 0:
                    x = col * 40 + H_OFF
                else:
                    x = col * 40 + H_OFF + RADIUS
                pygame.draw.circle(screen, (249,215,28, 127), (x, y), RADIUS, width=0)

create_coll(board.get_board())
selected = None 
ai_pos = [(0,6), (1,5), (1,6), (2,5), (2,6), (2,7), (3,4), (3,5), (3,6), (3,7)]

#game loop
while not done:
    if turn == AI:
        random_idx = random.randint(0, 9)
        available_moves = valid_moves(board.get_board(), ai_pos[random_idx], AI)
        while len(available_moves) == 0:
            random_idx = random.randint(0, 9)
            available_moves = valid_moves(board.get_board(), ai_pos[random_idx], AI)

        selected_move_ai = random.choice(available_moves)
        board.move(ai_pos[random_idx], selected_move_ai, AI)
        ai_pos.remove(ai_pos[random_idx])
        ai_pos.append(selected_move_ai)
        turn = PLAYERA
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and turn == PLAYERA:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rect2 = pygame.Rect(mouse_x, mouse_y, RADIUS//2, RADIUS//2)
            for c in coll_rects:
                if c.rect.collidepoint(mouse_x, mouse_y):
                    print("Mouse collided with " + str(c.get_row_col()))
                    clear_hints(hint_board)
                    if selected is None:
                        hints = valid_moves(board.get_board(), c.get_row_col(), PLAYERA)
                        print("Hints: " + str(hints))
                        for hint in hints:
                            if board.get_board()[hint[0]][hint[1]] == 1:
                                hint_board[hint[0]][hint[1]] = -1
                        selected = c.get_row_col()
                        print("selected " + str(selected))
                    else:
                        if selected == c.get_row_col():
                            selected = None
                            print("Reset selected")
                        else:
                            if board.move(selected, c.get_row_col(), PLAYERA):
                                turn = AI
                                print("Move and reset selected")
                            selected = None
                    break
    winner = check_win(board.get_board())
    if winner != False:
        print("The winner is " + str(winner))
        done = True
    screen.fill(BACKGROUND_COLOR)
    draw_board(board.get_board(), hint_board)
    pygame.display.update()

    clock.tick(60)