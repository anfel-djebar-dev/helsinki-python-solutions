def times_ten(start_index: int , end_index: int ):
    d={}
    n = start_index
    while n <= end_index :
        d[n] = n*10
        n+=1
    return d
if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
