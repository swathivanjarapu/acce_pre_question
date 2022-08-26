def one_sub(d,i):
    ave=0
    sum=0
    for key in d:
        sum+=d[key][i]
        
    print(sum/len(d[key]))
    return sum

def all_mark(d,i):
    i=0
    a=[]
    while i<3:
        x=one_sub(d,i)
        print(x)
        a.append(x)
        i+=1
    print(a)
    print(max(a))
    print(min(a))

d={"abi":[10,20,30],"biju":[60,23,45],"ruchi":[50,30,56]}
all_mark(d,0)