d = int(input("Enter the divisor : "))
l = []
for elem in range(1,d):
    if d%elem == 0:
       l.append(elem)
print (l)