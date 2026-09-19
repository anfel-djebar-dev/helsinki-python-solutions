# __________________ The First Finction: ____________________
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
def sudoku_grid_correct(sudoku: list) -> bool:
    
    for r in (0, 3, 6): # It passes through rows (0, 3, 6) and columns (0, 3, 6) which are the starting places of the 9 official blocks in Sudoku
        for c in (0, 3, 6):
            if not block_correct(sudoku, r, c) :
                return False
    return True

if __name__ == "__main__" :
    sudoku = [
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
    print(block_correct(sudoku , 0 , 3))
    print(block_correct(sudoku , 4 , 4))
