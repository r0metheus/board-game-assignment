import numpy as np
from scipy.spatial import distance
from decimal import Decimal
from Players import PLAYER_1, PLAYER_2

def heuristic(board, player):
  if player == PLAYER_1:
    goal = (16, 6)
  if player == PLAYER_2:
    goal = (0, 6)

  sum = 0
  for index, value in np.ndenumerate(board):
    if value == player:
      sum = sum + distance.euclidean(index, goal)
  return round(sum, 2)