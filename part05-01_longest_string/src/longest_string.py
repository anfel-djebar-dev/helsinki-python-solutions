# --------------The function : -------------
# function to finds and returns the longest string in a list of strings 
def longest(strings: list):
    longest = ""
    for string in strings:
        if len(string) >= len(longest):
            longest = string
    return longest 


# the main function :
if __name__ == "__main__" :
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))