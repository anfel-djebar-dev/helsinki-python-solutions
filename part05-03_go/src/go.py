# -----------------The function : -------------
def who_won(gameboard: list):
    count_player1 = 0
    count_player2 = 0
    for row in gameboard:
        for square in row :
            if square == 1 :
                count_player1 +=1 
            elif square == 2 :
                count_player2 += 1
    if count_player1 > count_player2 :
        return 1
    elif count_player1 < count_player2:
        return 2
    else :
        return 0