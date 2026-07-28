def line(n,text):
    if text != "" :
        print(text[0]*n)
    else :
        print("*" *n)
#line(2,"non")
if __name__ == "__main__":
    line(5, "x")