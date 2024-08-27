''' Write a Python program to count the number of characters (character
frequency) in a string.
'''

string = "Mohammadali"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
        
for key, value in frequency.items():
        print(f"{key}:{value}")


name = "seliya mohammadali"
print(name.count("a"))