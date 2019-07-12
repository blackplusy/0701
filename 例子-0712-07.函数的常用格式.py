#coding=utf-8

#无参数，无返回值
def print_hello():
    print('hello')

print_hello()
#无参数，有返回值
def sleep():
    return 'im sleeping!!!'
s=sleep()
print(s)
#有参数，无返回值
def sub(x,y):
    print('x+y=',x+y)
sub(10,20)
#有参数，有返回值
def sub(x,y):
    return x+y
s=sub(10,20)
print(s)
