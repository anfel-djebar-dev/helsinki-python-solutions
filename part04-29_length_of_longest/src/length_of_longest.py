# ----------- Creation of the functioon: ---------------
def length_of_longest(my_list):
    #initialization 
    longest = 00
    for item in my_list:
        if len(item) > longest :
            longest = len(item)
    return longest


# -------- Testing the function : ----------

if __name__ == "__main__" :
    the_list = [hi, some, seventeen, hello, too ]
    result = length_of_longest(the_list)
    print(result)