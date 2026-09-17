def same_chars(word,frst_index, scnd_index):

    if frst_index >=len(word) or scnd_index >= len(word):
         return False
         
    elif word[frst_index] == word[scnd_index]:
            return True
    else :
         return False
    
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))