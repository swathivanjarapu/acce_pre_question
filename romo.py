# numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL",
#              50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
# num = int(input("enter digit:"))  # LVIII
# roman = ''
# for k, v in sorted(numerals.items(), reverse=True):
#     while num >= k:
#         roman += v
#         num -= k
# print(roman)

from itertools import count


# a=[2,1,2,2]
# i=0
# b=[]
# c=0
# while i <len(a):
#     c=a.count(a[i])
#     # d=a[i],c
#     i=i+1
# print(c)
#     j=1
#     while j<len(a):
#         if a[i]==a[j] and :
#             c=a[i],i
   
#         j=j+1
#     b.append(c)
#     i=i+1

# print(b)
# n=int(input("enter number"))
# s=input("enter string")
# s.split()
# print(s)
# i=0
# while i<len(s):
#     if s[i]==s[-1]:
#         print(s[i])
#         print("true")
#     else:
#         print("false")
#     i+=1

# def fun(a,b,c):
#     if a%b==0 and a%c==0:
#         print("true")
#     else:
#         print("false")
# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# fun(a,b,c)

def fun(a,b,c):
    return a%b==0 and a%c==0
    
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
print(fun(a,b,c))