t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    temp=-1
    a.sort()
    for i in range(n):
        if a[i]!=0 and a[i]!=temp:
            count+=-1
            temp=a[i]
    print(count)


