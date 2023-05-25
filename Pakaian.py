#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[21]:


df= pd.read_excel('E:\BRATI\LATIHAN\EXCEL\jualan.xlsx')
print (df)


# In[22]:


df.dtypes


# In[23]:


df[['Jumlah Produk']] = df[['Jumlah Produk']].fillna(0)
df[['Jumlah Produk']] = df[['Jumlah Produk']].astype('int')
print (df)


# In[24]:


df = df.drop(columns=['Link','Desc','Pengali','Unnamed: 14','Unnamed: 15'])
print (df)


# In[25]:


df=df.dropna(axis=0,how='any')
print(df)


# In[26]:


pd.set_option("display.max_rows", None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df


# In[ ]:


#print unique values


# In[29]:


for dtype, col in (list(zip(df.dtypes, df.columns))):
    print (df[col].unique())


# In[31]:


df


# In[40]:


##Mengganti nama value dalam kolom warna

df['Warna'] = df['Warna'].replace(['PutihBW,LenganPendekNude'],'PutihBW-Pendek')
df

