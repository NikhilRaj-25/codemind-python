a=int(input())
for i in range(a):
    b=0
    s=input()
    for i in s:
        if  i.isdigit():
            b+=1
    if b==len(s):
        print('True')
    else:
        print('False')
