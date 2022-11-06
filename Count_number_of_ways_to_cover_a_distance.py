def dist(a):
        if a<0:
            return 0
        elif a==0:
            return 1
        else:
            return dist(a-1)+dist(a-2)+dist(a-3)
ans=0
a=int(input())
ans=dist(a);
print(ans)