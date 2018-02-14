# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:14:23 2018

@author: XuanHu
"""

import os

path = 'C:\\Users\\x1310\\Documents\\UCLA\\ee 211\\image'
filename='img'
i=0
print 'begin'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.jpg')>0:
            i+=1
            newname=filename+str(i)+'.jpg'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'   
print 'end' 