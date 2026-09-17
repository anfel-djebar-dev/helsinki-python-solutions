# ------------Creation of the function : -------------
def sum_of_positives(my_list) :
    the_sum = 0
    for n in my_list:
        if n >= 0 :
            the_sum += n 
        else : 
            continue
    return the_sum


#-------- Testing the function: -------
#result = sum_of_positives([0,2,-1,3,-3])
#print(result)

#the body "main"
if __name__ == "__main__" :
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)