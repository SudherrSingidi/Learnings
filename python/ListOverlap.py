import random
a = int(input("enter the max range of random numbers you would like to generate for list 1: "))
b = int(input("enter the max range of random numbers you would like to generate for list 2: "))
first_list = []
second_list = []
common_elements = []
for i in range(a):
    first_list.append(random.randint(0,a))
for j in  range(b):
    second_list.append(random.randint(0,b))
if len(first_list) > len(second_list):
    for x in second_list:
        if x in first_list:
            common_elements.append(x)
if len(first_list) < len(second_list):
    for x in first_list:
        if x in second_list:
            common_elements.append(x)
if len(first_list) == len(second_list):
    for x in second_list:
        if x in first_list:
            common_elements.append(x)
print(first_list)
print(second_list)
print(common_elements)