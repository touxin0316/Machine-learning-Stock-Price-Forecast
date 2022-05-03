import numpy as np
import matplotlib.pyplot as plt
import csv
import math
import random


bonus_input_datalist = []
predict_datalist = []
predict_timelist = []

with open('bonus_input.csv', newline='') as csvfile:
    bonus_input_datalist = np.array(list(csv.reader(csvfile)))
with open('predict_data.csv', newline='') as csvfile:
    predict_datalist = np.array(list(csv.reader(csvfile)))
with open('time.csv', newline='') as csvfile:
    predict_timelist = np.array(list(csv.reader(csvfile)))

#臺積概念股
MTK = []
FITI = []
GUC = []
MIC = []
TSMC_Price_Prediction = []
date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
MTK_p = []
FITI_p = []
GUC_p = []
MIC_p = []
time = []
for i in range(22) : 
  MTK.append(int(bonus_input_datalist[i]))
for i in range(22, 44) : 
  FITI.append(int(bonus_input_datalist[i]))
for i in range(44, 66) : 
  GUC.append(int(bonus_input_datalist[i]))
for i in range(66, 88) : 
  MIC.append(int(bonus_input_datalist[i]))
for i in range(88, 110) : 
  TSMC_Price_Prediction.append(int(bonus_input_datalist[i]))

for i in range(29) : 
  MTK_p.append(int(predict_datalist[i]))
for i in range(29, 58) : 
  FITI_p.append(int(predict_datalist[i]))
for i in range(58, 87) : 
  GUC_p.append(int(predict_datalist[i]))
for i in range(87, 116) : 
  MIC_p.append(int(predict_datalist[i]))
for i in range(20) : 
  time.append(predict_timelist[i])


#TSMC = np.array(TSMC).astype(int)
MTK = np.array(MTK).astype(int)
FITI = np.array(FITI).astype(int)
GUC = np.array(GUC).astype(int)
MIC = np.array(MIC).astype(int)
TSMC_Price_Prediction = np.array(TSMC_Price_Prediction).astype(int)
MTK_p = np.array(MTK_p).astype(int)
FITI_p = np.array(FITI_p).astype(int)
GUC_p = np.array(GUC_p).astype(int)
MIC_p = np.array(MIC_p).astype(int)

plt.scatter(date,MTK,s=50, alpha=0.3)
plt.scatter(date,FITI,s=50, alpha=0.3)
plt.scatter(date,MIC,s=50, alpha=0.3)
plt.scatter(date,GUC,s=50, alpha=0.3)


#合併矩陣
#x = np.concatenate((np.ones((x_datalist.shape[0],1)),x_datalist[:,np.newaxis]),axis=1)
x = np.concatenate((np.ones((MTK.shape[0],1)),MTK[:,np.newaxis]),axis=1)
x = np.concatenate((x,FITI[:,np.newaxis]),axis=1)
x = np.concatenate((x,MIC[:,np.newaxis]),axis=1)
x = np.concatenate((x,GUC[:,np.newaxis]),axis=1)

y = TSMC_Price_Prediction[:,np.newaxis]


#套用反矩陣公式

weight = np.matmul(np.matmul(np.linalg.inv(np.matmul(x.T,x)),x.T),y)
TSMC = []
print(weight)
for i in range(29) :
    TSMC.append((weight[0]+weight[1]*MTK_p[i]+weight[2]*FITI_p[i]+weight[3]*GUC_p[i]+weight[4]*MIC_p[i]).astype(int))
TSMC = np.array(TSMC).astype(int)

with open('107000109_bonus_prediction.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    i=0
    for row in TSMC:
      if i!=20 :
        writer.writerow([time[i][0].astype(str),int(row)]) 
      else :
        break 
      i+=1
