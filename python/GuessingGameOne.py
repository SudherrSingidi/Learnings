import random
a = random.randint(0,9)
print(a)
user_count = 0
system_count = 0
choice = 'Y'
while True:
    try:
        user_input = int(input("what is your guess :"))
    except ValueError:
        print("I did not understand that.Please enter a valid number")
        continue
    else:
        break
while choice == 'Y':
    if user_input < a :
        print("Your guess is too low!")
        system_count = system_count + 1
        print(choice)
    elif user_input > a :
        print("Your guess is too high")
        system_count = system_count + 1
    elif user_input == a :
        user_count = user_count + 1
        print(f"Congratulations!! Your guess: {user_input} matches with random number which is: {a}")
        choice = ' '
		while choice != 'Y' or choice != 'N':
			choice = input("Would you like to play another game? (y/n) ").upper()
			if choice == 'Y' or choice == 'N':
                break
            if choice != 'Y' or choice != 'N':
                print("I did not understand that.Please enter a valid option")
    if choice == 'Y':
        while True :
	        try :
                user_input = int(input("what is your guess : "))
            except ValueError:
                print("I did not understand that.Please enter a valid number")
                continue
            else :
                break
        if number_of_games >= 0:
			user_count = 0
			system_count = 0
print(user_input ,a)
print(system_count,user_count)

