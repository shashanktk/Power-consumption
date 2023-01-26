# -*- coding: utf-8 -*-
"""Power_consumption.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xGBSXaZ9WDeLYZ95tw6Kr3mm4KfvRQSa

# **Program to analyse the power consumption parameters during grinding operation**

How to use this program?



*   Firstly, gather the XML files from the operation done on the CNC machine
*   Upload those files into the notebook 
*   Now, change the path in the program according to the location of your file
*   Nextly, give the inputs for upper and lower limits of time values(of grinding area) based on the full scale graph which you can see
*   Finally, note down all the maximum values of the parameters during grinding operation
"""

from numpy.core.memmap import dtype
import matplotlib as matplotlib
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



with open('/content/trial 1_resin/RE_ABRASIVE_4.xml', 'r') as f:
        xml = f.read()

soup = BeautifulSoup(xml, 'xml')
# Get all 'rec' tags
recs = soup.find_all('rec')


# Get attribute value of attribute 'f3' from 'rec' tag
f1 = []
f2 = []
f3 = []
time = []

for rec in recs:
# print if present
  if rec.get('f1'):
    f1.append(rec.get('f1'))
  if rec.get('f2'):
    f2.append(rec.get('f2'))
  if rec.get('f3'):
    f3.append(rec.get('f3'))
  if rec.get('time'):
    time.append(rec.get('time'))


a = len(f1)
# print(a)
b = len(f2)
# print(b)
c = len(f3)
# print(c)
d = len(time)
# print(d)


#dataframes for each of the parameters(f1,f2,f3,time)
df1 = pd.DataFrame(f1, columns=['f1'])
df1['f1'] = df1['f1'].astype(float)

df2 = pd.DataFrame(f2, columns=['f2'])
df2['f2'] = df2['f2'].astype(float)

df3 = pd.DataFrame(f3, columns=['f3'])
df3['f3'] = df3['f3'].astype(float)

df4 = pd.DataFrame(time, columns=['time'])
df4['time'] = df4['time'].astype(float)


#concating all the dataframes into a single dataframe
frames = [df1,df2,df3,df4]
df = pd.concat(frames, axis = 1)

df

#plotting a full scale graph based on all the values(time and f3)
df.plot(x = 'time', y = 'f3')
plt.title('full scale plot')
plt.xlabel('time(s)')
plt.ylabel('f3(%)')
plt.savefig('plot.jpg', bbox_inches='tight', dpi=150)
plt.show()


#lower limit(time) of the grinding area
m = int(input('Lower limit of time:' ))
#upper limit(time) of the grinding area 
n = int(input('Upper limit of time:' ))

#picking out the values based on upper and lower limit
time_values = df.loc[(df['time'] > m)]
time_values = time_values.loc[time_values['time'] < n]
time_values

#plotting a graph at grinding operation
time_values.plot(x = 'time', y = 'f3')
plt.title('grinding operation plot')
plt.xlabel('time(s)')
plt.ylabel('f3(%)')
plt.savefig('plot1.jpg', bbox_inches='tight', dpi=150)
plt.show()


#printing the maximum values of all the parameters in the grinding area
print('max value of f1(W):',time_values['f1'].max())
print('max value pf f2(A):',time_values['f2'].max())
print('max value of f3(%):',time_values['f3'].max())
min_time = (time_values['time'].min())
max_time = (time_values['time'].max())
grinding_time =  n - m
print('actual grinding operation time(s):',grinding_time)