# -------- The function : ----------
def row_correct(sudoku: list , row_no: int) -> bool :
    row = sudoku[row_no] # for go directly to the row
     
    members_only = [square for square in row if square != 0 ]
    # this line will make a list with all the element of the row != 0 

    if len(members_only) != len(set(members_only)):
        return False
    return True
