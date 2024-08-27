'''Write a Python program to get the Fibonacci series of given range.'''

nums = int(input("Enter the number for Fibonacci series: "))

a, b = 0, 1


for num in range(nums):
    if num == 0:
        print(a)
    elif num == 1:
        print(b)
    else:
        c = a + b
        a = b
        b = c
        print(c)