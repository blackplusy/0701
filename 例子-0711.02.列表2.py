#coding=utf-8
#栈的方式访问列表
l=[1,2,3,4]
print(l)
l.append(5)
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.pop()
print(l)
#获取列表的索引
l=['2ha','taidi','keji','2ha']
print(l.index('2ha'))
print(l.index('keji'))

for index,values in enumerate(l):
    print('索引是：'+str(index)+'值是：'+values)
#列表的排序
l1=[1,3,2,4]
print(l1)
l1.reverse()
print(l1)
l=[1,3,5,2,4,6]
l.sort()
print(l)
l.sort(reverse=True)
#l.reverse()
print(l)
#列表推导式
#给定列表进行操作
a=[1,2,3,4]
print([3*x for x in a])
#没有给定列表进行操作使用range方法
print([3*x for  x in range(1,11)])
#加入if条件
print([x for x in a if x%2==0])
#多个for语句进行列表推导
print([[x,y] for x in range(2) for y in range(2)])








