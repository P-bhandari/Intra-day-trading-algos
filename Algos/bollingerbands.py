#!/usr/bin/env python
# coding: utf-8

# In[17]:


import statistics 
import numpy as np

bollinger_window_size = 20 ; 

def calc_bollinger(array):
    middleband = 0 ; 
    upperband = 0 ; 
    lowerband = 0 ; 
    if(len(array)>0):
        middleband = np.mean(array); 
        std_dev = np.std(array) ;
        upperband = middleband + std_dev ;
        lowerband = middleband - std_dev ;
    else:
        print("[calc_bollinger] Size of input array must be greater than 0"); 
    bollinger= []  ; 
    bollinger.append(upperband); 
    bollinger.append(middleband); 
    bollinger.append(lowerband); 
    return bollinger ; 
    
def bollinger_bands(array, start_index ,window_size=bollinger_window_size):
    if(start_index + window_size <len(array)):
        return calc_bollinger(array[start_index:start_index+20]);
    else:
        return calc_bollinger(array[start_index:]);
    
# creating a simple data - set 
sample = [1, 2, 3, 4, 5] 
  
a = bollinger_bands(sample,0,2); 


# In[18]:





# In[13]:





# In[14]:





# In[ ]:




