def formatted(my_list):
    formatted_list = []
    for n in my_list:
        decimal_float = f"{n:.2f}"
        formatted_list.append(decimal_float)
    return formatted_list
    
if __name__ == "__main__" :
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)