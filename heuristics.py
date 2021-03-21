import numpy as np
from scipy.spatial import distance
from decimal import Decimal
from Players import RED_PLAYER, BLUE_PLAYER

# todo this is weird, player goal is also player base
goals = {}
goals[BLUE_PLAYER] = (16, 6)
goals[RED_PLAYER] = (0, 6)

def heuristic(board, player):
  sum = 0
  for index, value in np.ndenumerate(board):
    if value == player:
      sum = sum + distance.euclidean(index, goals[player])
  return round(sum, 2)