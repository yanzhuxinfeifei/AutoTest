'''
1.列表
  1).元素可以是任意的数据类型:int float bool str list... list1=[20,"haha",45.78]
  2).取值:索引取值--类比字符串；取多个值使用切片
     扩展:列表的嵌套取值
  3).列表的元素是可以被改变的(增删改查)
     增:append() 默认追加元素到列表末尾
        insert() 指定位置进入元素插入 如list1.insert(4,"haha")
        extend() 两个列表合并
     删:pop() 默认删除最后一个元素，也可以指定位置(索引)进行删除
        clear() 清除所有元素
     改(取值--重新赋值): list1[4]="yanzhuxin"
  4).列表的元素是可以重复的，也就是说可以用来统计个数 count()
  5).len() 用来统计元素个数

'''
# list1=[20,"yanzhuxin",45.66,56,"yan"]
# list3=[1,2,3,4,5,6,7,8,9]
# print(list1)
# print(list1[1])
# print(list1[0:3:1])
# # append()只能传一个元素 ---增
# list1.append("xiao")
# # insert()只能传一个元素 ---增
# list1.insert(3,"bairu")
# # 两个列表合并  ---增
# list2=["zeng","zheng","li","duo"]
# list1.extend(list2)
# # pop()删除,默认删除最后一个  --删
# list1.pop(0)
# list1.pop()
# print(list1)
# print(list3)
# list3.clear()
# print(list3)
# # 修改 --取值-重新赋值
# list1[1] = "颜竹心"
# print(list1)
'''
2.元组
  1).元素可以是任意的数据类型:int float bool str list... tuplel=(20,"haha",45.78)
  2).取值:索引取值--类比字符串；取多个值使用切片
     扩展:列表的嵌套取值
  3).列表的元素是不可以被改变的 
  4).列表的元素是可以重复的，也就是说可以用来统计个数 count()
  5).len() 用来统计元素个数
  6).列表和元组之间可以进行相互转换，可以通过将元组转换为列表，修改数据成功后在转换成元组
'''
# tuple1=(20,"yanzhuxin",45.66,56,"yan")
# tuple2=(1,2,3,4,5,6,7,8,9)
# print(tuple1[3])
# list1=list(tuple1)
# print(isinstance(list1,list))
# list1.append("moweiyuansu")
# tuple3 = tuple(list1)
# print(isinstance(tuple3,tuple))
# print(tuple3)
# print(tuple3.count("yan"))
'''
3.字典 dict{key1:value1,key2:value2}
  1).元素:key: value【键值对】
  2).场景:存储数据属性：例如人的属性有姓名，身高，体重等
     key：不能是可以改变的数据类型，一般使用list和dict或者字符串str
          不能重复，必须是唯一的
     value:可以是任意数据类型，可以被改变，因此可以做增删改的操作
  3).字典是没有顺序的，因此不能使用索引取值，取值只能通过key来取 如:dict1["height"]  dict1.get["height"]
     取值需要注意的是，如果key存在，修改对应的key的value值，key不存在，新增加键值对
     字典的合并:update()
     删除:pop() 指定key删除，对应的键值对
          del 字典名 删除变量，变量不存在 
  4).len() 长度
'''
# dict1={"name":"yanzhuxin","age":24,"major":"computer","other":"haha"}
# dict2={"name":"hanhan","age":24,"major":"computer","other":"haha"}
# print(dict1)
# print(dict1["name"])
# dict1.pop("other")
# print(dict1)
# print(dict2)
# del dict2
# print(dict2)
'''
4.集合
集合：set{},元素单个
1).无序
2).元素不可以重复；使用场景可以用来做去重
3).可以将list转化为set来进行去重操作
'''
# list1=[20,"yanzhuxin",45.66,56,"yan","yanzhuxin"]
# print(list1)
# set1= set(list1)
# print(set1)

'''
5.控制流
  代码的执行顺序是从上到下依次执行:判断 循环
  1).if 语法
  if 条件： --条件成立--冒号：缩进(四个空格=tab键)
     子代码(执行语句)
  elif 条件: ---成立
     执行语句(子代码)
  ...(elif可以没有，可以有多个)
  else: --可以没有
     执行语句
  ...
'''
# score=125
# if  score>110:
#     print("成绩优异")
# elif score>100:
#     print("成绩优秀")
# elif score>70:
#     print("成绩良好")
# elif score>=60:
#     print("成绩及格")
# else:
#     print("成绩不合格，需要再好好努力一下!")

'''
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5 
注：num表示课堂人数。如果大于5，输出人数。 
3、list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面； 
方法2： 自动--dict（）
'''
# 第一题
a=[1,2,'6','summer']
print('i' in a)
# 第二题
dict_1={"class_id":45,'num':20}
perNum=dict_1["num"]
if perNum>5:
   print(perNum)
# 第三题
# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# list2= ['颜竹心','女', 24, '长沙']
# dict_2=dict(list2)
# print(list2)