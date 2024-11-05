#!/usr/bin/env python
# coding: utf-8

# In[15]:


def knapsack(W,weights,values):
    ratios = [v/w for v,w in zip (values,weights)]
    
    n = len(weights)
    index = list(range(n))
    index.sort(key = lambda i : ratios[i],reverse=True)
    max_value = 0
    fractions=[0]*n
    for i in index :
        if(weights[i] <= W):
            max_value += values[i]
            W -= weights[i]
            fractions[i] = 1
        else:
            fractions[i]= W/weights[i]
            max_value += values[i]*fractions[i]
            break
    print(fractions)
    return max_value

W=50
weights=[10,20,30]
values=[60,100,120]
print(knapsack(W,weights,values))


# In[ ]:




