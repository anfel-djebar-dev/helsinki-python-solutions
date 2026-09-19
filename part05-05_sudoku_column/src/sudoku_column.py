# _______________ The Function : _____________
def column_correct(soduku: list , column_no: int) -> bool:
 # Create a list 'column' containing all non-zero numbers in the specified column_no
   column = [row[column_no] for row in soduku if row[column_no] != 0]
   if len(column) == len(set(column)):
    return True
   return False

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
    print(column_correct(sudoku , 1))
    print(column_correct(sudoku , 0))
    