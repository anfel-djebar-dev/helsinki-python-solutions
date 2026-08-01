# --------Creatiation of the list : ----------
my_list = []
i=1


# ----- The loop : -----
while True:
    # enter word 
    word = input("Word: ")

    # ----- The condition's statements: -----
    if word in my_list :
        print("You typed in",i-1,"different words")
        break 

    else :
        my_list.append(word)
        i+=1
