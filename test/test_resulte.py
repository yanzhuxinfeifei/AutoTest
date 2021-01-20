'''
Author:田菲
Date:2020/10/26
Model:柠檬班ERP
varlist =['This', 'is', 3, 'demo', '!']怎么获取第2到第4个元素的值
'''
varlist =['This', 'is', 3, 'demo', '!']
# 获取到的列表的元素['is', 3, 'demo']
listValue=varlist[1:4]
# 获取到的列表的元素[3, 'demo', '!']
# listValue=varlist[2:5:1]
print(listValue)