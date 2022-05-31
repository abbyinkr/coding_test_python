N = 9
list1 = []

for i in range(N):
    list1.append(int(input()))
    
#print(list1)

list2 = list(sorted(list1, reverse=True))

print(list2[0])

print(list1.index(list2[0])+1)


