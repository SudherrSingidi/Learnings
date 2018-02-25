#exercise 1

print("Hey there! please enter the number of kilometers you would like to convert")
kms = input()
miles = float(kms)/1.6094
print(f"equivalant to  {round(miles,2)}  miles")




#exercise 2
from random import randint
num = randint(1,200)
num = int(num%2)
print(f"number is {num}")
if num == 0:
    print("even")
else:
    print("odd")

