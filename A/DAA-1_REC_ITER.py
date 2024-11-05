#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#RECURSIVE


# In[2]:


num = int(input("Enter number :- "))
print("Below is a fibonacci sequence...")
def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(0,num):
    print(fib(i))


# In[ ]:


#NON RECURSIVE(Iterative)


# In[4]:


num = int(input("Enter number :- "))
print("Below is fibonacci sequence...")
a=0
b=1
for i in range(0,num):
    if i<=1:
        print(i)
    else:
        result=a+b
        a=b
        b=result
        print(result)

