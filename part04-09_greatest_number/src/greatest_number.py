def greatest_number(a,b,c):
    greatest =1
    if a==b and b==c:
        greatest =a
        return greatest 
    elif a==b or b==c or a==c :
         if a>b or a>c:
             greatest =a
             return greatest 
         elif c>b or a<c:
             greatest =c
             return greatest 
         elif a<b or b>c: 
             greatest =b
             return greatest 
    elif a>b and a>c:
        greatest =a
        return greatest 
    elif c>b and a<c:
        greatest =c
        return greatest 
    elif a<b and b>c: 
        greatest =b
        return greatest 

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)