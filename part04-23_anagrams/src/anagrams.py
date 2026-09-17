# -------- Creation of the function :-------
def anagrams(first_word, second_word):

    #condition statements:
    if sorted(first_word) == sorted(second_word) : # if they have exactly the same character
        return True
    return False 

# --------- testing the function : ---------
    if __name__ == "__main__" :
        anagrams(team, meat)
        anagrams(hi, hello)