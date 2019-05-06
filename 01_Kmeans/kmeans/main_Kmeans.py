import numpy as np
import algorithm_Kmeans
   
#load data  
#列表，用来表示，列表中的每个元素也是一个二维的列表；这个二维列表就是一个样本，样本中包含有我们的属性值和类别号。
dataSet = []
#与我们所熟悉的矩阵类似，最终我们将获得N*2的矩阵，每行元素构成了我们的训练样本的属性值和类别号
fileIn = open("network_point.csv") 
for line in fileIn.readlines(): 
	temp=[]
	lineArr = line.strip().split(',')  #line.strip()把末尾的'\n'去掉
	temp.append(float(lineArr[1]))
	temp.append(float(lineArr[2]))
	dataSet.append(temp)
   #dataSet.append([float(lineArr[0]), float(lineArr[1])])  
fileIn.close()  
print(len(dataSet))

#clustering...  
#mat()函数是Numpy中的库函数，将数组转化为矩阵
dataSet = np.mat(dataSet)  
#在这里修改Kmeans的超参数k
k = 18  
#调用KMeans文件中定义的kmeans方法
centroids, clusterAssment = algorithm_Kmeans.kmeans(dataSet, k)
#show the result  
print ("cluster complete!"  )
algorithm_Kmeans.showCluster(dataSet, k, centroids, clusterAssment)