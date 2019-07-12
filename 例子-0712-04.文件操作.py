#coding=utf-8
#文件读
file=open('d:\\test.txt','r')
for i in file:
    print(i)
file.close()

#文件写

'''
str1='emituofomemeda!'
file=open('d:\\test1.txt','w')
file.write(str1)
file.close()
print('已完成')
'''
#追加内容
#\n代表换行
file=open('d:\\test1.txt','a')
file.write('\n come on baby!!!')
file.close()
