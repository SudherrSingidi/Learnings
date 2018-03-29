##### accessing values in nested loops

numbers = [[1,2,3],[4,5,6],[7,8,9]]

print(numbers[2][1]) ## to print number 8


#### printing values in nested loop using loops

numbers = [[1,2,3],[4,5,6],[7,8,9]]

for n in numbers:
	for x in n:
		print(x)

#### using nested list comprehension

[[print(x) for x in n ]for n in numbers]


#### print board

print_board = [[x for x in range(1,5)] for n in range(1,5)]
print(print_board)


#### XOX


xox = [['X' if x%2 != 0 else 'O' for x in range(1,4)] for n in range(1,4)]
print(xox)

