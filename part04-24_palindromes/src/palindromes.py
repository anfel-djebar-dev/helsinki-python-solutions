# ------------ Creation of the funciton : -------------
def palindromes(word):

    #initialization of i :
    i = len(word)
    
    #the loop for :
    for n in range(len(word)):

        i-=1
        if word[n] != word[i]:
            return False
        if n >= i:              
            return True    
    
#--------the loop while: -------
while True:

    # 1/enter the word:
    word = input("Please type in a palindrome: ")

    # 2/calling the function:
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

if __name__ == "__main__":
    palindromes(word)
    
                   
               


