#!/usr/bin/env python
# coding: utf-8

# In[22]:


from pdf2image import convert_from_path, convert_from_bytes
import os
import time
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


# In[28]:


def convert(file_name):
    count_jpg = 0
    #pages = convert_from_path('./'+file_name)
    pages = convert_from_bytes(open('./'+file_name, 'rb').read())
    for page in pages:
        page.save(file_name+'_'+str(count_jpg)+'.jpg', 'JPEG')
        count_jpg+=1 
    
    return count_jpg


# In[29]:


count = 0
count_pdf = 0
for file in os.listdir('./'):
    if file.endswith('.pdf'):
        print(file)
        count_pdf+=1
        count += convert(file)
print('All PDF files:',count_pdf)
print('All convert JPG:',count)
print('--------Finish PDF convert to JPG--------')
time.sleep(5)



# In[ ]:




