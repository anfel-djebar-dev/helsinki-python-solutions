def transpose(matrix: list):
    temp = 0
    i=1
    for r in range(0,len(matrix)):
        for c in range(r,len(matrix)):
            if c != r :
                temp = matrix[r][c] 
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp 
        i+=1

if __name__ == "__main__":
    
    m=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    print(m)
    transpose(m)    
    print(m)