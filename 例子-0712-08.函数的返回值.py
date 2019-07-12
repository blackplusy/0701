#coding=utf-8
#一个返回值
def sum(a,b):
    jisuan=a+b
    return jisuan
a=sum(10,20)
print(a)

#多个返回值
def ret(a,b):
    a*=10
    b*=10
    return a,b
num=ret(5,7)
print(num)
print(type(num))

num1,num2=ret(10,20)
print(num1)
print(num2)
