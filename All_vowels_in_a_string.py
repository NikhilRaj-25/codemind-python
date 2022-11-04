a=input()
a1=['a','e','i','o','u']
a2=['A','E','I','O','U']
for i in a:
    if i in a1:
        a1.remove(i)
    elif i in a2:
        a2.remove(i)
if len(a1)==0 or len(a2)==0:
    print('True')
else:
    print('False')