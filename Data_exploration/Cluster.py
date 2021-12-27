'''
don't know the explanation

'''


# from sklearn import datasets
# from sklearn import svm
# clf = svm.SVC(gamma=0.001, C=100.)
# digits = datasets.load_digits()
# clf.fit(digits.data[:-1], digits.target[:-1])
# x=clf.predict(digits.data[-1].reshape(1,-1))




'''
input:
result of an exam:

shorif -88.0,74.0,96.0,85.0
sadman -92.0,99.0,95.0,94.0
rakib  -91.0,87.0,99.0,95.0
siam   -78.0,99.0,97.0,81.0
rayhan -88.0,78.0,98.0,84.0
sabbir -100.0,95.0,100.0,92.0

output:
           [1 0 0 0 1 0]
           1= bad 
           0=good

'''

# import numpy as np
# from sklearn.cluster import KMeans
# list1 = [88.0,74.0,96.0,85.0]
# list2 = [92.0,99.0,95.0,94.0]
# list3 = [91.0,87.0,99.0,95.0]
# list4 = [78.0,99.0,97.0,81.0]
# list5 = [88.0,78.0,98.0,84.0]
# list6 = [100.0,95.0,100.0,92.0]
# X = np.array([list1,list2,list3,list4,list5,list6])
# kmeans = KMeans(n_clusters = 2).fit(X)
# pred = kmeans.predict(X)
# print(pred)


'''
who is good student who is not that good
'''



# import numpy as np
# from scipy.cluster.vq import vq, kmeans, whiten
# list1 = [88.0, 74.0, 96.0, 85.0]
# list2 = [92.0, 99.0, 95.0, 94.0]
# list3 = [91.0, 87.0, 99.0, 95.0]
# list4 = [78.0, 99.0, 97.0, 81.0]
# list5 = [88.0, 78.0, 98.0, 84.0]
# list6 = [100.0, 95.0, 100.0, 92.0]
# data = np.hstack([list1,list2,list3,list4,list5,list6])
# whiten = whiten(data)     # ---------calculate standard deviation
# centroids,_ = kmeans(whiten, 2) #----- kmeans is for data clustering
# result,_= vq(whiten, centroids)
# print(result)

