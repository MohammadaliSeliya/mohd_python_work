'''Write a Python program to get the Factorial number of given number.'''

nums=int(input("enter a number:"))

factorial=1

if nums < 0:
    print("factorial is not defined for negative numbers.")
elif nums == 0:
    print("the factorial of 0 is 1.")
else:
    for num in range(1,nums+1):
        factorial*=num
        print(f"the factorial of {nums} is:{factorial}")
        