def iso(a):
    l=len(a)
    for i in range(l):
        for j in range(l):
            if a[i]==a[j] and i!=j:
                return 0
    return 1
a=input()
if iso(a):
    print("True")
else:
    print("False")