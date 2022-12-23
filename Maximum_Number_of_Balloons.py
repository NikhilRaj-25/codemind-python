s=input()
b=a=l=o=n=0
for i in s:
    if i=='b':
        b+=1
    elif i=='a':
        a+=1
    elif i=='l':
        l+=1
    elif i=='o':
        o+=1
    elif i=='n':
        n+=1
ans=0
while True:
    if b<1 or a<1 or l<2 or o<2 or n<1:
        break
    else:
        ans+=1
        b-=1
        a-=1
        l-=2
        o-=2
        n-=1
print(ans)