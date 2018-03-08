
# num = 1
# while num <= 10:
# 	print("\U0001f595 " * num)
# 	num += 1

# for num in range(1,11):
# 		print("\U0001f595 " * num)
# 		num += 1


n= max(range(1,21)) - 1
space = " " * n
for num in range(1,21,2):
	smiley = "\U0001f595" * num
	print(f"{space}{smiley}")
	num += 2
	n = n-1
	space = " " * n

