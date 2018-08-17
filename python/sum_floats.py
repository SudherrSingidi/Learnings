def sum_floats(*args):
    count = 0
    for arg in args:
        if type(arg) == float:
        	count = count + arg
    return count
print(sum_floats(1.2,3.4,'yes',1,9.8))