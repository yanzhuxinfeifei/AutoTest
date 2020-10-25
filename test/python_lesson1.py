'''
1.for循环：用来遍历数据对象中的所有元素:str list tuple dict
  1).语法:
     for 变量名 in 数据对象:
         子代码(循环体)
     循环多少次由元素个数来决定
  2).循环终止
     break:终止循环
     continue:终止本次循环进行下一次循环
  3).range():内置函数，用来生成一个整数序列
     跟for循环一起使用：start:开始，stop:结束，step：步长
  4).count()计算元素个数
'''
# count=0
# list1=[20,"yanzhuxin",45.66,56,"yan"]
# for name in list1:
#     # print(name)
#     if name == "yanzhuxin":
#         # break
#        continue
#     count+=1
#     print(name)
# print(count)
# # range的使用
# print("range的使用")
# for number in range(1,5,1):
#     print(number)

'''
2.函数:
  将功能封装成函数，供对象调用，可以提高代码的复用率，提高代码执行效率
  1).语法:
     def 函数名():
         子代码(函数体)-- 实现功能
     注意:函数定义完成后，需要调用(通过函数名来调用)，没有调用不会执行
  2).函数里不固定的数据，需要在括号里定义成函数的参数
     形参:函数定义的时候定义的
     实参:参与逻辑运算，实际使用的参数
  3).参数定义的类型:
     必备参数:定义了就必须要传入的参数，不传会提示报错
     默认参数:缺省参数，可以定义的时候赋值一个默认值，调用的时候可以不传入；可以传代替默认值
     注意:默认参数必须在必备参数后面
     不定长参数:等前面的必备参数和默认参数都接受完，剩下的参数都给不定长参数接受
       *args: 接受不确定数量，个数的参数，可以不传，也可以传入多个(1个或者多个)，用元组接受
              传参方式为位置传参
       **kwargs:字典接受，传参方式为关键字传参
  4).传参的方式类型
     位置传参:按照位置参数传入
     关键字传参:指定参数名来进行传参，不关心顺序，比较可靠
     混合传参: 注意:关键字传参必须跟在位置传参后面
  5).返回值
     有进有出：参数进，返回值出
     返回值:函数可以给到外面的人用的数据，调用函数的时候，可以获得到这个返回值，使用return
     定义：使用return
     调用：变量接收返回值
     如果没有返回值则输出结果为None,有的话可以用return返回，可以有多个返回值用元组保存(多个返回值之间用逗号隔开)
  6).注意:返回值写在函数的最后，标志着函数的结束  
'''
# 函数的声明
# def function1(number1,number2,number3):
#     sum=number1+number2+number3
#     print(sum)
# # 函数的赋值及调用
# function1(12,54,67)
# *args的使用
# def function2(number1,number2,number3,*args):
#     sum1=number1+number2+number3
#     for i in args:
#         sum1 += i
#     print(sum1)
# function2(12,34,56,78,89,56,78,66,55)
# # **kwargs的使用
# def function2(number1,number2,number3,*args,**kwargs):
#     sum1=number1+number2+number3
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         sum1 += kwargs[j]
#     print(sum1)
# function2(12,34,56,78,89,56,78,66,55)
# def function3(salary,bonus,other):
#     print('''salary的值:{}'''.format(salary))
#     print('''bonus的值:{}'''.format(bonus))
#     print('''other的值:{}'''.format(other))
#
# function3(bonus=500,salary=300,other=100)
# # 返回值
# def function4(salary,bonus,other):
#     sum2=salary+bonus+other
#     sum3=salary+other
#     return sum2,sum3
#
# result1=function4(121,34,45)
# print(result1)
'''
3.内置函数
  print()
  input()
  type()
  isInstance()
  len()
  replace() count() find() index() append() insert() pop() remove() update()数据类型的内置方法
  str() float() int() list() tuple() dict() bool() set()
  range()
'''
'''
1. 把字符串转成列表 - list() 
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和 
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套 
'''
# 第一题
str1=["yan","zhu","xin",24,"haha"]
list1=list(str1)
print(isinstance(list1,list))
# 第二题
for sum  in range(1,5,1):
    sum += sum
print(sum)
# 第三题
str1=["yan","zhu","xin",24,"haha","xixi","heihei"]
if len(str1)>5:
    print("True")
else:
    print("False")
str2=["yan","zhu","xin"]
if len(str2)>5:
    print("True")
else:
    print("False")