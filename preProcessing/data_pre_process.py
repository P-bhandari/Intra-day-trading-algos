#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
def dataprocess(path,filenames):
    for name in filenames:
        if(not process_file(path,name,name[6:9]+name[4:6])):
            print("Error in parsing file = ",name);
        
        
def process_file(path, filename, outputname ):
    myData = np.genfromtxt(path+filename,dtype=None,delimiter= " ");
    np.save(path[:-4]+"pre_processed/"+outputname,myData);
    return True; 
#myData = np.genfromtxt("logs10apr.txt",dtype=['str','str','int','str','str','int','int','float','float','float'] ,delimiter= " ");
filenames = ["logs10apr.txt","logs11apr.txt","logs12apr.txt","logs13apr.txt","logs17apr.txt","logs18apr.txt","logs19apr.txt","logs20apr.txt","logs21apr.txt","logs24apr.txt"];
path = "/home/batman/Documents/TradingAlgo/dataset/raw/";
dataprocess(path,filenames); 


# In[ ]:




