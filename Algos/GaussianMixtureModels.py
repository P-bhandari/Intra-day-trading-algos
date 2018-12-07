#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pandas_datareader import data as web
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.model_selection import RandomizedSearchCV as rcv
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt
from sklearn import mixture as mix
from IPython import get_ipython


# In[7]:


df = web.DataReader('SPY',data_source='yahoo',start='2010')
df = df[['Open','High','Low','Close']]
df['open']=df['Open'].shift(1);
df['high']=df['High'].shift(1);
df['low']=df['Low'].shift(1);
df['close']=df['Close'].shift(1);

df =df[['open','high','low','close']]


# In[8]:


df = df.dropna();


# In[9]:


unsup = mix.GaussianMixture(n_components = 4, covariance_type="spherical",n_init=100,random_state = 42)


# In[10]:


unsup.fit(np.reshape(df,(-1,df.shape[1])))
regime = unsup.predict(np.reshape(df,(-1,df.shape[1])))


# In[11]:


df['Return'] = np.log(df['close']/df['close'].shift(1))


# In[17]:


Regimes = pd.DataFrame(regime,columns=['Regime'],index=df.index)    .join(df,how= 'inner')        .assign(market_cu_return =df.Return.cumsum())            .reset_index(drop=False)                .rename(column{'index':'Date'})


# In[ ]:




