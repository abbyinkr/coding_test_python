
str = list(input())
y = ''

for a in str:
    if(a in 'ABC'):
        y += chr(ord(a)+23)
    else :
        y += chr(ord(a)-3)
print(y)
