t=int(input("enter"))
note=[100,50,5,2,1]
n=int(input("enter"))
c=0
for i in note:
    c+=n//i
    n%=i
print(c)
