#coding=utf-8
#访问字典
dic={'name':'gaga','age':18}
print(dic)
print(dic['name'])

#修改字典
dic={'name':'heygor','tel':18028768679}
print(dic)
dic['name']='simida'
print(dic)
dic['tel']=110
print(dic)

#删除字典
#del
dic={'name':'o8ma','tel':110}
print(dic)
del dic['tel']
print(dic)
del dic
#print(dic)
#clear
dic={'name':'o8ma','tel':110}
print(dic)
dic.clear()
print(dic)

#keys()
dic={'name':'o8ma','tel':110}
print(dic.keys())
for i in dic.keys():
    print(i)
#values()
dic={'name':'o8ma','tel':110}
print(dic.values())
for i in dic.values():
    print(i)

#items()
for i,j in dic.items():
    print(i,j)








