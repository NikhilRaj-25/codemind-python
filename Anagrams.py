def ana(a,b):
    l=len(a)
    c=0
    for i in b:
        if i in b:
            c+=1
    if(c==l):
        return 1
    else:
        return 0
a=input()
b=input()
if ana(a,b):
    print("True")
else:
    print("False")