# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 03:20:18 2021

@author: XTreme.ws
"""
import numpy as np
import pandas as pd
Data1=["user_id", "gender", "age","B","zip" ]
d1=pd.read_table("C:/Users/XTreme.ws/Desktop/lab/movielens/users.dat", sep="::", header= None
                 , engine="python", names=Data1)
Data2=["movies_id", "title", "genres"]
d2=pd.read_table("C:/Users/XTreme.ws/Desktop/lab/movielens/movies.dat",sep="::", header=None, 
                 engine="python", names=Data2)
Data3=["user_id", "movies_id", "rating", "timestap"]
d3= pd.read_table("C:/Users/XTreme.ws/Desktop/lab/movielens/ratings.dat",sep="::", header=None, 
                  engine="python", names=Data3)
data0 = pd.merge(d1, d3)
Data_result = data0.merge(d2)
# print(Data_result)
"""mission2"""
gender=pd.pivot_table (Data_result, values=["rating"], index=["gender"], aggfunc={"rating" : np.mean
})
# print(gender)
age=pd.pivot_table (Data_result, values=["rating"], index=["age"], aggfunc={"rating" : np.mean})
print(age)