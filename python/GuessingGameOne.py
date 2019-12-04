import random
a = random.randint(0,9)
user_count = 0
system_count = 0
no_of_correct_guesses = 0
number_of_guesses = 0
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
    a = random.randint(0,9)
    if user_input < a :
        print("Your guess is too low!")
    elif user_input > a :
        print("Your guess is too high")
    elif user_input == a :
        no_of_correct_guesses = no_of_correct_guesses + 1
        print(f"Congratulations!! Your guess: {user_input} matches with random number which is: {a}")
        continue
    choice = ' '
    while choice != 'Y' or choice != 'N':
        choice = input("Would you like to play another game? (y/n) ").upper()
        if choice == 'Y' or choice == 'N':
            number_of_guesses = number_of_guesses + 1
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
print(f"Total number of guesses attempted by user : {number_of_guesses}")
print(f"Total number of successfull guesses : {no_of_correct_guesses}")
print("see you next time!")

