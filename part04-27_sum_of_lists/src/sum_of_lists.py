# -------------- Creaition of the function: ---------------
def list_sum(first_list, second_list) :
    #initialization 
    new_list = []
    sum =0 
    #the loop 
    for n in range(len(first_list)):
        sum = first_list[n] + second_list[n] 
        new_list.append(sum)
        sum = 0 
    return new_list 
    


# Testing the function :
if __name__ == "__main__" :
    a = [2,8,4]
    b = [1,5,9] 
    print(list_sum(a,b))
    