#coding=utf-8
#字符串的索引
str1='python is no.1'
print(str1[0])
print(str1[3])
print(str1[-2])
#print(str1[100])
#字符串的切片
name='www.baidu.com'
print(name[4:])
print(name[:-4])
print(name[4:-4])
print(name[4:9])
#字符串的拼接
a='python java php'
b=' no.1'
c=10
print(a+b)
print(a[:6]+' is'+b)
print(a+str(c))
#遍历
#for i in a:
#    print(i)
#去空格
a='   heygor   '
print(a.strip())
print(a.lstrip())
print(a.rstrip())
'''
name=input('请输入您的名字，不能超过3字')
if len(name)>=3:
    print('超了')
else:
    print(name)
'''
#引号
print('im your baba')
print("im your papa")
print('''im your dady!''')
#print('i'm your baba')
print("i'm your dady!")

print('''
老子吃火锅
你吃火锅底料
对你笑呵呵
因为我讲礼貌
''')







