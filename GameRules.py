from Players import Players

def check_win(board):
    if  board[0][6] == Players.AI and board[1][5] == Players.AI and board[1][6] == Players.AI and board[2][5] == Players.AI and board[2][6] == Players.AI and board[2][7] == Players.AI and board[3][4] == Players.AI and board[3][5] == Players.AI and board[3][6] == Players.AI and board[3][7] == Players.AI:
        return Players.AI

    if board[16][6] == Players.PLAYERA and board[15][5] == Players.PLAYERA and board[15][6] == Players.PLAYERA and board[14][5] == Players.PLAYERA and board[14][6] == Players.PLAYERA and board[14][7] == Players.PLAYERA and board[13][4] == Players.PLAYERA and board[13][5] == Players.PLAYERA and board[13][6] == Players.PLAYERA and board[13][7] == Players.PLAYERA: 
        return Players.PLAYERA
    return False

def valid_moves(board, pos):
    valid_pos = []
    #check 6 spaces around
    #check NE: row above
    if pos[0] >= 1 and board[pos[0] -1][pos[1]] == 1:
        if pos[0] % 2 != 0:
            if pos[1] < len(board[0]) -1 and board[pos[0] -1][pos[1]+1] == 1:
                valid_pos.append((pos[0] -1, pos[1] +1))
        else:
            valid_pos.append((pos[0] -1, pos[1]))
    #check NW
    if pos[0] >= 1 and pos[1] >= 1 and board[pos[0]-1][pos[1] -1] == 1:
        if pos[0] % 2 != 0:
            valid_pos.append((pos[0]-1, pos[1]))
        else:
            valid_pos.append((pos[0]-1, pos[1]-1))
    # #check E
    if pos[1] < len(board[0]) -1 and board[pos[0]][pos[1] +1] == 1:
        valid_pos.append((pos[0], pos[1] +1))
    # #check W
    if pos[1] >= 1 and board[pos[0]][pos[1] - 1] == 1:
        valid_pos.append((pos[0], pos[1] -1))
    # #check SE
    if pos[0] < len(board) - 1 and board[pos[0] +1][pos[1]] == 1:
        if pos[0] % 2 != 0:
            if pos[1] < len(board[0])-1 and board[pos[0] +1][pos[1]+1] == 1:
                valid_pos.append((pos[0]+1, pos[1]+1))
        else:
            valid_pos.append((pos[0]+1, pos[1]))
    # #check SW
    if pos[0] < len(board[0]) -1 and pos[1] >= 1 and board[pos[0] +1][pos[1] -1] == 1:
        if pos[0] % 2 != 0:
            valid_pos.append((pos[0]+1, pos[1]))
        else:
            valid_pos.append((pos[0] +1, pos[1] -1))
    return valid_pos