#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Text_Extract import get_text
from Orig_Total import get_total
from ExRate import get_rate

def apply_exchange(orig,rate):
    orig = float(orig)
    rate = float(rate)
    
    converted = orig * rate
    converted = round(converted, 2)
    return converted

