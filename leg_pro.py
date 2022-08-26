t=int(input())
i=0
while i<t:
    c,d,l=map(int,input().split())
    
    total_leg=(c+d)*4
    min_cat=(c-d*2)
    if  total_leg>=l and l%4==0 or (d+min_cat)*4<=l:
        print("yes")
    else:
        print("no")
    i=i+1
    
    # if l<(c+d)*4  and l%4==0:
    #     print("yes")
    # elif l>(c-2(d))*4 and l%4==0:
    #     print("yse")
    # else:
    #     print("no")
    # i=i+1

# l=[23, 45 ,82, 27 ,66 ,12 ,78 ,13 ,71, 86 ]
# m=l[0]
# i=0
# while i<len(l):
#     if l[i]>m:
#         m=l[i]
#         j=i
#     i=i+1
# print(m)
# print(j)
