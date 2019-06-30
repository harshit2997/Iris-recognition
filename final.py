import os
import pickle as pk
from sklearn import svm
import numpy as np

train_feat =[]
train_lab =[]
test_feat=[]
test_lab=[]


#res in filenames is for resnet

f1= open("f_out_res","rb")
temp = pk.load(f1)
f1.close()

f2= open ("f_lab_res","rb")
temp2 = pk.load(f2)
f2.close()

for i in range(535):
	train_feat.append(temp[i].flatten())
	train_lab.append(temp2[i])

print "train feat loaded"

f1= open("f_out_res_test","rb")
temp = pk.load(f1)
f1.close()

f2= open ("f_lab_res_test","rb")
temp2 = pk.load(f2)
f2.close()

for i in range(214):
        test_feat.append(temp[i].flatten())
        test_lab.append(temp2[i])

print "test feat loaded"

clf = svm.SVC(gamma='scale', decision_function_shape='ovr')
clf.fit (train_feat, train_lab)

print "trained"

svm_test = clf.score(test_feat, test_lab)
print str(svm_test)

