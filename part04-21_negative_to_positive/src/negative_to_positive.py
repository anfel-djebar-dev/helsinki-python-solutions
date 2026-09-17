 # --------- Enter the number N : --------
N = int(input("Please type in a positive integar : "))


# ----------The loop For : ------------
for n in range(-N , N, 1) :
    if n == 0: 
        continue
    print(n)
print(N)