# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 04:11:48 2022

@author: XTreme.ws
"""
class PC():
    def __init__(self,name,os,ram,gpu,cpu,temp):
        self.name = name
        self.os = str(os)
        self.used_ram=int(ram)
        self.gpu = gpu
        self.cpu=cpu
        self.temp=int(temp)
    def __repr__(self):
        return (f'Welcome to your PC: {self.name}, {self.os}, {self.ram}, {self.gpu}, {self.cpu}, {self.temp}')
    def reboot(self):
        self.temp=40
        self.used_ram=0
        print("Your PC was rebooted")
    def turn_on_fan(self):
        self.temp =- 15
    def Virtual_machine(self):
        if(self.used_ram>3):
            print("Too much Ram used now")
        else:
            print("Your virtyal machine is working now")
    def Game(self):
        if (self.used_ram<=2 and self.temp<=60):
            print("Run Game.exe")
        else:
            print("Clean your RAM and low down Temp")
    def Install_programm(self):
        if (self.os=="Windows_10"):
            print("Programm will install right now")
        else:
            print("Your os do not support this programm")
PC1 = PC('Xtreme.ws','Windows_10','3','GTX1660','AMD101','40')
PC2 = PC('DNS1','Windows_7','4','Radeon660','Intel3','30')   
PC3 = PC('Elbrus','Elbrus ver1.0','1','GPU E','Intel Core b3658','60')    
    