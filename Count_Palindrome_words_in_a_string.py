def pali(a,b):
    a1=len(a)
    for i in range(a1):
        if a[i]==b[i]:
            continue
        else:
            return 0
    return 1
a=input()
l=a.split()
a1=a2=a3=""
c=0
for i in l:
    a1=i
    a2=i[::-1]
    a1=a1.lower()
    a2=a2.lower()
    if pali(a1,a2):
        c+=1
print(c)