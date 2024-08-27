'''Write python program that swap two number with temp variable and
without temp variable.'''

# with temp varaible

num1 = 10
num2 = 20

print("Before swapping:")
print("num1 =",num1)
print("num2 =",num2)

temp = num1
num1 = num2
num2 = temp

print("After swappimg with temp varaible:")
print("num1 =",num1)
print("num2 =",num2)

# Without temp variable

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping without temp varaible:")
print("num1 =",num1)
print("num2 =",num2)