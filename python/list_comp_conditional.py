####  Using conditional logics in list comprehensions


#### If

numbers = [1,2,3,4,5,6,7,8,9,10]

evens = [num for num in numbers if num%2 == 0]
odds = [num for num in numbers if num%2 != 0]
print(evens)
print(odds)


###### if else

numbers = [1,2,3,4,5,6,7,8,9,10]

out = [n*3 if n%2 != 0 else n/2 for n in numbers]
out = [int(n) for n in out]
print(out)


### joining strings

vowels = "python is so much fun!!!"
join = [char for char in vowels if char not in 'aeiou']
join = ''.join(char for char in vowels if char not in 'aeiou')
print(join)


## swap list elements to make a meaningful sentence

sample = ['cool','dude','hey','......']
sample[0] , sample[1] , sample[2], sample[3] = sample[2] ,sample[3] ,sample[0],sample[1]

sample_final = ''.join(n for n in sample)
print(sample_final)


answer = [char[0] for char in ['Elie','Tim','Matt'] ]
print(answer)

answer2 = [n for n in [1,2,3,4,5,6] if n%2 == 0]
print(answer2)


### print union of two lists
answer = [n for n in [1,2,3,4] if n in [3,4,5,6]]
print(answer)


#### print all characters of a list item in reverse order
answer2 = [char[::-1].lower() for char in ['Elie','Tim','Matt']]
print(answer2)


#### print list of numbers between 1 and 100 that are divisible by 12
answer =  [n for n in range(1,101) if n%12 == 0]
print(answer)

### print only certain characters from a string
answer = [char for char in 'amazing' if char not in 'aeiou']
print(answer)