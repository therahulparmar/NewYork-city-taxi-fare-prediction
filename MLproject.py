#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#%matplotlib inline
#import matplotlib
#import math
#matplotlib.rcParams["figure.figsize"]=(20,10


# In[2]:


df1 = pd.read_csv("yellow_tripdata_october.csv" , low_memory=False)
df1


# In[3]:


df2 = df1.dropna()
df2


# In[4]:


df2.RatecodeID.describe()


# In[5]:


plt.scatter(df2.total_amount, df2.trip_distance)
plt.xlabel('total_amount')
plt.ylabel('trip_distance')
plt.title('t v d')
plt.show()


# In[6]:


df2.trip_distance.describe()


# In[7]:


df2.shape


# In[8]:


def remove_pps_outliers(df2):
    df_out = pd.DataFrame()
    for key, subdf in df2.groupby('VendorID'):
        m = np.mean(subdf.trip_distance)
        st = np.std(subdf.trip_distance)
        reduced_df = subdf[(subdf.trip_distance> 0 ) & (subdf.trip_distance<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
df3 = remove_pps_outliers(df2)
df3.shape


# In[9]:


df3.trip_distance.describe()


# In[10]:


plt.scatter(df3.total_amount, df3.trip_distance)
plt.xlabel('total_amount')
plt.ylabel('trip_distance')
plt.title('t v d')
plt.show()


# In[11]:


def remove_pps_outliers(df3):
    df_out = pd.DataFrame()
    for key, subdf2 in df3.groupby('VendorID'):
        m = np.mean(subdf2.total_amount)
        st = np.std(subdf2.total_amount)
        reduced_df = subdf2[(subdf2.total_amount> 0 ) & (subdf2.total_amount<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
df4 = remove_pps_outliers(df3)
df4.shape


# In[12]:


df4.total_amount.describe()


# In[13]:


plt.scatter(df4.total_amount, df4.trip_distance)
plt.xlabel('total_amount')
plt.ylabel('trip_distance')
plt.title('t v d')
plt.show()


# In[14]:


df4.RatecodeID.describe()


# In[15]:


def remove_pps_outliers(df4):
    df_out = pd.DataFrame()
    for key, subdf3 in df4.groupby('RatecodeID'):
        m = np.mean(subdf3.RatecodeID)
        st = np.std(subdf3.RatecodeID)
        reduced_df = subdf3[(subdf3.RatecodeID> 0 ) & (subdf3.RatecodeID<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
df5 = remove_pps_outliers(df4)
df5.shape


# In[16]:


df5.RatecodeID.describe()


# In[17]:


df5


# In[18]:


df5.dtypes


# In[19]:


index_names = df5[ df5['RatecodeID'] == 99.0 ].index


# In[20]:


drop_A=df5.index[df5['RatecodeID'] == 99.0].tolist()
df6=df5.drop(df5.index[drop_A])


# In[21]:


df6.shape


# In[22]:


df6.RatecodeID.describe()


# In[23]:


import seaborn as sns
plt.figure(figsize=(15,10))
ax = plt.axes()
corr = df5.corr()
sns.heatmap(corr, fmt='.2f', annot=True, cmap ="YlGnBu")
ax.set_title('Matrix Showing Correlation Between Every Parameters')
plt.show()


# In[24]:


df6 = df5.assign(final_amount= (df5.fare_amount + df5.extra + df5.mta_tax + df5.tip_amount + df5.tolls_amount + df5.improvement_surcharge + df5.congestion_surcharge ))


# In[25]:


df6


# In[26]:


df7 = df6.drop(['extra' , 'mta_tax' , 'tip_amount' , 'tolls_amount' , 'improvement_surcharge' , 'total_amount' , 'congestion_surcharge'] , axis=1)


# In[27]:


df7


# In[28]:



plt.scatter(df7.final_amount, df7.trip_distance)
plt.xlabel('final_amount')
plt.ylabel('trip_distance')
plt.title('t v d')
plt.show()


# In[29]:


def remove_pps_outliers(df7):
    df_out = pd.DataFrame()
    for key, subdf7 in df7.groupby('VendorID'):
        m = np.mean(subdf7.final_amount)
        st = np.std(subdf7.final_amount)
        reduced_df = subdf7[(subdf7.final_amount> 0 ) & (subdf7.final_amount<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
df8 = remove_pps_outliers(df7)
df8.shape


# In[30]:


df8.final_amount.describe()


# In[31]:


plt.scatter(df8.final_amount, df8.trip_distance)
plt.xlabel('final_amount')
plt.ylabel('trip_distance')
plt.title('t v d')
plt.show()


# In[ ]:




