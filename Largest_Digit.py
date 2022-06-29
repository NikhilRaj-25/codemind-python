a=int(input())
l=0
while a:
    r=a%10
    if r>l:
        l=r
    a=a//10
print(l)