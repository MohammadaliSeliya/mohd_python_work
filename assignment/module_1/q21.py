'''Write a Python function that takes a list of words and returns the length of the longest one.'''


list = ["milk","sugar","coffee","watermelon"]

max_len = 0

for word in list:
    if len(word) > max_len:
        max_len = len(word)
print(max_len) 
       