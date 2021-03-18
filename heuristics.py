import numpy as np
from scipy.spatial import distance
from decimal import Decimal
from Players import PLAYERA, AI

goal = PLAYERA
available_goals = [[16, 6], [15, 5], [15, 6], [14, 5], [14, 6], [14, 7], [13, 4], [13, 5], [13, 6], [13, 7]]

def manhattan(a, b):
  mean = 0
  for goal in b:
    mean = mean + distance.euclidean(a, goal)
  return mean/len(b)

def heuristic(board):
  sum = 0
  for index, value in np.ndenumerate(board):
    if value == goal:
      sum = sum + manhattan(index, available_goals)
  return round(sum, 2)