# def interleaving(*args):
# 	list1 = ''
# 	list2 = ''
# 	list3 = []
# 	split_list = [arg for arg in args]
# 	merge_list = list(zip(split_list[0],split_list[1]))
# 	list1,list2 = ''.join(merge_list[0]),''.join(merge_list[1])
# 	list3.append(list1)
# 	list3.append(list2)
# 	return ''.join(i for i in list3)

# print(interleaving('hi','ho'))

def interleave(str1,str2):
	return ''.join(''.join(x) for x in (zip(str1,str2)))
str1 = input()
str2 = input()
print(interleave(str1,str2))
