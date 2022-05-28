a=input()
b=input()
c=a+b
d=65
for i in range(70):
    for j in range(len(c)):
        if ord(c[j])==d:
            print(c[j],end='')
    d+=1