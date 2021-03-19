import numpy as np
from scipy.spatial import distance
from decimal import Decimal
from Players import PLAYERA, AI

player_goal = PLAYERA
goal = (16, 6)

def manhattan(a, b):
  mean = 0
  for goal in b:
    mean = mean + distance.euclidean(a, goal)
  return mean/len(b)

def heuristic(board):
  sum = 0
  for index, value in np.ndenumerate(board):
    if value == player_goal:
      sum = sum + distance.euclidean(index, goal)     # manhattan(index, goal)
  return round(sum, 2)