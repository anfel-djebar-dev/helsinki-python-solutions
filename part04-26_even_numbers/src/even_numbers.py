# ------------The Creation of the function: ---------------
def even_numbers(my_list):
    new_list = []
    for n in my_list:
        if n % 2 == 0 :
            new_list.append(n)
    return new_list


# --------- Testing the function: -----------
if __name__ == "__main__" :
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)