#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Text_Extract import get_text

def get_total(path):
    receipt_txt = get_text(path)
    
    if 'Total' in receipt_txt:
        where = receipt_txt.find('Total')
        tot = receipt_txt[(where - 6):(where - 1)]
        return tot

