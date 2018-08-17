
# Version #1

def decrement_list(x):
    return x-1


nums = [1,2,3,4]
decremented_list = list(map(decrement_list,nums))
print(decremented_list)

#version 2

def decre_list(x):
	return list(map(lambda n: n-1,x))

user_input = input()
list_input = list(eval(user_input))
print(decre_list(list_input))

