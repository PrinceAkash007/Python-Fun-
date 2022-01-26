#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[13]:


img = cv2.imread('Tom cruise.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.medianBlur(gray_img, 5)
edges = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)


# In[14]:


color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)


# In[16]:


cv2.imshow('Image', img)
cv2.imshow('Cartoon', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




