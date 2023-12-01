#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
choice = int(input("Enter your choice 1/2/3/4 \n"))
num1  = float(input("enter first number.......\n"))
num2  = float(input("enter second number......\n"))

if choice == 1:
    dt = add(num1,num2)
    print("The output is:",dt)
elif choice == 2:
    dt = sub(num1,num2)
    print("The output is:",dt)
elif choice == 3:
    dt = mul(num1,num2)
    print("The output is:",dt)  
elif choice == 4:
    dt = div(num1,num2)
    print("The output is:",dt) 
else:
    print("Invalid......")
    

