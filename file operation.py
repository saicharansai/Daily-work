#!/usr/bin/env python
# coding: utf-8

# In[26]:


wr = open("text.txt",'w')
wr.write("this is first example\n")
wr.write("this is second example\n")
wr.write("this is third example\n")
wr.write("this is fouth example\n")
wr.write("this is fifth example\n")
wr.write("this is sixth example\n")
wr.close()


# In[27]:


wr = open("text.txt",'a')
wr.write("this is seventh example\n")
wr.write("this is eigth example\n")
wr.write("this is nineth example\n")
wr.write("this is tenth example\n")
wr.close()


# In[28]:


fr = open("text.txt",'r')
st = fr.read(100)
print(st)


# In[29]:


fr = open("text.txt",'r')
st = fr.readline()
print(st)


# In[30]:


fr = open("text.txt",'r')
st = fr.readlines()
print(st)


# In[31]:


with open("text.txt") as f:
    for text in f:
        print(text)

