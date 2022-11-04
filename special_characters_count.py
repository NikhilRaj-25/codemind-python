a=input()
l=a.split()
v="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
c=0
for i in l:
    for j in i:
        if j not in v:
            c+=1
print(c)