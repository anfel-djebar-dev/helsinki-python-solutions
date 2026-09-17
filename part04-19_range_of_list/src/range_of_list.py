# ---------- The creation Of The Function : ----------
def range_of_list(my_list):
    # range the list from the smallest to the greatest with : sorted()
    new_list = sorted(my_list)
    # calcule the difference between the greatest and the smallest number (item)
    result = new_list[-1] - new_list[0] 
    return result 

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)