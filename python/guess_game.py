# Using while loop.Infinite 

# from random import randint

# num = randint(1,10)

# user = int(input("Guess a number between 1 and 10: "))

# while user != num:
# 	if user < num:
# 		print("the number you guessed is too low")
# 		user = int(input("Please make another guess: "))
# 	elif user > num:
# 		print("The number you guessed is too big")
# 		user = int(input("Please make another guess: "))
# print(f"compurt is playing {num}.Good guess.You won this game")


#Using for loop.Limit the number of guesses to 3

# from random import randint

# num = randint(1,10)

# print(f"computer's choice is {num}")

# user = int(input("Guess a number between 1 and 10: "))
# decision = 'Y'

# # while decision != 'N':		
# if user != num:
# 	for i in range(1,4):
# 		if (i - max(range(1,4))) != 0 and user < num :
# 			print("the number you guessed is too low")
# 			n = int(max(range(1,4)))
# 			# print(f"i is :{i} and n is :{n}")
# 			attempts = n - i
# 			print(f"{i} attempt failed.remaining attempts {attempts}")			
# 			user = int(input("Please make another guess: "))
# 			i += 1
# 		elif (i - max(range(1,4))) != 0 and user > num:
# 			print("the number you guessed is too big")
# 			# print(f"{i}")
# 			n = int(max(range(1,4)))
# 			attempts = n - i
# 			# print(f"i is :{i} and n is :{n}")
# 			print(f"{i} attempt failed.remaining attempts {attempts}")
# 			user = int(input("Please make another guess: "))
# 			i += 1
# 		elif (i - max(range(1,4))) == 0 and user == num or (i - max(range(1,4))) != 0 and user == num:
# 			print("Good guess.You won the game")
# 			break			
# 		else:
# 			print("You have attempted maximum number of times:Better luck next time")
# else:
# 	print("Good guess.You won the game")

# # decision = input("Would you like to play another game : (Y/N)").upper()







#Using for loop.Limit the number of guesses to 3.repeat based on user input

from random import randint



decision = 'Y'

while decision != 'N':
	num = randint(1,10)
	user = int(input("Guess a number between 1 and 10: "))
	if user != num:
		for i in range(1,4):
			if (i - max(range(1,4))) != 0 and user < num :
				print("the number you guessed is too low")
				n = int(max(range(1,4)))
				# print(f"i is :{i} and n is :{n}")
				attempts = n - i
				print(f"Attempt {i} is unsuccessful.remaining attempts {attempts}")			
				user = int(input("Please make another guess: "))
				i += 1
			elif (i - max(range(1,4))) != 0 and user > num:
				print("the number you guessed is too big")				 
				n = int(max(range(1,4)))
				attempts = n - i
				# print(f"i is :{i} and n is :{n}")
				print(f"Attempt {i} is unsuccessful.remaining attempts {attempts}")
				user = int(input("Please make another guess: "))
				i += 1
			elif (i - max(range(1,4))) == 0 and user == num or (i - max(range(1,4))) != 0 and user == num:
				print("Good guess.You won the game")
				break			
			else:
				print("You have attempted maximum number of times:Better luck next time")
				break
	elif user == num:
		print("Good guess.You won the game")
	decision = input("Would you like to play another game (Y/N): ").upper()	
# elif decision == 'N':
# 	break

