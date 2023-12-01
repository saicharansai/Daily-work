#!/usr/bin/env python
# coding: utf-8

# In[9]:


def funct3(num_lst):
    even_num = []
    odd_num = []
    for number in num_lst:
        if number % 2 == 0:
            even_num.append(number)
        else:
            odd_num.append(number)
    print("The even numbers are...", even_num)
    print("The odd numbers are...", odd_num)



# In[11]:


funct3([1,10,2,4,11,14,13])

