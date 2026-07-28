# ---- the first function: ---- 
def first_word(sentence):
    i=0
    word=""
    while i<len(sentence):
        if sentence[i] == " ":
            return word
        word+=sentence[i]
        i+=1
        
# --- Testing the first function : ---
#sentence = "once upon a time there was a programmer"
#print(first_word(sentence))

# ---- the second function: ----
def second_word(sentence):
    sentence = sentence.strip() + " "
    sentence = sentence[sentence.find(" ") + 1:]
    index2 = 0
    i = index2
    second_word=""
    while i >= index2:
         if sentence[i] == " " or sentence[i] == None:
            return second_word
         second_word+=sentence[i]
         i+=1
         
# --- Testing the Second function : --- 
#sentence = "once upon a time there was a programmer"
#print(second_word(sentence))  

# --- the Third function : ---
def last_word(sentence):
    i=-1
    word=""
    while abs(i) < len(sentence):
        if sentence[i] == " ":
            return word
        word = sentence[i] + word
        i-=1
 
# --- Testing the Third function : ---
#sentence = "once upon a time there was a programmer"
#print(last_word(sentence))

if __name__ == "__main__":
   sentence = "once upon a time there was a programmer"
   print(first_word(sentence))
   print(second_word(sentence))
   print(last_word(sentence))