a=input()
b=a.lower()
c=0
for i in range(0,len(a)):
    if a[i]!=' ':
        if a[i]==b[i]:
            c+=1
print(c)