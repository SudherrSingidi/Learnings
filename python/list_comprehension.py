### Syntax :  [_____ FOR_____IN_____]

### list comprehension on numbers : multiply a list element by itself
nums = [2,4,6,8,10]
Y = [x*x for x in nums]
print(Y)

### list comprehension on characters : convert characters of a string to upper or lower case

name = "sudheer"
name_list = ['sudheer','srujan','prudvi','nithin','raj','dinesh','daya','sandeep','xyz','dinesh']

up = [x.upper() for x in name]  ## Upper
upp = [x.upper() for x in name_list] 
print(up)
print(upp)

low = [x.lower() for x in name]  ## lower
print(low)


#### converting first letters of a string to uppercase
name_list_1 = ['ashley','matt','michael']

Upper_char = [char[0].upper() + char[1::] for char in name_list_1]
print(Upper_char)


#### range with list comprehension

x = [n*10 for n in range(1,6)]
print(x)

##### boolean values with list comprehension

boolean = [bool(val) for val in [0,[],'',1,9]]
print(boolean)


##### converting numbers in a list to strings

numbers = [1,2,3,4,5,6,7]

str_val = [str(n) for n in numbers]
print(str_val)


