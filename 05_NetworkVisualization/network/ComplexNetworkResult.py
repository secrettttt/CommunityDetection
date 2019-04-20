# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv 
import networkx as nx
import matplotlib.pyplot as plt
from scipy.io import loadmat

#读取network文件
f = open('network_mix1.dat','r')

#临时变量
temp = 0

#创建并初始化一个网络
G = nx.Graph()
while 1:
    data = f.readline();
    p = (data.split())
    G.add_edge(p[0],p[1]);
    temp += 1
    if temp == 19608:
        break
else:
    print('error')

#读取Clust文件
f_Clust = loadmat("Clust.mat")

#处理读出的数据
value=f_Clust['Clust']
k=[]
v=[]
for i in range(1,1001):
    k.append(str(i))
for i in range(0,1000):
     v.append(str(value[0][i]))

#生成字典：节点：类别
partition = dict(zip(k,v))

#颜色代码
cl=['b', 'g','r','c','m','k','w','y',
    '#D8BFD8','#FF6347','#40E0D0','#EE82EE','#F5DEB3','#BC8F8F',
    '#4169E1','#8B4513','#FA8072','#FAA460','#2E8B57','#FFF5EE',
    '#A0522D','#C0C0C0','#87CEEB','#6A5ACD','#3CB371','#7B68EE',
    '#00FA9A','#48D1CC','#C71585','#191970'
    ]

#打印网络的节点个数
print (G.number_of_nodes())

#数据可视化：输出划分前网络图
pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True, font_weight='bold'\
        ,node_size=1,font_size=1,width=0.1,node_color='b')
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #分辨率
plt.savefig("network.png")
plt.show()

#数据可视化：输出划分后网络图
count = 0
for com in set(partition.values()) :
    count += 1
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]                
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 1,\
                                node_color = cl[count%30],\
                                with_labels=True, font_weight='bold'\
                                ,font_size=1)
nx.draw_networkx_edges(G,pos,with_labels = True,width=0.1)

#去掉坐标轴和刻度：不知道为什么会自动生成？
plt.xticks([])
plt.yticks([])
plt.axis('off')

plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #分辨率
plt.savefig("networkResult_IsoFdp.png")
plt.show()


#读取Clust_Kmeans文件
csv_file=open('Clust_Kmeans.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
dat=[]    #创建列表准备接收csv各行数据
row = 0
for one_line in csv_reader_lines:
    dat.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中
    row += 1    #统计行数

#处理读出的数据
k=[]
v=[]
flag=0
#node0的位置是(0,0),原图没有。当flag=0时，k=row,v=value;当flag=1时，k=0,原图没有这个点。
for i in dat:
    if flag>1:
        k.append(i[0])
        v.append(i[1])
    flag += 1
#生成字典：节点：类别
partition = dict(zip(k,v))
print(partition)

#数据可视化：输出划分后网络图
count = 0
for com in set(partition.values()) :
    count += 1
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]                
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 1,\
                                node_color = cl[count%30],\
                                with_labels=True, font_weight='bold'\
                                ,font_size=1)
nx.draw_networkx_edges(G,pos,with_labels = True,width=0.1)

#去掉坐标轴和刻度：不知道为什么会自动生成？
plt.xticks([])
plt.yticks([])
plt.axis('off')

plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #分辨率
plt.savefig("networkResult_Kmeans.png")
plt.show()



#读取Clust_DBSCAN文件
csv_file=open('Clust_DBSCAN.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
dat=[]    #创建列表准备接收csv各行数据
row = 0
for one_line in csv_reader_lines:
    dat.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中
    row += 1    #统计行数

#处理读出的数据
k=[]
v=[]
flag=0
#node0的位置是(0,0),原图没有。当flag=0时，k=row,v=value;当flag=1时，k=0,原图没有这个点。
for i in dat:
    if flag>1:
        k.append(i[0])
        v.append(i[1])
    flag += 1
#生成字典：节点：类别
partition = dict(zip(k,v))
print(partition)

#数据可视化：输出划分后网络图
count = 0
for com in set(partition.values()) :
    count += 1
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]                
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 1,\
                                node_color = cl[count%30],\
                                with_labels=True, font_weight='bold'\
                                ,font_size=1)
nx.draw_networkx_edges(G,pos,with_labels = True,width=0.1)

#去掉坐标轴和刻度：不知道为什么会自动生成？
plt.xticks([])
plt.yticks([])
plt.axis('off')

plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #分辨率
plt.savefig("networkResult_DBSCAN.png")
plt.show()