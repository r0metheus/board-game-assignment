from Players import PLAYERA, AI

ai_home = [(0,6), (1,5), (1,6), (2,5), (2,6), (2,7), (3,4), (3,5), (3,6), (3,7)]
player_a_home = [(16,6), (15,5), (15,6), (14,5), (14,6), (14,7), (13,4), (13,5), (13,6), (13,7)]

even_directions = [
    (-1 ,0), #top right
    (-1,-1), #top left
    (0,+ 1), #right
    (0, -1), #left
    (+1,-1), # bottom left
    (+1, 0) #bottom right
]

odd_directions = [
    (-1,+1), #top right
    (-1, 0), #top left
    (0, +1), #right
    (0, -1), #left
    (+1, 0), # bottom left
    (+1,+1) #bottom right
]

def check_win(board):
    if  board[0][6] == PLAYERA and board[1][5] == PLAYERA and board[1][6] == PLAYERA and board[2][5] == PLAYERA and board[2][6] == PLAYERA and board[2][7] == PLAYERA and board[3][4] == PLAYERA and board[3][5] == PLAYERA and board[3][6] == PLAYERA and board[3][7] == PLAYERA:
        return PLAYERA

    if board[16][6] == AI and board[15][5] == AI and board[15][6] == AI and board[14][5] == AI and board[14][6] == AI and board[14][7] == AI and board[13][4] == AI and board[13][5] == AI and board[13][6] == AI and board[13][7] == AI: 
        return AI
    return False

def check_if_in_board(board, pos):
    return 0 <= pos[0]  and pos[0] < len(board) and 0 <= pos[1] and pos[1] < len(board[0]) and board[pos[0]][pos[1]] != 0

def is_empty(board, pos):
    return board[pos[0]][pos[1]] == 1 and not is_pebble(board, pos) and check_if_in_board(board, pos)

def is_pebble(board, pos):
    return board[pos[0]][pos[1]] == AI or board[pos[0]][pos[1]] == PLAYERA

def get_neighbours(board, pos):
    neighbours = []
    if pos[0] % 2 == 0:
        for d in even_directions:
            new_x = pos[0] + d[0]
            new_y = pos[1] + d[1]
            if check_if_in_board(board, (new_x, new_y)):
                neighbours.append((new_x, new_y))
    else:
        for d in odd_directions:
            new_x = pos[0] + d[0]
            new_y = pos[1] + d[1]
            if check_if_in_board(board, (new_x, new_y)):
                neighbours.append((new_x, new_y))

    return neighbours

## elimitate diagonals from double jump check

def double_jumps(board, positions):
    #for each pos, check if there is a neighbour not empty
    #add all new neighbour to array
    all_jumps = []
    for p in positions:
        if not is_empty(board, p):
            neighbours = get_neighbours(board, p)
            for n in neighbours:
                if is_empty(board, n):
                    all_jumps.append(n)
    return all_jumps

def valid_moves(board, pos, player):
    valid_pos = get_neighbours(board, pos)
    to_remove = []
    
    #check for double jumps
    for j in double_jumps(board, valid_pos):
        valid_pos.append(j)
    
    #if pos is in the opposite home, it cannot exit
    if player == AI and pos in player_a_home:
        print("AI got in PLAYER A home")
        #can move only in current home
        for p in valid_pos:
            if p not in player_a_home:
                to_remove.append(p)
    elif player == PLAYERA and pos in ai_home:
        print("PLAYER A got in AI home")
        for p in valid_pos:
            if p not in ai_home:
                to_remove.append(p)


    #remove not valid positions
    for p in valid_pos:
        if not is_empty(board, p):
            to_remove.append(p)
    
    for p in to_remove:
        valid_pos.remove(p)

    return valid_pos
    