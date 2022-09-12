for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    ans=0
    for j in range(1,a+1):
        if(j%a==0 and j%b!=0):
            ans+=1
            if ans>=d:
                break
        elif(j%b==0 and j%a!=0):
            ans+=1
            if ans>=d:
                break
    if ans>=d:
        print('Win')
    else:
        print('Lose')