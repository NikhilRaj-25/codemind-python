a=int(input())
numbers=list(map(int,input().split()))
uniques= [ ]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
for i in uniques:
    print(i,end=' ')