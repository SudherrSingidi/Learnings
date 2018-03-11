# user = input("Computer Asking..... Hey how are you :")
# print(f"computer :{user}")
# while user != "stop":
# 	user1 = input("user :")
# 	if user1 == "stop":
# 		print("Computer : Dear user, Congratulations!!! you won the copy cat game")
# 		break
# 	else:
# 		print(f"Computer :{user1}")

# user = input("How are you :")
# while user != "stop":
# 	print(user)
# 	user = input()
# print("you win")

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through

i = 0  # i should be incremented by one each iteration
while  number != 5:
	
    print(number)
    number = randint(1,10)
    print(i)
    i += 1
    if number == 5:
    	print(number)
    	break

	