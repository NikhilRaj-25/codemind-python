a=input()
for i in range(len(a)):
    b=a.count(a[i])
    if b==1:
        print(i)
        break
else:
    print('-1')