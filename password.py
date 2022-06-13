password = 'a123456'
x = 3
x = int(x)
while True:
	password_answer = input('請輸入密碼： ')
	if password_answer == password:
		print('密碼正確')
		break
	elif password_answer != password and x != 1:
		x = x - 1 
		print('密碼錯誤，你還有', x, '次機會')
	else:
		print('你沒有機會了')
		break


