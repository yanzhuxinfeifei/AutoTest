#python基础语法&基本数据类型
'''
1.命名规范(标识符--项目名 包名 文件名 方法名 变量名)
  1).只能包含数字、字母、下划线
  2).不能以数字开头
  3).不能用关键字来进行命名，但是可以使用关键字加字母或者数字进行组合命名(一般情况下如果使用关键字命名时文件会报错)
  print(keyword.kwlist)
  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
  'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  4).不同数字和字母之间使用下划线分割(易于阅读)
  5).可以使用驼峰命名进行类的命名(PythonLesson)
  6).见名知意
  7).变量一定要先声明(定义并赋值)在使用
'''
# number=12
# str1="颜竹心"
# print(number)
# print(str1)
'''
2.字符串的操作
1).取值：元素 位置(即就是索引),索引默认是从0开始
2).取多个值：使用切片--[开始索引:结束索引:步长](取值时取首不取尾)
   开头索引可以省略默认从0开始
   结束索引可以省略默认末尾结束
   步长可以省略默认值为1
3).负数:从右边开始取,如-1表示最后一个
4).元素个数：len()--为python的内置函数
5).替换字符串的元素:replace()【将字符串中的某一元素替换成指定的字符】,
   index()【获取指定字符，同时该方法在未找到指定元素时代码运行不报错，返回-1】,
   find()【获取指定字符，同时该方法在未找到指定元素时】,count()【计算指定字符在字符串中的个数】
6).
'''
# str2="wo shi yanzhuxin"
# print("索引为5的元素为:"+str2[5])
# print("多个字符的取值:"+str2[3:7:1])
# print("字符串的最后一位的字符为:"+str2[-1])
# # 注意使用len()内置函数时前面不要做字符串的拼接否则会报错
# print(len(str2))
# print(str2.replace("yanzhuxin","Yanzhuxin"))
# print(str2.index("th"))
# print(str2.find("th"))
'''
3.格式化输出
第一种：.format()--最常用
1). 占位符：{}传递变量，.format()
2). .format()可以默认按顺序传入变量，也可以从指定位置传入变量，需要注意的是不能混合使用
第二种：$s、$d、$f
1).$s(表示字符串)
2).$d(表示整数)
3).$f(表示小数)
'''
# name="颜竹心"
# age=18
# major="计算机"
# print('''----个人信息-----
# name:{0}
# age:{1}
# marjor:{2}
# '''.format(name,age,major))


'''
4.Python运算符
1).算术运算符：+ - * / % **
2).赋值运算符: = +=(如a+=等同于a=a+5) -=:等号右边的值赋给左边的变量
3).比较运算符: < <= > >= == !=(比较运算符的结果都为布尔值即就是True或者false)
4).逻辑运算符：and(与)真真为真、or(或)假假为假、非(not)
5).成员运算符：in、 not in
'''
# # 算术运算符实例
# str="yanzhuxin"
# print(10+45)
# print(78-45)
# # 赋值运算符实例
# number1=12
# number1=number1+34
# number2=345
# number3=45
# number3+=100
# number4=145
# print(number1)
# print(number1)
# # 比较运算符实例
# print(number1>number2)
# print(number1<number2)
# # 逻辑运算符实例
# print(12<10 and number2<number1)
# print(12>10 or number2<number1)
# # 成员运算符实例
# print("yan" in str)

'''习题
1.在控制台打印出以下格式的内容
请输入姓名：musne
请输入年龄：18
请输入性别：nan
******************
姓名：musne
性别: nan
年龄：18
******************
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？ 
3）替换python为 “lemon”. 
4) 找到aaa的起始位置
'''
enter_name=input("请输入姓名:")
enter_age=input("请输入年龄:")
enter_sex=input("请输入性别:")
print('''******************
姓名: {0}
性别: {1}
年龄：{2}
******************
# # '''.format(enter_name,enter_age,enter_sex))
# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6:1])
# print(str1.index('aaa'))
# print('o a' in str1)
# print('he' in str1)
# print('ab' in str1)











