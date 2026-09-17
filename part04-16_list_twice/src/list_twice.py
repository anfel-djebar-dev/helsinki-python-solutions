# ---------The creation of the list : -----------
my_list = []

# ----- The loop : -----
while True:
    # Enter the items
    item = int(input("New item: "))
    # The condition statement 
    if item == 0 :
        print("Bye!")
        break
    my_list.append(item)
    # Print the original list
    print("The list now:",my_list)
    # Print the item of the list from the smallest to greatest
    print("The list in order:",sorted(my_list))