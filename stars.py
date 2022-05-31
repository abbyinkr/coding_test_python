# 2438 
n = int(input())
str = ''
for i in range(1,n+1):
    str += '*'
    print(str)

#2439
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ', end="")
    for j in range(i):
        print("*", end="")
    print()
    
#2440
n = int(input())
# range(start,end,step)
for i in range(n, 0, -1):
    print("*" * i)
    
#2441
n = int(input())
# range(start,end,step)
for i in range(0, n, 1):
    print(" " * i + "*" * (n-i))
    
#2442
n = int(input())
# range(start,end,step)
for i in range(1, n+1, 1):
    print(" " *(n-i) + "*" * ((2*i)-1))
    
#2443
n = int(input())
# range(start,end,step)
for i in range(n, 0, -1):
    print(" " *(n-i) + "*" * ((2*i)-1))
    
#2444
n = int(input())
# range(start,end,step)
for i in range(1, n, 1):
    
    print(" " *(n-i) + "*" * ((2*i)-1))
for i in range(n, 0, -1):
    print(" " *(n-i) + "*" * ((2*i)-1))


