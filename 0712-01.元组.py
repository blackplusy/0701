#coding=utf-8
a=(1)
print(a)
print(type(a))

b=(1,)
print(type(b))

tup=(1,2,3,4)
print(tup)

for i in tup:
    print(i)

#元组
tup=(1,2,3,4)
del tup
#print(tup)

#元组的切片和索引
tup=(3,5,7,9)
print(tup[0])
print(tup[-2])
print(tup[2:])
print(tup[:-2])
#元组补充
tup=(3,5,7,9,3)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(3))
print(tup.count(3))









