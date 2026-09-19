# __________________ The First Finction: ___________________
def block_correct(sudoku: list , row_no: int , column_no: int) -> bool :
    block = []
    n = 0
    while n < 3 :
        row = sudoku[row_no + n]
        elements = [ element for element in row[ column_no : column_no + 3] if element != 0]
        block += elements
        n +=1
    return len(block) == len(set(block))

# _________________ The Second Function: ___________________ 
def column_correct(soduku: list , column_no: int) -> bool:
 # Create a list 'column' containing all non-zero numbers in the specified column_no
   column = [row[column_no] for row in soduku if row[column_no] != 0]
   if len(column) == len(set(column)):
    return True
   return False

# _______________ The Third Function : _____________________
def row_correct(sudoku: list , row_no: int) -> bool :
    row = sudoku[row_no] # for go directly to the row
     
    members_only = [square for square in row if square != 0 ]
    # this line will make a list with all the element of the row != 0 

    if len(members_only) != len(set(members_only)):
        return False
    return True



# _________________ The Main Grid Function _________________
def sudoku_grid_correct(sudoku: list) -> bool:

    # 1. Checking all 9 rows and 9 columns
    i = 0
    while i < 9:
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False
        i += 1

    # 2. Checking all 9 official blocks (3x3)
    for r in (0, 3, 6):
        for c in (0, 3, 6):
            if not block_correct(sudoku, r, c):
                return False

    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))  # False

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))  # True