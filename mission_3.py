# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:45:13 2021

@author: XTreme.ws
"""
txt = input("Let's play a game:")
a = ['rock','paper','scissors']
if txt != a[0] and txt != a[2] and txt != a[1]:
    print("Введите правильные слова")
else:    
    from random import randint
    rand = randint(0,2)
    print("Computer says:"+a[rand])
if txt==a[2] and rand ==1:
    print("You won")
elif txt==a[2] and rand ==0:
    print("You lose")
elif txt==a[1] and rand ==0:
    print("You won")
elif txt==a[1] and rand ==2:
    print("You lose")
elif txt==a[0] and rand ==2:
    print("You won")
elif txt==a[0] and rand ==1:
    print("You lose")    
else: print("Draw")