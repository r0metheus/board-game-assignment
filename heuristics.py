import numpy as np
from scipy.spatial import distance
from Players import RED_PLAYER, BLUE_PLAYER, other
import random

goals = {}
goals[BLUE_PLAYER] = (16, 6)
goals[RED_PLAYER] = (0, 6)
MAX = 30

RANDOM = 0
EUCLIDEAN = 1
V_DISPLACEMENT = 2
CLUSTERING = 3
EMPTY_GOAL = 4


def heuristic_value(kind):
    if kind == "EUCLIDEAN":
        return EUCLIDEAN
    if kind == "V_DISPLACEMENT":
        return V_DISPLACEMENT
    if kind == "CLUSTERING":
        return CLUSTERING
    if kind == "EMPTY_GOAL":
        return EMPTY_GOAL


def heuristic(board, player, kind):
    if kind == RANDOM:
        return random.randint(0, 200)
    if kind == EUCLIDEAN:
        return euclidean(board, player)
    if kind == V_DISPLACEMENT:
        return v_displacement(board, player)
    if kind == CLUSTERING:
        return clustering(board, player)
    if kind == EMPTY_GOAL:
        return empty_goal(board, player)


def euclidean(board, player):
    s = 0
    for index, value in np.ndenumerate(board):
        if value == player:
            s += MAX - (distance.euclidean(index, goals[player]))
    return round(s, 2)


def v_displacement(board, player):
    me = 0
    opponent = 0
    for index, value in np.ndenumerate(board):
        if value == player:
            me += MAX - distance.euclidean(index, goals[player])
        if value == other(player):
            opponent += MAX - distance.euclidean(index, goals[player])
    return round(me - opponent, 2)


def clustering(board, player):
    s = 0
    for index, value in np.ndenumerate(board):
        if value == player:
            s += MAX - distance.euclidean(index, goals[player])
            for jndex, value in np.ndenumerate(board):
                x = board[index[0], index[1]]
                y = board[jndex[0], jndex[1]]
                if((x == BLUE_PLAYER or x == RED_PLAYER) and x == y):
                    s += MAX - 0.1*distance.euclidean(index, jndex)
    return round(s, 2)


blue_player_home = [(0, 6), (1, 5), (1, 6), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7)]
red_player_home = [(16, 6), (15, 5), (15, 6), (14, 5), (14, 6), (14, 7), (13, 4), (13, 5), (13, 6), (13, 7)]


def empty_goal(board, player):
    goal = red_player_home.copy()
    if player == RED_PLAYER:
        goal = blue_player_home.copy()

    # remove already occupied positions
    to_remove = []
    for g in goal:
        if board[g[0]][g[1]] != 1:
            to_remove.append(g)
    for pos in to_remove:
        goal.remove(pos)

    if len(goal) == 0:
        if player == RED_PLAYER:
            next_goal = blue_player_home[0]
        if player == BLUE_PLAYER:
            next_goal = red_player_home[0]
    else:
        next_goal = goal[0]
    s = 0
    for index, value in np.ndenumerate(board):
        if value == player:
            s += MAX - abs(next_goal[0]-index[0]) - abs(next_goal[1]-index[1])
    return s
