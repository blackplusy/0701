#coding=utf-8
dic={'heygor':'123','admin':'888'}
while 1:
	name=input('请输入用户名')
	if name in dic.keys():
		print('yes')
		while 1:
			passwd=input('请输入您的密码：')
			if passwd==dic[name]:
				print('已经登陆')
				break
			else:
				print('请重新输入密码')
		break
		# if passwd in dic.values():
		# 	print('yes')
	else:
		print('重新输入')