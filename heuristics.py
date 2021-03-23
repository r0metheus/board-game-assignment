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

def heuristic(board, player, kind):
  if kind == RANDOM:
    return random.randint(0, 200)
  if kind == EUCLIDEAN:
    return euclidean(board, player)
  if kind == V_DISPLACEMENT:
    return v_displacement(board, player)
  if kind == CLUSTERING:
    return clustering(board, player)

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
        if((x == BLUE_PLAYER or x == RED_PLAYER) and x==y):
          s += MAX - 0.1*distance.euclidean(index, jndex)
  return round(s, 2)