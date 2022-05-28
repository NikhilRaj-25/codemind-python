a=input()
count=1
for i in range(1,len(a)-1):
    if a[i].isupper():
        count+=1
print(count)