import random
r = random.randint(1,100)

while True:
	ans = input('請輸入您猜測的數字?(1~100整數)')
	ans = int(ans)
	if ans == r:
		print('您猜對了，恭禧!')
		break
	else:
		if ans > r:
			print('您猜的數字比答案大!再猜一次!')
		elif ans < r:
			print('您猜的數字比答案小!再猜一次!')