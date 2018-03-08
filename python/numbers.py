
for num in range(1,21):
	if num%2 == 0 and num != 4:
		print(f"number {num} is even")
	elif num%2 != 0 and num != 13:
		print(f"number {num} is odd")
	elif num == 4 or num == 13:
		print(f"number {num} is unlucky")
						