a=input()
v=c=d=w=0
for i in a:
    if i in 'aeiouAEIOU':
        v+=1
    elif i.isdigit():
        d+=1
    elif i==' ':
        w+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)