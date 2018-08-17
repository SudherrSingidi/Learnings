def is_all_strings(all_strings):
    return all(n for n in all_strings if isinstance(n,str))

all_strings = [2,'c','a','d','e']
print(is_all_strings(all_strings))

#version 2

def is_all_strings_two(all_strings):
    return all(type(n) == 'str' for n in all_strings)
print(is_all_strings_two(all_strings))