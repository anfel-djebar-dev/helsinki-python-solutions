def line(n,text):
    if text != "" :
        print(text[0]*n)
    else :
        print("*" *n)

def triangle(size):
    i=1
    while i<=size:
        line(i,"#")
        i+=1

if __name__ == "__main__":
    triangle(5)
