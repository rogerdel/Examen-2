# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:41:06 2020

@author: Roger
"""
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier


def preprocesing():
    data_csv = pd.read_csv("data.csv", header = None)
    
    data = np.array(data_csv)
    
    prep_data = []
        
    for i in data:
        if not("?" in i):
            i[1] = float (i[1])
            i[13] = float(i[13])
            prep_data.append(i)
      
    dic = {"+": 1, "-": 0}
    vals = [1 for i in range(len(prep_data[0]))]
    max  = [0 for i in range(len(prep_data[0]))]
    
    for i in range(len(prep_data)):
        for j in range(len(prep_data[0])):
            key = prep_data[i][j]
            if isinstance(key, str):
                if key not in dic:
                    dic[key] = vals[j]
                    vals[j]+=1 
                prep_data[i][j] = dic[key]
            else:
                if(key > max[j]):
                    max[j] = key
  
    for i in range(len(vals)):
        if vals[i] > 1:
            vals[i]-=1
        else:
            vals[i] = max[i]
    
    
    
    for i in range(len(prep_data)):
        for j in range(len(prep_data[0])):
            if(prep_data[i][j] > 2):
                prep_data[i][j] /= vals[j]
    
    return prep_data

    

def splitdata(data):
    ntr = (int)(len(data)*0.8)
    data_train = data[:ntr]
    data_test = data[ntr:]
    
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    
    for i in data_train:
        x_train.append(i[:-1])
        y_train.append(i[-1:][0])
    
    for i in data_test:
        x_test.append(i[:-1])
        y_test.append(i[-1:][0])
   

    x_train =np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    
    return x_train, y_train, x_test, y_test 


data = preprocesing()
x_train, y_train, x_test, y_test  = splitdata(data)

   

mlp = MLPClassifier(activation = "relu" ,solver = "adam", hidden_layer_sizes=(100, 100, 50,1), max_iter=500)
mlp.fit(x_train,y_train)

test = mlp.predict(x_test)

eval = 0

mc = np.zeros((2,2))
for i in range(len(y_test)):
    if(test[i] == y_test[i]):
        eval+= 1
        mc[test[i]][y_test[i]] += 1
    else:
        mc[y_test[i]][test[i]] += 1

eval = (eval/len(test))*100
print("Presicion: ","{:.2f}".format(eval)+"%")
labels = ["+", "-"]
print("    ",labels[0]," ", labels[1])
for i in range(len(mc)):
    for j in range(len(mc)):
        if(j == 0):
            print(labels[i], end = "   ")
        print(mc[i][j],end = " ")
    print()
        
