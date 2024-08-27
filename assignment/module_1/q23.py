''' Write a Python function to insert a string in the middle of a string.
'''

string1 = input("Enter the string1: ")
string2 = input("Enter the string2: ")
middle = len(string1)// 2

result = string1[:middle] +  string2 + string1[middle:]
print(result)

    