def fun(a,m,rs):
    if a==m:
        return rs
    if a>m:
        c = a-m
        rs=rs-c
        return rs
    elif a<m:
        d =m-a
        rs=rs+d
        return  rs 
print(fun(4,4,6))
    