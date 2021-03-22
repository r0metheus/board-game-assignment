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
      for jndex,value in np.ndenumerate(board):
        x=board[index[0],index[1]]
        y=board[jndex[0],jndex[1]]
        if((x==BLUE_PLAYER or x==RED_PLAYER) and x==y):
          sum = sum+0.1*distance.euclidean(index,jndex)
  return round(sum, 2)