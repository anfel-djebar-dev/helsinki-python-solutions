# ----------- Creation of the functioon: ---------------
def shortest(my_list):
    #initialization 
    shortest = "                                                                  "
    for item in my_list:
        if len(item) < len(shortest) :
            shortest = item
    return shortest


# -------- Testing the function : ----------

if __name__ == "__main__" :
    the_list = ["hi", "some", "seventeen", "hello", "too" ]
    result = length_of_longest(the_list)
    print(result)