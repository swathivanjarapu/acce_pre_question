# each character
# def strin(s):
#     a="hackerrank"
#     n=len(a)
    
#     i=0
#     for chr in s:
#         if chr==a[i]:
#             i+=1
#             if i==n:
#                 return "yes"
#     return "no"
# print(strin('hackerrank'))

# substring in string

from abc import abstractclassmethod
from re import S, T


# def substrin(string,sub):
#     l=len(sub)
#     c=0
#     for i in range(len(string)):
#         s=string[i:i+l]
#         if s==sub:
#             c+=1
#     return c
# print(substrin('abcdcdc','cdc'))

def solu(string,ending):
    if len(string)<len(ending): return False
    for (x,y) in zip(string[::-1],ending[::-1]):
        if x!=y:
            return False
    return True
print(solu('abcde','cde'))
print(solu('abcde',''))
print(solu('abcde','abc'))