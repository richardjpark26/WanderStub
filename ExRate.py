#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_rate():
    import requests
    import json
    
    curr = str(input("Which currency is the receipt in?: "))
    curr = curr.upper()

    parameter = {"base":"USD","symbols":curr}
    response = requests.get("https://api.exchangeratesapi.io/latest", params = parameter)
    
    resp = json.loads(response.text)
    rates = resp['rates']
    designated_rate = rates[curr]
    
    return designated_rate

