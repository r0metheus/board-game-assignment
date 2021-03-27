from heuristics import heuristic
from GameRules import check_win


def minimax(node, depth, maximizingPlayer, move, player, kind):
    if (check_win(node.state.get_board()) != False):
        move = (node.startPos, node.endPos)
        if (maximizingPlayer):
            value = float("inf")
        else:
            value = float("-inf")
    if (depth == 0):
        return heuristic(node.state.get_board(), player, kind), move
    if (maximizingPlayer):
        value = float("-inf")
        move = ""
        for child in node.children:
            minimaxResult = minimax(child, depth - 1, not(maximizingPlayer), (node.startPos, node.endPos), player, kind)[0]
            if (value < minimaxResult):
                move = (child.startPos, child.endPos)
            value = max(value, minimaxResult)
        return value, move

    else:
        value = float("inf")
        move = ""
        for child in node.children:
            minimaxResult = minimax(child, depth - 1, not(maximizingPlayer), (node.startPos, node.endPos), player, kind)[0]
            if (value > minimaxResult):
                move = (child.startPos, child.endPos)
            value = min(value, minimaxResult)
        return value, move


def minimaxAlphaBeta(node, depth, alpha, beta, maximizingPlayer, move, player, kind):
    if (depth == 0 or check_win(node.state.get_board()) != False):
        if(check_win(node.state.get_board()) != False):
            if(maximizingPlayer):
                return float("-inf"), move
            else:
                return float("inf"), move
        else:
            return heuristic(node.state.get_board(), player, kind), move

    if maximizingPlayer:
        value = float("-inf")
        for child in node.children:
            minimaxResult2 = minimaxAlphaBeta(child, depth-1, alpha, beta, False, (node.startPos, node.endPos), player, kind)
            minimaxResult = minimaxResult2[0]
            minimaxResultMove = minimaxResult2[1]
            if(minimaxResult == float("-inf")):
                value = minimaxResult
                move = minimaxResultMove
                break
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
            minimaxResult2 = minimaxAlphaBeta(child, depth-1, alpha, beta, True, (node.startPos, node.endPos), player, kind)
            minimaxResult = minimaxResult2[0]
            minimaxResultMove = minimaxResult2[1]
            if(minimaxResult == float("inf")):
                value = minimaxResult
                move = minimaxResultMove
                break
            if (value > minimaxResult):
                move = (child.startPos, child.endPos)
            value = min(value, minimaxResult)
            beta = min(beta, value)
            if (beta <= alpha):
                break
        return value, move
