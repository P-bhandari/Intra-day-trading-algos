#!/usr/bin/env python
# coding: utf-8

# In[18]:


from pandas_datareader import data as web
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.model_selection import RandomizedSearchCV as rcv
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt


# In[10]:


df = web.DataReader('SPY',data_source='yahoo',start='2010')


# In[12]:


df = df[['Open','High','Low','Close']]
df['open']=df['Open'].shift(1)
df['high']=df['High'].shift(1)
df['close']=df['Close'].shift(1)
df['low']=df['Low'].shift(1)


# In[14]:


#extrapolating values for the missing numbers in the dataset
imp =Imputer(missing_values='NaN',strategy='mean',axis=0)


# In[25]:


steps =[('imputation',imp),('scaler',StandardScaler()),('lasso',Lasso())]


# In[46]:


pipeline = Pipeline(steps)
parameters = {'lasso__alpha':np.arange(0.0001,1,.0001),
            'lasso__max_iter':np.random.uniform(100,100000,4)}


# In[47]:


reg = rcv(pipeline,parameters,cv=5) #5-fold crossvalidation


# In[48]:


#split data into test train and X Y
X= df[['open','high','low','close']]
Y= df['Close']


# In[62]:


avg_err={}
for t in np.arange(50,97,3):
    split = int(t*len(X)/100)
    reg.fit(X[:split],Y[:split])
    best_alpha = reg.best_params_['lasso__alpha']
    best_iter = reg.best_params_['lasso__max_iter']
    reg1= Lasso(alpha=best_alpha,max_iter = best_iter)
    X= imp.fit_transform(X,Y)
    reg1.fit(X[:split],Y[:split])
    #calculating accuracy/error
    df['P_C_%i'%t]=0 
    df.iloc[split:,df.columns.get_loc('P_C_%i'%t)]=reg1.predict(X[split:])
    df['Error_%i'%t]=np.abs(df['P_C_%i'%t]-df['Close'])
    e=np.mean(df['Error_%i'%t][split:])
    avg_err[t]=e
    Range = df['high'][split:]-df['low'][split:]
    plt.scatter(avg_err.keys(),avg_err.values())
    print( np.average(Range))


# In[61]:





# In[ ]:




