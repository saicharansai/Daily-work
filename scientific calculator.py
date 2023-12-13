#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def modulus(a, b):
    return a % b

def power_of_2(a):
    return a ** 2

def square_root(a):
    return math.sqrt(a)

def logarithm(a, b):
    return math.log(a, b)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

choice = int(input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12): \n"))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1:
    result = add(num1, num2)
    print("The output is:", result)
elif choice == 2:
    result = sub(num1, num2)
    print("The output is:", result)
elif choice == 3:
    result = mul(num1, num2)
    print("The output is:", result)
elif choice == 4:
    result = div(num1, num2)
    print("The output is:", result)
elif choice == 5:
    result = modulus(num1, num2)
    print("Result:", result)
elif choice == 6:
    result = power_of_2(num1)
    print("Result:", result)
elif choice == 7:
    result = square_root(num1)
    print("Result:", result)
elif choice == 8:
    result = logarithm(num1, num2)
    print("Result:", result)
elif choice == 9:
    result = sin(num1)
    print("Result:", result)
elif choice == 10:
    result = cos(num1)
    print("Result:", result)
elif choice == 11:
    result = tan(num1)
    print("Result:", result)
else:
    print("Invalid choice.")


# In[ ]:




