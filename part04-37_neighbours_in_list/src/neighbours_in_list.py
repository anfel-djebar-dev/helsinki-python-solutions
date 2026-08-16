def longest_series_of_neighbours(my_list: list) :
    if not my_list:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(my_list)):
        # نتحقق مما إذا كان الفرق مطلقاً بين العنصر الحالي والذي قبله يساوي 1
        if abs(my_list[i] - my_list[i - 1]) == 1:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 1

    return max_len

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))