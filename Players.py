RED_PLAYER = 2
BLUE_PLAYER = 4


def other(player):
    if player == RED_PLAYER:
        return BLUE_PLAYER
    return RED_PLAYER


def player_to_string(player):
    if player == RED_PLAYER:
        return str("RED_PLAYER")
    return str("BLUE_PLAYER")
