a=input()
b=input()
l1=a.split()
l2=b.split()
a1=[]
a2=[]
for i in l1:
    if i not in a1 and l1.count(i)==1:
        a1.append(i)
for i in l2:
    if i not in a2 and l2.count(i)==1:
        a2.append(i)
c=0
for i in a1:
    if i in a2:
        c+=1
print(c)