a,b=map(int,input().split())
while (b != 0):
    g = b;
    b = a % b;
    a = g;
print(a)