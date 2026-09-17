# ----------- Creation of the functioon: ---------------
def all_the_longest(my_list):
    #initialization 
    longest = ""
    new_list = []
    for item in my_list:
        if len(item) >  len(longest) :
            longest = item
    for item in my_list:
        if len(item) == len(longest) :
            new_list.append(item)
    return new_list


# -------- Testing the function : ----------

if __name__ == "__main__" :
    the_list = ["hi", "some", "seventeen", "hello", "too  much" ]
    result = all_the_longest(the_list)
    print(result)