
# from itertools import count
# input_1 = input("Enter option for user1: ")
# input_1 = input_1.lower()
# if input_1 != "scissors" or input_1 != "rock" or input_1 != "paper":
# 	for i in count():
# 		print("Dear user1,your input is invalid.please enter valid input")
# 		input_2 = input("Enter option for user1: ")
# 		if input_1 == "scissors" or input_1 == "rock" or input_1 == "paper":
# 			break
# elif input_1 == "scissors" or input_1 == "rock" or input_1 == "paper":
# 	 input_2 = input("Enter option for user2: ")
# 	 input_2 = input_2.lower()
# if input_2 != "scissors" or input_2 != "rock" or input_2 != "paper":
# 	for y in count():
# 		print("Dear user2,your input is invalid.please enter valid input")
# 		input_2 = input("Enter option for user2: ")
# 		if input_2 == "scissors" or input_2 == "rock" or input_2 == "paper":
# 			break
# else:

# 	if (input_1 == "scissors" and input_2 == "paper") or (input_1 == "paper" and input_2 == "rock") or (input_1 == "rock" and input_2 == "scissors"):
# 		print("User 1 wins!")
# 	else:
# 		print("user 2 wins")

import getpass
print("Welcome to:\n....Rock....\n.....Paper.....\n......Scissors......\nYou are about to play")
while True:
	try:
		number_of_games = int(input("How many times you would like to play RPS in this game: "))
		if number_of_games <= 0:
			raise ValueError
	except ValueError:
		print("I did not understand that.Please enter a valid number which is greater than 0")
		continue
	else:
		break
choice = ' '
user_1 = 0
user_2 = 0


while choice != 'Y' or choice != 'N':
	choice = input(f"You chose to play RPS {number_of_games} times.Would you like to continue (y/n) ").upper()
	if choice == 'Y' or choice == 'N':
		break
	if choice != 'Y' or choice != 'N':
		print("I did not understand that.Please enter a valid option")
while choice == 'Y':
	print("Game starts now. Good luck!!!")
	for r in range(number_of_games):
		input_1 = getpass.getpass("Enter option for user1: ")
		input_1 = input_1.lower()
		# check for valid input from user1
		if input_1 != "scissors" and input_1 != "rock" and input_1 != "paper":
			# If input is invalid,ask user input until the input is valid
			while  input_1 != "scissors" or input_1 != "rock" or input_1 != "paper":
				print("Dear user1,your input is invalid.please enter valid input")
				input_1 = getpass.getpass("Enter option for user1: ")
				if input_1 == "scissors" or input_1 == "rock" or input_1 == "paper":
					break
		input_2 = getpass.getpass("Enter option for user2: ")
		input_2 = input_2.lower()

		# check for valid input from user2
		if input_2 != "scissors" and input_2 != "rock" and input_2 != "paper":
			# If input is invalid,ask user input until the input is valid
			while  input_2 != "scissors" or input_2 != "rock" or input_2 != "paper":
				print("Dear user2,your input is invalid.please enter valid input")
				input_2 = getpass.getpass("Enter option for user2: ")
				if input_2 == "scissors" or input_2 == "rock" or input_2 == "paper":
					break
		# check the winner	
		if (input_1 == "scissors" and input_2 == "paper") or (input_1 == "paper" and input_2 == "rock") or (input_1 == "rock" and input_2 == "scissors"):
			print("User 1 wins!")
			user_1 += 1

		elif (input_2 == "scissors" and input_1 == "paper") or (input_2 == "paper" and input_1 == "rock") or (input_2 == "rock" and input_1 == "scissors"):
			print("user 2 wins") 
			user_2 += 1
		else:
			print("Tied") 
	if user_2 > user_1:
		print(f"User 2 won {user_2} times.So, User 2 wins")				
	elif user_2 < user_1:
		print(f"User 1 won {user_1} times.So, User 1 wins")
	elif user_1 == user_2:
		print("It's a tie")
	choice = ' '
	while choice != 'Y' or choice != 'N':
		choice = input("Would you like to play another game? (y/n) ").upper()
		if choice == 'Y' or choice == 'N':
			break
		if choice != 'Y' or choice != 'N':
			print("I did not understand that.Please enter a valid option")
	if choice == 'Y':
		while True:
			try:
				number_of_games = int(input("How many times you would like to play RPS in this game: "))
			except ValueError:
				print("I did not understand that.Please enter a valid number")
				continue
			else:
				break
		if number_of_games >= 0:
			print(f"You chose to play RPS {number_of_games} times")
			user_1 = 0
			user_2 = 0	
print("See you next time!.")




# from random import *


# computer = randint(0,2)
# computer = int(computer)
# if computer == 0: 
# 	computer = "scissors"
# elif computer == 1:
# 	computer = "paper"
# else:
# 	computer = "rock"
# input_2 = input("Enter option for user2: ")
	
# if (computer == "scissors" and input_2 == "paper") or (computer == "paper" and input_2 == "rock") or (computer == "rock" and input_2 == "scissors"):
# 	print("computer wins!")
# 	print("computer options is " + computer)
# elif (input_2 == "scissors" and computer == "paper") or (input_2 == "paper" and computer == "rock") or (input_2 == "rock" and computer == "scissors"):
# 	print("user 2 wins") 
# 	print("computer options is " + computer)
# else:
# 	print("Tied") 
# 	print("computer options is " + computer) 
# 	print("user2 option is " + input_2)