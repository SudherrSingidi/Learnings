#a made-up language formed from English by transferring the initial consonant or consonant cluster of each word to the end of 
#the word and adding a vocalic syllable (usually ˈpiɡ ˌlatn: so chicken soup would be translated to ickenchay oupsay . 

import re
def pig_latin(line):
    line_list = [i for i in line.split()]
    print(line_list)
    line_list_type = [type(n) for n in line_list]
    print(line_list_type)
    r_list = ' '.join((char if char.isdigit() else char [1:] + char[0] + 'ay') for char in line_list)
    # re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
    # return re.sub('[0-9][a-f]', '[0-9]', r_list)
    return r_list
line = input()
print(pig_latin(line))
