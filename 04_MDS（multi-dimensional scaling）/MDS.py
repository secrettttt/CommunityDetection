# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:44:56 2019

@author: ASUS
"""
import csv
import numpy as np
import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

data = np.zeros((1001, 1001))

with open('network_mix1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    x = [row[0] for row in reader]
    
with open('network_mix1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    y = [row[-1] for row in reader] 

for i in range(0,len(y)-1):
    data[int(x[i])][int(y[i])]=1
    
x = [x for x in range(1,1001)]
x.append(int(0))

y = [x for x in range(1,1001)]
y.append(int(0))

Word = pd.DataFrame( data , x , y )

mds = MDS(dissimilarity='precomputed')

point = mds.fit_transform(data)

csvFile = open('network_mix1_point.csv','w', newline='') # 设置newline，否则两行之间会空一行
writer = csv.writer(csvFile)
for i in range(1,len(point)):#从1开始是因为第一个点（0,0）是前面加上去的，没卵用
    writer.writerow(point[i])
csvFile.close()

