number_of_items= int(input("How many items: "))
i=1
list_of_item = []
while i <= number_of_items: 
    item = int(input(f"Item {i}: "))
    list_of_item.append(item)
    i+=1
print(list_of_item)
