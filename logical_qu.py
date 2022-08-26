# list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# l=[1,2,3]
# m=[1,3,4]
# a=l+m
# a .sort()
# print(a)


# # i=0
# while i<len(l)
# n=input("enter symobl")
# print(reverse(n[-1]))
# # i=0
# while i<len(n):
#     j=1
#     while j<=len(n):
        
#         if n[i]==n[-j].reverse():
#             print(n[-j])
#             print("true")
#             break
#         else:
#             print("false")
#         j=j+1
#     i=i+1
# 85 25 65 21 84

# n=int(input("enter ur number"))
# i=0
# c=[]
# while i<n:
#     m=int(input("enter number"))
#     c.append(m)
#     j=0
#     b=0
#     while j<len(c):
#         b= b*10+c[j]%10
#         j=j+1
#     i=i+1
# print(b)
# if b%10==0:
#     print("yes")
# else:
#     print("no")

# def isValid(s: str) -> bool:
#     # Stack for left symbols
#     leftSymbols = []
#     # Loop for each character of the string
#     for c in s:
#         # If left symbol is encountered
#         if c in ['(', '{', '[']:
#             leftSymbols.append(c)
#             print( leftSymbols)
#         # If right symbol is encountered
#         elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
#             leftSymbols.pop()
#         elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
#             leftSymbols.pop()
#         elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
#             leftSymbols.pop()
#         # If none of the valid symbols is encountered
#         else:
#             return False
#     return leftSymbols == []
# s=input("enter symbol")
# print(isValid(s))

def fun(s):
    a=[]
    for i in s:
        if i in ['(','{','[']:
            a.append(i)
        elif i==')' and len(a)!=0 and a[-1]=='(':
            a.pop()
        elif i=='}' and len(a)!=0 and a[-1]=='{':
            a.pop()
        elif i==']' and len(a)!=0 and a[-1]=='[':
            a.pop()
        else:
            return False
    return a==[]
s=input("enter symbol")
print(fun(s))

