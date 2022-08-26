# n=int(input("enter ur number"))
# l=[]
# i=0
# while i<n:
#     a=input("enter number")
    
# a3b2c
# o/p=5
# a="a3b2c"
# i=0
# n=10
# c=""
# for i in range(0,len(a)-1,+2):
#     c=c+(a[i]*int(a[i+1]))
# # while i<len(a)-1:
# #     c+=a[i]*int(a[i+1])
# #     i+=2
# print(c)
# print(len(c))
# if len(c)>=n:
#     print(c[n-1])
# else:
#     print("-1")


a=[8,4,5,3,2,6,9,1]
i=0
c=[]
while i<len(a):
    j=i+1
    s=0
    su=0
    while j<len(a):
        if a[j]<a[i]:
            s+=a[j]
        else:
            su+=a[j]
        j+=1
    b=s*su
    c.append(b)
    # print(b)
    i=i+1
print(c)