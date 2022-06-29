a=int(input())
for i in range(1,(a//2)+1):
    if i*(i+1)==a:
        b=1
        print('YES')
        break
else:
    print('NO')