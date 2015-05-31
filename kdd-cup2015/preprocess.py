import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

def evaluation(label,pred_label):
    num = len(label)
    logloss = 0.0
    for i in range(num):
        p = max(min(pred_label[i][label[i]-1],1-10**(-15)),10**(-15))
        logloss += np.log(p)
    logloss = -1*logloss/num
    return logloss


#save result as csv file
def saveResult(testlabel,filename = "submission.csv"):
    with open(filename,'wb') as myFile:
        myWriter=csv.writer(myFile)
        #myWriter.writerow(["id","Class_1","Class_2","Class_3","Class_4","Class_5","Class_6","Class_7","Class_8","Class_9"])
        id_num = 1
        for eachlabel in testlabel:
            l = []
            l.append(id_num)
            l.extend(eachlabel)
            myWriter.writerow(l)
            id_num += 1
            
'''
def svc_cross_val(data, label):
    #clf = SVC(C=1.0, kernel="rbf", cache_size=3000)
    #scores = cross_validation.cross_val_score(clf, data, label, cv=5)
    clf = LogisticRegression(C=1.0, intercept_scaling=1, dual=False, fit_intercept=True, penalty='l2', tol=0.0001)
    print cross_validation.cross_val_score(clf, data, label, scoring='average_precision')
    print cross_validation.cross_val_score(clf, data, label, cv=5, scoring='recall')
    print cross_validation.cross_val_score(clf, data, label, cv=5, scoring='f1')
    print cross_validation.cross_val_score(clf, data, label, cv=5, scoring='accuracy')
    print cross_validation.cross_val_score(clf, data, label, cv=5, scoring='roc_auc')
'''
