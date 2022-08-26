# def OperationsBinaryString(str):
#     if str==None:
#          return -1
#     b=int(str[0])
#     i=1
#     while i<len(str):
#         if str[i]=='A':
#             b&=int(str[i+1])
#         elif str[i]=='B':
#             b|=int(str[i+1])
#         else:
#             b^=int(str[i+1])
#         i+=2
#     return b
# str=input()
# print(OperationsBinaryString(str))

#  def two_strings (string1,string2):
#     if len(string1)==len(string2):
#         if sorted(string1)==sorted(string2):
#             return 'Yes'
#         else:
#             return 'No'
# string1=input()
# string2=input()
# print(two_strings (string1,string2))
# def fun(a,b):
#     c=sorted(a)
#     d=sorted(b)
#     if c==d:
#         i=0
#         while i<len(c):
#             if c[i]==d[i]:
#                 return 'Yes'
#             else:
#                 return 'No'
# a=input()
# b=input()
# print(fun(a,b))


def anagram(a,b):
    if sorted(a)==sorted(b):
        return "Yes"
    else:
        return "No"
a=input()
b=input()
print(anagram(a,b))