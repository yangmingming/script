# -*- coding: utf-8 -*-
#以上方式支持utf-8

#脚本参数
from sys import argv

#判断文件是否存在
from os.path import exists

#一般打印
print "ymm"
#汉字打印
print "中国"
#参数打印+变量的使用
name = "ymm"
age = 20
print "my name is %s, I'm %d" %(name, age)

#%r打印
print "my name is %r, I'm %r" %(name, age)

#重复打印
print "*" * 20

#字符串拼接
str1 = "my "
str2 = "name "
str3 = "is "
str4 = "ymm "
print str1 + str2 + str3 + str4

#布尔类型打印
print "bool %r %r" %(True, False)

script, argv1, argv2 = argv
print "script:%s, argv1:%s, argv2:%s" %(script, argv1, argv2)

#用户输入
input_name = raw_input("input your name:")
input_age  = int(raw_input("input your age[int]:"))
print "input name:%s, input age:%d" %(input_name, input_age)

#函数的使用
def fun1(*args):
    argv1, argv2 = args
    print "function argv1:%s, argv2:%s" %(argv1, argv2)
def fun2(argv1, argv2):
    print "function argv1:%s, argv2:%s" %(argv1, argv2)

fun1("yang", "ming")
fun2("yang", "ming")

#文件读
print "read file %s" %script
fd = open(script)

#读第一行
print "read only one line"
print fd.readline()

print "seek 0"
fd.seek(0)

str = fd.read()
fd.close()

file = raw_input("Please input one output file :")
print "file [%s] is exists ? %r" %(file, exists(file))

#文件写
fd_w = open(file, "w")
fd_w.write(str)
fd_w.close()


"""
python ex22.py  1 2
  File "ex22.py", line 31
    printf "input name:%s, input age:%d" %(input_name, input_age)
                                       ^
SyntaxError: invalid syntax

Traceback (most recent call last):
  File "ex22.py", line 25, in <module>
    script, argv1, argv2 = argc
NameError: name 'argc' is not defined

Traceback (most recent call last):
  File "ex22.py", line 49, in <module>
    print fd.read_line()
AttributeError: 'file' object has no attribute 'read_line'
"""
