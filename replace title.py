# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 10:14:27 2016

@author: PRANAV
"""
#from path import path
from os import listdir
import os
a=''
p=listdir(r'C:\Users\PRANAV\Documents\GitHub\My-best-programs')
#orca=p.files(pattern='*.py')
orca=[]
for elem in p:
    if elem.endswith('.py'):
        orca.append(elem)
def replace(a):
    ie=open(a,'r')
    pie=ie.read()
    ert=pie.replace('PRANAV','PRANAV')
    print(ert)
    ie.close()
    ei=open(a,'w')
    ei.write(ert)
    ei.close()
for elem in orca:
    replace(elem)



