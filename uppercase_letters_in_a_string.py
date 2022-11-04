a=input()
b=a.upper()
c=0
for i in range(0,len(a)):
    if a[i]!=' ':
        if a[i]==b[i]:
            c+=1
print(c)