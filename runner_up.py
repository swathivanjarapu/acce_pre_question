# arr = map(int, input().split())
# print(arr)
n = int(input())
arr =map(int, input().split())
arr1=set(arr)
a=list(arr1)
m=max(a)
a.remove(m)
print(max(a))
  
        
  
        