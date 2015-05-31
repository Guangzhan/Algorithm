import numpy as np
import time
import preprocess
import csv

from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

#save result as csv file
def saveResult(testlabel,filename = "kdd-randomforest.csv"):
	with open(filename,'wb') as myFile:
		myWriter=csv.writer(myFile)
		#myWriter.writerow(["id","Class_1","Class_2","Class_3","Class_4","Class_5","Class_6","Class_7","Class_8","Class_10"])
		id_num = 1
		for eachlabel in testlabel:
			l = []
			l.append(id_num)
			l.extend(eachlabel)
			myWriter.writerow(l)
			id_num += 1

def loadTrainSet():
	traindata = []
	trainlabel = []
	#table = {"Class_1":1,"Class_2":2,"Class_3":3,"Class_4":4,"Class_5":5,"Class_6":6,"Class_7":7,"Class_8":8,"Class_10":10}
	with open("train.csv") as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			l = []
			for i in range(1,10):
				l.append(int(row[i]))
			traindata.append(l)
			trainlabel.append(row[-1])
	f.close()


	traindata = np.array(traindata,dtype="float")
	trainlabel = np.array(trainlabel,dtype="int")
	#Standardize(zero-mean,nomalization)
	mean = traindata.mean(axis=0)
	std = traindata.std(axis=0)
	traindata = (traindata - mean)/std
	
	#shuffle the data
	randomIndex = [i for i in xrange(len(trainlabel))]
	np.random.shuffle(randomIndex)
	traindata = traindata[randomIndex]
	trainlabel = trainlabel[randomIndex]
	return traindata,trainlabel
def loadTestSet():
	testdata = []
	with open("test.csv") as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			l = []
			for i in range(1,10):
				l.append(int(row[i]))
			testdata.append(l)
	f.close()
	testdata = np.array(testdata,dtype="float")
	#Standardize(zero-mean,nomalization)
	mean = testdata.mean(axis=0)
	std = testdata.std(axis=0)
	testdata = (testdata - mean)/std
	return testdata
def loaddata():
	print "loading data..."
	#load data in train.csv, divided into train data and validation data
	data,label = loadTrainSet()
	
	val_data = data[0:20000]
	val_label = label[0:20000]
	train_data = data[20000:]
	train_label = label[20000:]
	#load data in test.csv
	test_data = loadTestSet()
	return train_data,train_label,val_data,val_label,test_data




def rf(train_data,train_label,val_data,val_label,test_data,name="kdd-randomforest.csv"):
	print "Start training Random forest..."
	rfClf = RandomForestClassifier(n_estimators=300,n_jobs=-1)
	rfClf.fit(train_data,train_label)
	
	
	#evaluate on validation set
	print np.mean(cross_validation.cross_val_score(rfClf, val_data, val_label, cv=10, scoring='roc_auc'))
	
	'''#evaluate on validation set
	val_pred_label = rfClf.predict_proba(val_data)
	logloss = preprocess.evaluation(val_label,val_pred_label)
	print "logloss of validation set:",logloss
	'''

	print "Start classify test set..."
	test_label = rfClf.predict_proba(test_data)
	preprocess.saveResult(test_label,filename = name)



if __name__ == "__main__":
	t1 = time.time()
	train_data,train_label,val_data,val_label,test_data = loaddata()
	rf(train_data,train_label,val_data,val_label,test_data) 
	t2 = time.time()
	print "Done! It cost",t2-t1,"s"
