def play_turn(game_board: list, x: int, y: int, piece: str):
    if x >=0 and x <=2 and y >=0 and y <=2:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False
    
    