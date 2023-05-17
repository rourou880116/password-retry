password = "a123456"
x = 1
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		while x < 4:
			print('密碼錯誤 剩下可嘗試次數: ', 3 - x )
			x = x + 1
			break
	if x == 4:
		print('無法再登入')
		break