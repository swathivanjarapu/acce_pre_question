# n=int(input("enter number"))
# for i in range(1,n+1):
#     s="#"*i
#     print(s.rjust(n))

n=int(input("enter number"))
for i in range(1,n+1):
    s="#"*i
    print(s.ljust(n))
