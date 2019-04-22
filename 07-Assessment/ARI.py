# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:09:41 2019

@author: ASUS
"""

# coding=utf-8
import csv
import numpy as np
from scipy.io import loadmat
from sklearn import metrics

if __name__ == '__main__':
   
    '''
    获取真实的社区划分结果：trueResult
    '''
    #dat转txt
    import os
    files = os.listdir('.')
    for filename in files:
        portion = os.path.splitext(filename)
        #如果后缀是.dat
        if portion[1] == ".dat":  
        #重新组合文件名和后缀名
            newname = portion[0] + ".txt"   
            os.rename(filename,newname)
    
    #读取txt文件
    trueResult = np.loadtxt('community_mix1.txt')
    print(trueResult)
    tR=[]
    for i in range(len(trueResult)):
        tR.append(int(trueResult[i][1]))
    
    
    '''
    获得IsoFdp聚类结果的的ARI值
    '''
    #读取Clust文件
    f_Clust = loadmat("Clust.mat")
    #处理读出的数据
    IsoFdpResult=f_Clust['Clust']
    IFR=[]
    for i in range(0,len(IsoFdpResult[0])):
        IFR.append(int(str(IsoFdpResult[0][i])))  
     
    A = np.array(IFR)
    B = np.array(tR)
    IsoFdpARI = metrics.adjusted_rand_score(tR,IFR)
    print('IsoFdpARI:',IsoFdpARI)
    
    '''
    获得Kmeans聚类结果的的ARI值
    '''
    #读取Clust_Kmeans文件
    csv_file=open('Clust_Kmeans.csv')
    csv_reader_lines = csv.reader(csv_file)
    dat=[]
    row = 0
    for one_line in csv_reader_lines:
        dat.append(one_line)
        row += 1
    #处理读出的数据
    KR=[]
    flag=0
    #当flag=0时，k='row',v='value'，第0行没有数据;。
    for i in dat:
        if flag>0:
            KR.append(int(i[1]))
        flag += 1
        
    A = np.array(KR)
    B = np.array(tR)
    KmeansARI = metrics.adjusted_rand_score(tR,KR)
    print('KmeansARI:',KmeansARI)

    
    '''
    获得DBSCAN聚类结果的的ARI值
    '''
    #读取Clust_DBSCAN文件
    csv_file=open('Clust_DBSCAN.csv')
    csv_reader_lines = csv.reader(csv_file)
    dat=[]
    row = 0
    for one_line in csv_reader_lines:
        dat.append(one_line) 
        row += 1
    #处理读出的数据
    DBSR=[]
    flag=0
    #当flag=0时，k='row',v='value'，第0行没有数据;。
    for i in dat:
        if flag>0:
            DBSR.append(int(i[1]))
        flag += 1
        
    A = np.array(DBSR)
    B = np.array(tR)
    DBSCANARI = metrics.adjusted_rand_score(tR,DBSR)
    print('DBSCANARI:',DBSCANARI)
    
    '''
    结果可视化并以文件形式输出
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
    plt.figure(figsize=(8, 6), dpi=80)
    # 再创建一个规格为 1 x 1 的子图
    plt.subplot(1, 1, 1)
    # 柱子总数
    N = 3
    # 包含每个柱子对应值的序列
    values = (KmeansARI,DBSCANARI,IsoFdpARI)
    # 包含每个柱子下标的序列
    index = np.arange(N)
    # 柱子的宽度
    width = 0.35
    # 绘制柱状图, 每根柱子的颜色为绿色
    p2 = plt.bar(index, values, width, label="ARI", color="green")
    # 设置横轴标签
    plt.xlabel('Algorithm')
    # 设置纵轴标签
    plt.ylabel('ARI')
    # 添加标题
    plt.title('Assessment-ARI')
    # 添加纵横轴的刻度
    plt.xticks(index, ('Kmeans', 'DBSCAN', 'IsoFdp'))
    plt.yticks(np.arange(0, 1.2, 0.2))
    # 添加图例
    plt.legend(loc="upper right")
    plt.savefig("Assesement-ARI.png")
    plt.show()