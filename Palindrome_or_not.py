a=input()
a=a.lower()
b=a[::-1]
c=0
for i in range(len(a)):
    if a[i]==b[i]:
        c=2
    else:
        print('False')
        c=1
        break
if c==2:
    print('True')