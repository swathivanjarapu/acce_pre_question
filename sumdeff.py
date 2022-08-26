def differenceofSum(n, m):
    i=1
    s=0
    s1=0
    while i<m:
        if i%4==0:
            s+=i
        else:
            s1+=i
        i+=1
    return s1-s
n=int(input(""))
m=int(input(""))
print(differenceofSum(n, m))
        