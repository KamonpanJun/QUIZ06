#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns


# In[2]:


pwd


# In[3]:


###Read csv file
df = pd.read_csv("Salaries.csv")


# In[4]:


##List first 5 records
df.head()


# In[9]:


##QUIZ1
df.head(10)


# In[10]:


##QUIZ1
df.head(20)


# In[11]:


##QUIZ1
df.head(50)


# In[14]:


##QUIZ1
df.tail()


# In[5]:


###check a particular column type
df['salary'].dtype


# In[6]:


##check types for all the columns
df.dtypes


# In[7]:


##QUIZ2 p50-61
##Group data using rank
df_rank = df.groupby(['rank'])


# In[8]:


##calculate mean value for each numeric column per each group
df_rank.mean()


# In[15]:


#calculate mean salary for each professor rank
df.groupby('rank')[['salary']].mean()


# In[16]:


#calculate mean salary for each professor rank
df.groupby(['rank'], sort = False)[['salary']].mean()


# In[17]:


#calculate mean salary for each professor rank
df_sub = df[df['salary']>120000]


# In[18]:


#select only those rows that contain female professors
df_f = df[df['sex'] == 'Female']


# In[19]:


#select colum salary
df['salary']


# In[20]:


#select colum salary
df[['rank','salary']]


# In[21]:


#select rows by their position
df[10:20]


# In[22]:


#select rows by their labels
df_sub.loc[10:20,['rank','sex','salary']]


# In[23]:


#select rows by their labels
df_sub.iloc[10:20,[0,3,4,5]]


# In[24]:


#create a new data frame from the original sorted by the column  salary
df_sorted = df.sort_values(by = 'service')
df_sorted.head()


# In[25]:


df_dorted = df.sort_values(by=['service','salary'],ascending = [True, False])
df_sorted.head(10)

