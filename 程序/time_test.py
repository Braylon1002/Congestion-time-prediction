#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt#约定俗成的写法plt


# In[10]:


dt = pd.read_excel('C:\\Users\\kongzi\\Desktop\\处理数据\\test.xlsx',names = ['时间','速度'])


# In[11]:


dt


# In[12]:


#假设8点经过该拥挤路段，该路段两端纬经度为（30.6214，104.094），（30.6195，104.058）
from math import radians,cos,sin,asin,sqrt
def geodistance(lat1,lng1,lat2,lng2):
    #经纬度换算成弧度
    lat1,lng1,lat2,lng2= map(radians,[float(lat1),float(lng1),float(lat2),float(lng2)])
    dlon = lng2-lng1
    dlat = lat2-lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    distance = 2*asin(sqrt(a))*6371*1000#地球平均半径，6371km
    #distance = round(distance/1000,3)
    return distance


# In[13]:


L = geodistance(30.6214,104.094,30.6195,104.058)
#此为该路段长度
L


# In[38]:


#计算通过此路段时间
#计算早上八点所在行
def v_start(dt,time):
    for i in range(len(dt)):
        if str(dt['时间'][i]) == time:
            a= i
            return a
#v = v_start(dt,'2014-08-23 08:00:00')
def time_end(L,dt,time):
    v = v_start(dt,time)
    sum = 0
    for i in range(v,len(dt)):
        sum += dt['速度'][i]*60
        if sum <L:
            continue
        else:
            #
            t =(L-(sum - dt['速度'][i-1]*60))/dt['速度'][i]
            end = i-v+t/60
            return end
end_time = time_end(L,dt,'2014-08-23 08:00:00')

    
    
    


# In[39]:


end_time


# In[20]:


dt['时间'][1]


# In[ ]:




