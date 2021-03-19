from heuristics import heuristic

def minimax(node, depth, maximizingPlayer, move, player):
  if (depth == 0):
    return heuristic(node.state.get_board(), player), move

  if (maximizingPlayer):
    value = float("-inf")
    move = ""
    for child in node.children:
      minimaxResult = minimax(child, depth - 1, False, (node.startPos, node.endPos), player)[0]
      if (value < minimaxResult):
        move = (child.startPos, child.endPos)
      value = max(value, minimaxResult)
    return value, move

  else:
    value = float("inf")
    move = ""
    for child in node.children:
      minimaxResult = minimax(child, depth - 1, True, (node.startPos, node.endPos), player)[0]
      if (value > minimaxResult):
        move = (child.startPos, child.endPos)
      value = min(value, minimaxResult)
    return value, move

def minimaxAlphaBeta(node, depth, alpha, beta, maximizingPlayer, move, player):
  if (depth == 0):
    return heuristic(node.state.get_board(), player), move

  if (maximizingPlayer):
    value = float("-inf")
    for child in node.children:
      minimaxResult = minimaxAlphaBeta(child, depth-1, alpha, beta, False, (node.startPos, node.endPos), player)[0]
      if(value < minimaxResult):
        move = (child.startPos, child.endPos)
      value = max(value, minimaxResult)
      alpha = max(alpha, value)
      if (alpha >= beta):
        break
    return value, move

  else:
    value = float("inf")
    for child in node.children:
      minimaxResult = minimaxAlphaBeta(child, depth-1, alpha, beta, True, (node.startPos, node.endPos), player)[0]
      if (value > minimaxResult):
        move = (child.startPos, child.endPos)
      value = min(value, minimaxResult)
      beta = min(beta, value)
      if (beta <= alpha):
        break
    return value, move