a=input()
b=input()
a=a.lower()
b=b.lower()
l1=a.split()
l2=b.split()
c=0
for i in l1:
    if i in l2:
        c+=1
print(c)