#coding=utf-8

file=open('D:\\test.txt','r')
for i in file.readlines():
    #print(i)
    #print(type(i))
    i=i.strip('\n')
    #print(i)
    b=i.split(' ')
    if b[-1]=='18888888888':
        print('its here!')
        break
    #print(b)
file.close()
