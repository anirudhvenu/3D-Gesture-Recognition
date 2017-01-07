import sys
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
import random as rnd
#f=open("trainLabelData_freqCount.txt")
#g=open("testLabelData_freqCount.txt")
h=open("AllData_3.txt")
d=open("corrAllLabel_3.txt")
#data=np.loadtxt(g)
trainLabel1=data[:,0]
trainData1=data[:,1:]


#data2=np.loadtxt(f)
testLabel1=data2[:,0]
testData1=data2[:,1:]

allData=np.loadtxt(h)
allLabel=np.loadtxt(d)

#eff=[];
#for i in range(500,1000,100):
start=170
i=10
tsize=2

trainData=allData[start:i+start,:]
trainLabel=allLabel[start:i+start]
testData=allData[i+1:i+tsize,:]
testLabel=allLabel[i+1:i+tsize]
#testLabel=allData[i+1:335,0]

clf=svm.SVC(kernel='linear')
clf.fit(trainData,trainLabel)
acc=clf.score(testData,testLabel)
#j=range(355,356)
#p=np.array(allData.take(j))
#pred=clf.predict(allData[1,:])
#print pred
#print acc
#pred=clf.predict(X_test)

#eff.append((clf.score(testData,testLabel)))

#m=max(eff)
#ind=eff.index(m)
#print m 
#print ind 
#x=range(500,1000,100)
#import matplotlib.pyplot as plt
#plt.plot(x,eff)
#plt.ylabel('Efficiency')
#plt.xlabel('No of Training Examples')
#plt.show()

#print data.shape
#print data2.shape
print '0.64'

#from sklearn.preprocessing import normalize
# normData=normalize(t2)
# normData
