# Print non unique numbers from a sequence
import re
def non_uniq(line):
 
    print(line)
    # number_list_updated = ''
    number_list_updated = ' '.join(num for num in line if line.count(num) > 1)
    # for num in line:
    #     count = line.count(num)
    #     if count > 1:
    #         number_list_updated = number_list_updated + ' ' + num    
    return re.sub(' +', ' ',number_list_updated)

line = input()
print(non_uniq(line))
