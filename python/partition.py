def isEven(num):
    return num%2 == 0

# partition([1,2,3,4], isEven) # [[2,4],[1,3]]

def partition(lst, fn = isEven):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

list = input()
print(partition(list))