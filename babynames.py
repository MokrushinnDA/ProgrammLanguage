# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:30:38 2021

@author: XTreme.ws
"""
import matplotlib.pyplot as plt
import pandas as pd
cols = ['names', 'gender','frequency']
years = range(1880,2010)
pieces=[]
for i in years:
    df=pd.read_table('C:/Users/XTreme.ws/Desktop/lab/babynames/yob%d.txt'%i, sep=',',engine='python', names=cols)
    df['year']=i
    pieces.append(df)
    data=pd.concat(pieces, ignore_index= True) 
"""mission2""" 
# mis2=data.groupby('gender').size()
# print(mis2)
"""mission3"""  
# Gcout=data.groupby(['year','gender']).size()
# print(Gcout)
# Y_F=[]
# Y_M=[]
# for i in range (0,262):
#     if i%2==0:
#         Y_F.append(Gcout.iloc[i])
#     else:
#         Y_M.append(Gcout.iloc[i])
# plt.plot(years,Y_F, label='F')
# plt.plot(years,Y_M, label='M')
# plt.legend()
"""mission4"""
proportion = []
data['proportion']=data['frequency'].apply(lambda x:x/1690784*100)
proportion.append(data)
data1=pd.concat(proportion, ignore_index= True)
"""mission5"""
num=1690784
Johnny=[]
Nat=[]
Bob=[]
Denis=[]
for i in years:
    J_sum=sum(data1[data1['names']=='Johnny']['frequency'])
    Johnny.append(J_sum/num)
    N_sum=sum(data1[data1['names']=='Natalie']['frequency'])
    Nat.append(N_sum/num)
    B_sum=sum(data1[data1['names']=='Bob']['frequency'])
    Bob.append(B_sum/num)
    D_sum=sum(data1[data1['names']=='Denis']['frequency'])
    Denis.append(D_sum/num)
plt.plot(years, Johnny, label='Johnny')
plt.plot(years, Nat, label='Natalie')
plt.plot(years, Bob, label='Bob')
plt.plot(years, Denis, label='Denis')
plt.legend()
"""mission6"""#not work
# cout=[]
# for  i in years:
#     data.sort_values(by="frequency", ascending=False)
# for i in range(131):     
#     print(data.head(i))
