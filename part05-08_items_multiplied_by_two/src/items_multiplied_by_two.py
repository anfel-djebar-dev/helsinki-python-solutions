def double_items(my_list: list):

    # -------First solution ------:
    new_list = [i*2 for i in my_list]

    # ------Second solution -----:
    #for i in my_list :
       # new_list.append(i*2)

    # -------Third solution------ :
    #new_list = my_list[:]
    #for i in range(len(new_list)):
        #new_list[i] *= 2

    return new_list

if __name__ == "__main__"  :
    print(double_items([5,2,6,3,9,1]))

