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
'''
import keyword
# print(keyword.kwlist)
# int class=10
'''
2.python的基本语法
  1).Python对缩进非常敏感：只有存在父子关系才允许缩进(比如:函数或者条件判断、for循环)
  2).Python后没有分号
  3).Python对大小写异常敏感(因此在编码过程中需要格外之意)
'''

# print("python打印内容1")
'''
3.注解的使用(提高代码的可读性，方便自己也方便别人阅读，针对功能上的调整部分代码可以使用注解注掉防止后面会再度使用)
  1).单行注解：#
  2).多行注解：''''''【三单引】,""""""【三双引】
  3).注解的快捷键: ctrl+/ (按一次可以注掉相应的代码，再按可以取消注解)

'''
# print("python打印内容1")
# print("python打印内容2")
# print("python打印内容3")

'''
4.基本数据类型
  1).基本数据类型:int(整型)、float(浮点型)、Bool(布尔型--True(1)、False(0))、str(字符串)
  2).内置函数:type()--用来查验数据类型; isInstance()--用来判断是否属于某一指定的类型的数据，判断结果一般为布尔值
  3).字符串(str)：被成对的引号包裹的任何内容字符串--'',"","""""",''''''.
     1.引号嵌套:单 双 三
     2.三引号：可以保持格式--所见即所得等同于换行  
'''
print(type(12))
print((type('我是字符串数据一枚')))
print(isinstance(12,int))
print(isinstance('hahahaha',int))
print('''我是"python"小案例1''')
print("我是'python'小案例2")
print("我是'''python'''小案例3")
print('我是"python"小案例4')

# 引号嵌套的错误使用
# print('我是'python'小案例2')
# print("我是"python"小案例2")
# print('''我是'''python'''小案例2''')
