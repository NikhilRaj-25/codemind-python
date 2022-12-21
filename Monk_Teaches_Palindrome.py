def ispali(s,s1):
    for i in range(0,len(s)):
        if s[i]!=s1[i]:
            return False
    return True
for k in range(int(input())):
    s=input()
    s1=s[::-1]
    if(ispali(s,s1)):
        if(len(s)%2==0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')