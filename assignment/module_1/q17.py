''' Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.'''


str1 = "mohammadali"
str2 = "seliya"

print(str2[:2] + str1[2:]  + " " + str1[:2] + str2[2:])