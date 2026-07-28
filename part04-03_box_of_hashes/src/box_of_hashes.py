def line(n,text):
    if text != "" :
        print(text[0]*n)
    else :
        print("*" *n)

def box_of_hashes(height):

    i=1
    while i<= height:
        line(10, "#")
        i+=1


if __name__ == "__main__":
    box_of_hashes(5)
