# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:09:59 2019

@author: ASUS
"""
import csv
import numpy as np
from scipy.io import loadmat
from sklearn.decomposition import PCA 

#读取Coord文件
f_Coord = loadmat("Coord.mat")

#处理读出的数据
data = f_Coord['Coord']
print(len(data))

pca=PCA(n_components=2)
newData=pca.fit_transform(data)
print(newData)

name = np.zeros((len(data),1))
for i in range(0,len(data)):
    name[i] = int(i) + 1
newData = np.c_[name,newData]  


csvFile = open('network_point.csv','w', newline='')#设置newline，否则两行之间会空一行
writer = csv.writer(csvFile)
for i in range(0,len(data)):
    writer.writerow(newData[i])
csvFile.close()