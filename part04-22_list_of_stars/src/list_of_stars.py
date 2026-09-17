# ---------Creation of the Function:-----------
def list_of_stars(my_list):

    # --------Creation of the loop :--------
    for n in my_list:
        print("*" * n)


    # ---- Testin the function : ----
#list_of_stars([2,4,0,5,8])

if __name__ == "__main__":
    the_list = [2,4,0,5,8]
    list_of_stars(the_list)