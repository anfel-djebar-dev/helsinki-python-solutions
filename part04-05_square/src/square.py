def line(n,text):
    if text != "" :
        print(text[0]*n)
    else :
        print("*" *n)

def square(size, character):
    i=1
    while i<=size:
        line(size,character)
        i+=1


if __name__ == "__main__":
    square(5, "x")