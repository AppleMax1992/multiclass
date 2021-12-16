# coding:utf-8
from numpy.lib.arraysetops import unique
from pandas.core.indexes.base import Index
import pymongo
import pandas as pd
import re
import collections
from sklearn import metrics
test = pd.read_csv('./test_samples.csv')
prediction = pd.read_csv('./submission_test.csv')
import matplotlib
#matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve

# 中文名	外文名	别名	拼音	国籍	本名	作者	类型	书名	作品名称
# df1 = test['中文名'] + prediction['中文名']
# df2 = test['外文名'] + prediction['外文名']
# df3 = test['别名'] + prediction['别名']
# df4 = test['拼音'] + prediction['拼音']
# df5 = test['国籍'] + prediction['国籍']
# df6 = test['本名'] + prediction['本名']
# df7 = test['作者'] + prediction['作者']
# df8 = test['类型'] + prediction['类型']
# df9 = test['书名'] + prediction['书名']
# df10 = test['作品名称'] + prediction['作品名称']
# res = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10],axis=1)
res = prediction
# 多分类设置阈值得问题




# 当阈值变小时，更多样本会被测试成飞机，虚线下移。假设取极限，阈值为0，那么所有样本都会被预测为飞机，召回率最大，为1；而精确率为 5/10 等于0.5。同理，阈值变大，虚线上移，精确率会变高，但召回率反而变低。

# 在设置阈值的时候，有两种方法：
# 1、从0-1之间按照等间隔设置，比如0，0.1，0.2，…，0.9，1.0。这样能得到10组 “p” “r” 值。当然也可以把间隔设置的小一点，可以得到更多组 “p” “r” 值。
# 2、把所有样本的概率预测值从小到大排序去重，并以此数列分别为阈值，进行计算 “p" “r” 值，可以得到更多组 “p” “r” 值。

res = res.applymap(lambda x: [0, 1][x>0.4])
# 0.4之后准确率反而会下降
# # 预测值
res.to_csv('merge_2.csv',index=None,encoding='utf_8_sig') 
test =  test[['中文名','外文名','别名','拼音','国籍','本名','作者','类型','书名','作品名称']]
label = ['name','foregin name','nickname','western script','country','original name','author','category','book name','title']
pred = res.to_numpy()
target = test.to_numpy()
print(target)
print("=================================")
print(pred)
print(metrics.accuracy_score(pred,target))
print(metrics.hamming_loss(pred, target))

# precision recall curve
precision = dict()
recall = dict()
for i in range(10):
    precision[i], recall[i], _ = precision_recall_curve(target[:, i],
                                                        pred[:, i])
    plt.plot(recall[i], precision[i], lw=2, label='{}'.format(label[i]))
    
plt.xlabel("recall")
plt.xlim(0.0,1.5)
plt.ylabel("precision")
plt.legend(loc="best")
plt.title("precision vs. recall curve")
plt.show()
# f1_score_micro = metrics.f1_score(test, res, average='micro')
# f1_score_macro = metrics.f1_score(test, res, average='macro')
# print(f"Accuracy Score = {accuracy}")
# print(f"F1 Score (Micro) = {f1_score_micro}")
# print(f"F1 Score (Macro) = {f1_score_macro}")