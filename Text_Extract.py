#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

