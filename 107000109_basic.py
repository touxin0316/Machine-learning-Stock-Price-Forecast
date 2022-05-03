#!/usr/bin/env python
# coding: utf-8

# import packages
# Note: You cannot import any other packages!
import numpy as np
import matplotlib.pyplot as plt
import csv
import math
import random



# Global attributes
# Do not change anything here except TODO 1 
StudentID = '107000109' # TODO 1 : Fill your student ID here
input_dataroot = 'input.csv' # Please name your input csv file as 'input.csv'
output_dataroot = StudentID + '_basic_prediction.csv' # Output file will be named as '[StudentID]_basic_prediction.csv'

input_datalist =  [] # Initial datalist, saved as numpy array
output_datalist =  [] # Your prediction, should be 20 * 2 matrix and saved as numpy array
                      # The format of each row should be [Date, TSMC_Price_Prediction] 
                      # e.g. ['2021/10/15', 512]

# You can add your own global attributes here

train_data = []
validation_data = []
test_data = []


# Read input csv to datalist
with open(input_dataroot, newline='') as csvfile:
    input_datalist = np.array(list(csv.reader(csvfile)))

# From TODO 2 to TODO 6, you can declare your own input parameters, local attributes and return parameters
def SplitData():
# TODO 2: Split data, 2021/10/15 ~ 2021/11/11 for testing data, and the other for training data and validation data 


  #切前面的155作為training set
  for i in range(155) : 
    train_data.append(np.array(input_datalist[i][1:3]))
  #切後面的30作為validation set
  for i in range(155, 185) : 
    validation_data.append(np.array(input_datalist[i][1:3]))
  #未來的20作為test set
  for i in range(189, 209) : 
    test_data.append(np.array(input_datalist[i][1]))

def PreprocessData(x_datalist, y_datalist, x_validation, y_validation):
# TODO 3: Preprocess your data  e.g. split datalist to x_datalist and y_datalist

  for i in range(155) : 
    x_datalist.append(train_data[i][0])
    y_datalist.append(train_data[i][1])

  for i in range(30) : 
    x_validation.append(validation_data[i][0])
    y_validation.append(validation_data[i][1])


                      
def Regression(x_datalist, y_datalist, x_validation, y_validation):
# TODO 4: Implement regression
  x_datalist = np.array(x_datalist).astype(int)
  y_datalist = np.array(y_datalist).astype(int)
  x_validation = np.array(x_validation).astype(int)
  y_validation = np.array(y_validation).astype(int)
  x_square_datalist = []
  x_square_datalist = x_datalist**2
  x_tripple_datalist = []
  x_tripple_datalist = x_datalist**3
  #x_forth_datalist = []
  #x_forth_datalist = x_datalist**4

  #合併矩陣
  x = np.concatenate((np.ones((x_datalist.shape[0],1)),x_datalist[:,np.newaxis]),axis=1)
  x = np.concatenate((x,x_square_datalist[:,np.newaxis]),axis=1)
  x = np.concatenate((x,x_tripple_datalist[:,np.newaxis]),axis=1)
  #x = np.concatenate((x,x_forth_datalist[:,np.newaxis]),axis=1)
  y = y_datalist[:,np.newaxis]
  #套用反矩陣公式
  weight = np.matmul(np.matmul(np.linalg.inv(np.matmul(x.T,x)),x.T),y)
  return weight

def CountLoss(x_datalist, y_datalist, x_validation, y_validation, weight):
# TODO 5: Count loss of training and validation data
  x_datalist = np.array(x_datalist).astype(int)
  y_datalist = np.array(y_datalist).astype(int)
  x_validation = np.array(x_validation).astype(int)
  y_validation = np.array(y_validation).astype(int)
  MAPE = 0
  for i in range(30) :
    MAPE += abs((y_validation[i]-(weight[0]+weight[1]*x_validation[i]+weight[2]*(x_validation[i]**2)+weight[3]*(x_validation[i]**3)))/y_validation[i])
  MAPE = MAPE / 30
  return MAPE

def MakePrediction(test_data, weight):
# TODO 6: Make prediction of testing data 
  test_data = np.array(test_data).astype(int)
  for i in range(20) :
    output_datalist.append((weight[0]+weight[1]*test_data[i]+weight[2]*(test_data[i]**2)+weight[3]*(test_data[i]**3)).astype(int))
# TODO 7: Call functions of TODO 2 to TODO 6, train the model and make prediction 
x_datalist = []
y_datalist = []
x_validation = []
y_validation = []
SplitData()
PreprocessData(x_datalist, y_datalist, x_validation, y_validation)
w = Regression(x_datalist, y_datalist, x_validation, y_validation)
print(w)
MAPE = CountLoss(x_datalist, y_datalist, x_validation, y_validation, w)
print(MAPE)
MakePrediction(test_data, w)

# Write prediction to output csv
with open(output_dataroot, 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    i=0
    for row in output_datalist:
      writer.writerow([input_datalist[189+i][0],int(row)])  
      i+=1
