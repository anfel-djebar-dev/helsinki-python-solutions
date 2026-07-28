def line(n,text):
    if text != "" :
        print(text[0]*n)
    else :
        print("*" *n)

def shape(width,trngl_char,height,rctngl_char):
    i=1
    while i<=width:
        line(i,trngl_char)
        i+=1
    i=1
    while i<=height:
        line(width,rctngl_char)
        i+=1
#shape(5, "x", 2, "o")
if __name__ == "__main__":
    shape(5, "x", 2, "o")