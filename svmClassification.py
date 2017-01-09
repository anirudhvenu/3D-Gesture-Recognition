import sys
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
import random as rnd
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
h=open("AllData_3.txt")
d=open("corrAllLabel_3.txt")

allData=np.loadtxt(h)
allLabel=np.loadtxt(d)

start=0
i=11000
tsize=1100

trainData=allData[start:i+start,:]
trainLabel=allLabel[start:i+start]
testData=allData[i+1:i+tsize,:]
testLabel=allLabel[i+1:i+tsize]

clf=svm.SVC(kernel='linear')
clf.fit(preprocessing.scale(trainData),trainLabel)
pred=clf.predict(testData)
confusion_matrix(allLabel[7000:8100],pred)

