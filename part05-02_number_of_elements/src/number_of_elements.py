# function to count how many elements within the matrix match the argument value :
def count_matching_elements(matrix: list , element: int):
    count = 0
    for row in matrix :
        for column in row :
            if column == element :
                count +=1 
    return count

# the main function :
if __name__ == "__main__" :
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
                