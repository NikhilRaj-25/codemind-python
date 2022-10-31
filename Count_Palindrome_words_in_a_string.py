def pali(a):
    a=a.lower()
    b=a[::-1]
    c=0
    for i in range(len(a)):
        if a[i]==b[i]:
            c=2
        else:
            return 0
    return 1
a=input()
l=a.split()
c=0
for i in l:
    if pali(i):
        c+=1
print(c)