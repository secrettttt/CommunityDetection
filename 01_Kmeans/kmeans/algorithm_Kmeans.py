from numpy import *  
import pandas as pd 

#求这两个矩阵的距离，vector1、2均为矩阵 
def euclDistance(vector1, vector2):  
	return sqrt(sum(power(vector2 - vector1, 2))) 
  
#在样本集中随机选取k个样本点作为初始质心
def initCentroids(dataSet, k):  
	numSamples, dim = dataSet.shape    
	centroids = zeros((k, dim))  		
	for i in range(k):  
		index = int(random.uniform(0, numSamples))  
		centroids[i, :] = dataSet[index, :]  
	return centroids  
  
 
#dataSet为一个矩阵
def kmeans(dataSet, k):  
	numSamples = dataSet.shape[0]   
	clusterAssment = mat(zeros((numSamples, 2))) 
	clusterChanged = True  
  
   #在样本集中随机选取k个样本点作为初始质心
	centroids = initCentroids(dataSet, k)  
  
	while clusterChanged:  
		clusterChanged = False  
		for i in range(numSamples): 
			minDist  = 100000.0  
			minIndex = 0  
			#计算每个样本点与质点之间的距离，将其归内到距离最小的那一簇
			for j in range(k):  
				distance = euclDistance(centroids[j, :], dataSet[i, :])  
				if distance < minDist:  
					minDist  = distance  
					minIndex = j  
              
			#k个簇里面与第i个样本距离最小的的标号和距离保存在clusterAssment中
			#若所有的样本不在变化，则退出while循环
			if clusterAssment[i, 0] != minIndex:  
				clusterChanged = True  
				clusterAssment[i, :] = minIndex, minDist**2  
  
		for j in range(k):  
			pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]  
			centroids[j, :] = mean(pointsInCluster, axis = 0)  
	return centroids, clusterAssment  
  
#centroids为k个类别，其中保存着每个类别的质心
#clusterAssment为样本的标记，第一列为此样本的类别号，第二列为到此类别质心的距离 
def showCluster(dataSet, k, centroids, clusterAssment):  
    numSamples, dim = dataSet.shape       
    b = []
    for i in range(numSamples): 
        markIndex = int(clusterAssment[i, 0])
        b.append(markIndex)
    a = []
    for i in range(len(dataSet)):
        #dataSet中的节点的序号是从1开始的
        a.append(i+1)
 
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'row':a,'type':b})
 
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("Clust_Kmeans.csv",index=False,sep=',')