''' Write a Python program to count the occurrences of each word in a
given sentence.'''


string=input('enter the string: ')
words=string.split()
dict = {}
for i in words:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)