#! usr/bin/python
# -*-coding:utf-8 -*-

'''
Created on 2015��3��8��

@author: Administrator
'''

from numpy import *
# import os
import glob

#Read the file from the workspace
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\n')
        dataMat.append(int(lineArr[0]))
    return dataMat

#Counting the number times in the file 
def countNumber(fileTxtFile):
    dic = {}
    count = 0
    for number in fileTxtFile:
        if number in dic.keys():
            dic[number] += 1
        else:
            dic[number] = 1
        count = count + 1
    return dic, count

#main function
if __name__ == '__main__':
    for filename in glob.glob(r'rating2_user*.txt'):
        #Read *.txt file for data file
        fileTxt = loadDataSet(filename)
        dic, count = countNumber(fileTxt)
        
        #Put the dic into a list
        lineArr = []
        for line in dic:
            lineArr.append([int(line), float(dic[line]) / count])
        #print lineArr
        
        #Write the result to the file
        myfile = open("test.txt", 'w') 
        for line2 in lineArr:
            print line2[0], line2[1]
            myfile.write(str(line2[0]) + " " + str(float(line2[1])) + "\n")
    myfile.close()
