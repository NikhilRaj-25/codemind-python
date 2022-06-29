a=int(input())
ans=[]
while a:
    rem=a%10
    ans.append(rem)
    a=a//10
for i in range(len(ans)):
    if ans.count(i)>1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')