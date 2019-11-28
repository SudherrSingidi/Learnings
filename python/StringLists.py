str = list(input("Enter the string you would like to perform a palindrome test on: "))
reversed_list = str[::-1]
if reversed_list == str:
    print("The string you enetered is a palindrome")
else:
    print("The string you enetered is NOT a palindrome")