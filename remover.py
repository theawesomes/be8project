# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:40:51 2017

@author: Mitesh
"""

import os
l1=os.listdir(os.getcwd())
p1=[]
for ele in l1:
  if ele.startswith('tested'):
    p1.append(ele)
for path in p1:
    os.chdir(os.getcwd()+"\\"+path)
    l2=os.listdir(os.getcwd())
    for fi in l2:
        os.remove(os.getcwd()+"\\"+fi)
    os.chdir("..")
    os.rmdir(os.getcwd()+"\\"+path)
    
