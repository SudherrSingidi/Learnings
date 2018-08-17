

##### 								Add items to lists using insert
# Insert - inserts an element into a list at a specified index: syntax - list.insert(index, list element)
# Extend - extends a list by adding a list of elements to a list: syntax - list.extend(['list element'])
# Append - Appends a single list item to the end of the list: syntax - list.append(list element)
friends = []
friends.extend(['sudheer','srujan','prudvi','nithin','raj','dinesh','daya','sandeep','xyz','dinesh'])
print(friends)


#######        Delete items from list - list.clear(), list.pop(), list.remove()

#clear an entire list
friends_clear = friends[:] # list slicing : list[start:stop:step]
friends_clear.clear()
print(friends_clear)
#Remove a list element using remove

friends_remove = friends[:]
friends_remove.remove('xyz')
print(friends_remove)

# Remove list elements using pop.pop() metod removes a list element at a specified index

friends_pop = friends[:]  # list slicing : list[start:stop:step]
friends_pop.pop(-1) # removes last element of the list .other syntaxes friends_pop.pop(len(friends_pop)) or  friends_pop.pop()
print(friends_pop)


#######    Find index of a specified list element   list.index() - return value error if the item we are looking for is not in the list

# passing a list item to find the index
friends_index = friends[:]
num = friends_index.index('sandeep')
print(num)

# specifying start and end positoins to find index. Syntax: list.index(list elemnt, start position, end position)
num = friends_index.index('dinesh', 4) # looks for 'dinesh' from index 4 (inclusive)
print(num)

num = friends_index.index('dinesh', 5 , 10) # looks for 'dinesh' from index 6(inclusive) to index 9(exclusive)
print(num)


###### findout the occurence of an item in the list - list.count()

friends_count = friends[:]
count = friends_count.count('dinesh')
print(count)


##### Revers the list items : list.reverse()
friends_reverse = friends[:]
friends_reverse.reverse()
print(friends_reverse)


##### sort the list :  list.sort()

friends_sort = friends[:]
friends_sort.sort()
print(friends_sort)

##### Join all list items to crate a string : 'list item seperator'.join(list name)

friends_join = friends[:]
string = ' | '.join(friends_join)
print(string)

##### SLICING lists

friends_slice_start = friends[1:]
print(friends_slice_start)


friends_slice_end = friends[:3]
print(friends_slice_end)

friends_slice_negative = friends[-1:]
print(friends_slice_negative)


friends_slice_step = friends[1::2]
print(friends_slice_step)


#### Reversing lists using slice

friends_reverse_slice = friends[::-1]
print(friends_reverse_slice)


#### replacing a portion of lists using slice

friends_replace_slice = friends[:]

friends_replace_slice[6:8] = ['daya','sandeep','dinesh','aravin']
print(friends_replace_slice)

##### reversing a list elemnt

friends_reverse_slice = friends[2][::-1]
print(friends_reverse_slice)

##### swapping values in lists

friends_swap = friends[:]
print(friends_swap)
friends_swap[0] , friends_swap[1] = friends_swap[1] , friends_swap[0]
print(friends_swap)

















































