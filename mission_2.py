# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:36:13 2021

@author: XTreme.ws
"""
a = int(input("Введите число:"))

def Rek(a):
    if a == 1:
        return a
    else: 
        return a * Rek(a-1)
print(Rek(a))