s=input()
a=s.lower()
l=list(a)
c=0
if 'a' not in s:
    c+=1
    print('a',end=" ")
if 'e' not in s:
    c+=1
    print('e',end=" ")
if 'i' not in s:
    c+=1
    print('i',end=" ")
if 'o' not in s:
    c+=1
    print('o',end=" ")
if 'u' not in s:
    c+=1
    print('u',end=" ")
if c==0:
    print('0')