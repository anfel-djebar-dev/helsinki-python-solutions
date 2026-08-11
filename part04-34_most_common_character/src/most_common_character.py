def most_common_character(my_string: str) :
    most_common = my_string[0]
    max_count = 0

    for char in my_string:
        current_count = my_string.count(char)
        
        if current_count > max_count:
            max_count = current_count
            most_common = char

    return most_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))