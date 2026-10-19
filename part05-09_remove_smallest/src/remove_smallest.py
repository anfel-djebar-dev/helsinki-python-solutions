def remove_smallest(my_list : list):
    
    my_list.remove(min(my_list))

if __name__ == "__main__" :
    numbers = [2,5,2,6,1,6,29]
    print(remove_smallest(numbers))