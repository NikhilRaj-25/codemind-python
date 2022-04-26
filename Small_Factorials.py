a=int(input())
def fact(a):
    f=1
    for i in range (1,a+1):
       f=f*i
    print(f)
for j in range(1,a+1):
    b=int(input())
    fact(b)