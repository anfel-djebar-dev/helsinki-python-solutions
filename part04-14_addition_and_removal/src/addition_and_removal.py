# ----creation of the liste:---- 
list = []
i = 1 


# -----The loop:-----
while True:
    print("The list is now",list)
    opperation = input("a(d)d, (r)emove or e(x)it: ")
    

# ----- The exit's condition: -----
    if opperation == "x" :
        print("Bye!")
        break

# ----- The addition's condition: -----
    elif opperation == "d":
        list.append(i)
        i+=1
        # continue due to not do the next condition if this is true
        continue 

# ----- The removel's condition : -----
    elif opperation == "r" :
        # pop : with i-1 , and remove : with i 
        # / bcs i is the contents of the index here 
        # index = i-1 , content = i 
        # I think these line [25:27] has a wrong ideas 
        # so ---> pop() with nothing is the best solution here <---
        # /bcs it remove the last index or number of the list 
        list.pop()
        i-=1
        continue 