def temp(T):
      ans = [0 for i in range(len(T))]
      stack = []
      stack.append(0)
      i=1
      while i <len(T):
         while len(stack) and T[i]>T[stack[-1]]:
            index = stack[-1]
            ans[index] = i-index
            stack.pop()
         if not len(stack) or T[i]<=T[stack[-1]]:
            stack.append(i)
         i+=1
      return ans
a=int(input())
lst=list(map(int,input().split()))
print(*(temp(lst)))