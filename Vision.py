#!/usr/bin/env python
# coding: utf-8

# # Extract Text from Receipt

# In[269]:


def get_text(path):
    
    from google.cloud import vision
    import io
    
    client = vision.ImageAnnotatorClient()
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        
    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    native = texts[0].description
    
    return native


# # Get Total from Receipt

# In[270]:


def get_total(path):
    receipt_txt = get_text(path)
    
    if 'Total' in receipt_txt:
        where = receipt_txt.find('Total')
        tot = receipt_txt[(where - 6):(where - 1)]
        return tot


# # Getting Exchange Rates

# In[271]:


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


# # Apply Exchange Rate

# In[272]:


def apply_exchange(orig,rate):
    orig = float(orig)
    rate = float(rate)
    
    converted = orig * rate
    converted = round(converted, 2)
    return converted


# # Main

# In[273]:


def main():
    path = input("Where is the image?: ")
    orig = get_total(path)
    rate = get_rate()
    
    return apply_exchange(orig,rate)
    


# In[275]:


main()


# In[ ]:




