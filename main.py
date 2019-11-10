#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Text_Extract import get_text
from Orig_Total import get_total
from ExRate import get_rate
from converted import apply_exchange

def main():
    path = input("Where is the image?: ")
    orig = get_total(path)
    rate = get_rate()
    
    return apply_exchange(orig,rate)

