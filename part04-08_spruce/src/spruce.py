def spruce(number):
    print("a spruce!")
    i =1
    n=1
    space=number-1
    while i<=number:
        print(" "* space+ "*" * n)
        n+=2
        i+=1
        space-=1
    print(" " * (number-1)+"*")
if __name__ == "__main__":
    spruce(5)