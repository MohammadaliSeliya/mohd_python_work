''' Write a python program to sum of the first n positive integers.'''

       
num = int(input("enter a number: "))

if num <= 0:
    print("please give a positive integer: ")
else:
    sum = 0
    for i in range(1, num+1):
        sum += i
    print("sum of negative integer in the range: ",sum)
        