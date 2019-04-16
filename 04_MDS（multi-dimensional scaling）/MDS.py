# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:44:56 2019

@author: ASUS
"""
import csv
import numpy as np
from sklearn.manifold import MDS

#输入：边集.csv(要求点的坐标从1开始,依次递增1;34行减1是因为数组下标是从0开始)
#输出：点的坐标.csv
#三处需要更改：1,2,3

#1文件名
with open('network_mix1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    x = [row[0] for row in reader]
 
#2文件名
with open('network_mix1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[-1] for row in reader] 

xSet=set(x)
xIter=list(xSet)
for i in xIter:
    if i.isalnum()==False:
        xIter.remove(i)

data = np.zeros((len(xIter), len(xIter)))

for i in range(0,len(y)-1):
    data[int(x[i])-1][int(y[i])-1]=1

mds = MDS(dissimilarity='precomputed')

#输出的point是np数组,1000行2列
#给矩阵添加一列，https://blog.csdn.net/yan456jie/article/details/53997505
point = mds.fit_transform(data)
name = np.zeros((len(xIter),1))
for i in range(0,len(xIter)):
    name[i] = int(i) + 1
pointRes = np.c_[name,point]  

#3文件名
csvFile = open('network_mix1_point.csv','w', newline='')#设置newline，否则两行之间会空一行
writer = csv.writer(csvFile)
for i in range(0,len(xIter)):
    print(pointRes[i])
    writer.writerow(pointRes[i])
csvFile.close()

