#coding: gbk
'''
Created on 2015年5月25日

@author: 3403
'''

'''
a = [1,2,5,1,2,3,5,6,6,5,4,6,4,2,0,8,9,7,4,1,1,2,2,2,2,2,2,2,2,3,3,3,2,5,2,5,8,5,5]
count = len(a)
myset = set(a)
for item in myset:
    print item,100*a.count(item)/count
'''
import numpy as np
import csv
import operator
import json

def readLogTrain(filename):
    index = 0
    reader = csv.reader(open(filename))
    dataMat = []
    for line in reader:
        if index !=0 :
            dataMat.append([int(line[0]), line[2], line[3]])
        index += 1
    
    return dataMat

def main():
    
    dataMat = readLogTrain("log_test.csv")
    
    n = 0
    result = []
    numList = []
    dataList = []
    
    csvfile = open("train.csv", "wb")
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'access', 'wiki', 'video', 'nagivate', 'page_close', 'problem', 'browser', 'discussion', 'server'])
    
    dic = {'server':0, 'browser':0, 'problem':0, 'video':0, 'access':0, 'wiki':0, 'discussion':0, 'nagivate':0, 'page_close':0}
    for data in dataMat:
        if len(numList) == 0:
            numList.append(data[0])
            
        if data[0] not in numList:
            numList.append(data[0])
            result.append(numList[n])
            
            for x in dataList:
                dic[x] = dataList.count(x)
                
            for item in dic.keys():
                result.append(dic[item])
        
            print result
            writer.writerow(result)
            result = []
            dataList = []
            dic = {'server':0, 'browser': 0, 'problem':0, 'video':0, 'access':0, 'wiki':0, 'discussion':0, 'nagivate':0, 'page_close':0}
            n += 1
            dataList.append(data[1])
            dataList.append(data[2])
        else:
            dataList.append(data[1])
            dataList.append(data[2])
                
    
    result.append(numList[n])
    
    for x in dataList:
        dic[x] = dataList.count(x)
    for item in dic.keys():
        result.append(dic[item])
    print result
    writer.writerow(result)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
