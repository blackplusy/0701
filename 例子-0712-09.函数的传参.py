#coding=utf-8
#实参位置
def animal(pet1,pet2):
    print(pet1+'汪@@'+pet2+'喵！！！')
#调用函数时候传入2参数
animal('2ha','bosi')
animal('bosi','2ha')

#关键字
def animal(pet1,pet2):
    print(pet1+'汪@@'+pet2+'喵！！！')

animal(pet2='bosi',pet1='2ha')

#默认值
def animal(pet2,pet1='2ha'):
    print(pet1+'汪@@'+pet2+'喵！！！')

animal('bosi')
animal('jiafei','taidi')

#不定长参数

def test(x,y,*args):
    print(x,y,args)

test(1,2,'simida','go',1,2)

def test(x,y,**args):
    print(x,y,args)

test(1,2,a=10,b='gaga')












