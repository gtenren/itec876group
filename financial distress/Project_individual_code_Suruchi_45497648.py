#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import csv
import numpy as np
from pandas import DataFrame
from sklearn.model_selection import train_test_split


# In[5]:


data=pd.read_csv("Book6.csv")
data.head()


# In[6]:


df=pd.DataFrame(data)
df.head()


# In[7]:


dfnp=df.drop(['Financial Distress'], axis=1)


# In[8]:


xd=dfnp.pivot_table(index='Company',columns='Time',values='x1')
xd


# In[9]:


xd=xd.reset_index()
df.drop_duplicates(subset='Company',keep='last',inplace=True)
a=[]
x=[]


# In[10]:


for item in df['Financial Distress'] :
 a = item
 if a  >= -0.5 :
  z=0
 else :
  z=1
 x.append(z)
xdx=pd.DataFrame(x)
xdx.head()


# In[11]:


fd=pd.concat([xdx,xd],ignore_index=True,axis=1)
fd.head()


# In[12]:


fd =fd.drop([fd.columns[1]] ,axis='columns')
fd.head()


# In[13]:


fd.to_csv(r'C:\Users\j.s.bhalla\Desktop\filex.csv',header=False,index=False)


# In[14]:


data2=pd.read_csv("filex.csv",header=None)
data2.head()
dfr=pd.DataFrame(data2)
dfr1=dfr.fillna(0)
dfr1


# In[15]:


dfr1.to_csv(r'C:\Users\j.s.bhalla\Desktop\final_file.csv',header=False,index=False)


# In[16]:


test = dfr1[0:422]
test


# In[17]:


print(dfr1.head())
y=dfr1.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(dfr1, y, test_size=0.2)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)


# In[18]:


print(X_train.head())


# In[19]:


print(X_test.head())


# In[20]:


print(y_train.head())
print(y_test.head())


# In[21]:


test_tsv = X_train.to_csv ('financial_test.tsv', index = None, header=False,sep ='\t')


# In[22]:


train_tsv = X_test.to_csv ('financial_train.tsv', index = None, header=False,sep ='\t')

