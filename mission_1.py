# -*- coding: utf-8 -*-
txt = input("Введите что-нибудь:")
l1 = len(txt)
a_list = []
a_list += txt
a_list.insert(0,a_list[l1-1])
a_list.pop(l1)
a_list.insert(l1+1,a_list[1])
a_list.pop(1)
print (a_list)

