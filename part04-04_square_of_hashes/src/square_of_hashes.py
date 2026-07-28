def line(n,text):
    if text != "" :
        print(text[0]*n)
    else :
        print("*" *n)

def square_of_hashes(size):
    i=1
    while i<=size:
        line(size,"#")
        i+=1
#line(4, "#")

if __name__ == "__main__":
    square_of_hashes(5)
