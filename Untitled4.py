#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from pytesseract import pytesseract
from pytesseract import Output
import cv2


# In[2]:


#import pytesseract
import PIL.Image


# In[3]:


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"H:\FYP\Testing\Images\image9.jpg"

img = Image.open(image_path)


# In[4]:


img


# In[5]:


img1 = cv2.imread(image_path)


# In[6]:


myconfig = r"--psm 11 --oem 3"

text = pytesseract.image_to_string(img, config=myconfig)


# In[7]:


text


# In[8]:


print(img1.shape)
height, width, _ = img1.shape


# In[9]:


boxes = pytesseract.image_to_boxes(img1, config=myconfig)


# In[10]:


#for box in boxes.splitlines():
    #box = box.split(" ")
    #img1 = cv2.rectangle(img1,(int(box[1]), height -int(box[2])), (int(box[3]), height - int(box[4])),(0, 255, 0), 2)


# In[11]:


data = pytesseract.image_to_data(img1, config=myconfig, output_type=Output.DICT)


# In[12]:


amount_boxes = len(data['text'])


# In[13]:


for i in range(amount_boxes):
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img1 = cv2.rectangle(img1, (x, y), (x+width, y+height), (0,255,0), 2)
        img1 = cv2.putText(img1, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2, cv2.LINE_AA)


# In[14]:


print(data['text'])


# In[15]:


cv2.imshow("image", img1)
cv2.waitKey(0)


# In[ ]:




