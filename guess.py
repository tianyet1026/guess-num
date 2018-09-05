import random
uplimit = input('要猜數字範圍的上限值:')
uplimit = int(uplimit)
downlimit = input('要猜數字範圍的下限值:')
downlimit = int(downlimit)
r = random.randint(downlimit, uplimit)
i=0
while True:
	print(uplimit, '到', downlimit, '之間')
	ans = input('請輸入您猜測的數字?')
	ans = int(ans)
	i+=1 #i=i+1功能相同的速寫法
	if ans == r:
		print('您猜對了，恭禧!')
		print('已經猜了', i, '次')
		break
	elif ans > r:
		print('您猜的數字比答案大!')
	elif ans < r:
		print('您猜的數字比答案小!')
	print('已經猜了', i, '次')