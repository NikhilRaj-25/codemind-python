a=int(input())
for i in range(a):
    st=input()
    for j in st:
        if j.isdigit():
            print('Yes')
            break
    else:
        print('No')