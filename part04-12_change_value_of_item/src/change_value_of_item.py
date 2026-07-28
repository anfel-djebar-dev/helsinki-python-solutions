list = [1,2,3,4,5]
index =0
new_value=1
while  True:
    index=int(input("index: "))
    if index == -1:
        break
    new_value= int(input("new value :"))
    list[index] = new_value
    print(list)