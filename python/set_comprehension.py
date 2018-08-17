string = "hello"

answer = {(char if char in 'aeiou') for char in string}
print(answer)