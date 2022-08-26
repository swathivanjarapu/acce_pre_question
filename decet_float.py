# import re
# for _ in range(int(input())):
#     print(re.search(r'^([-\+])?\d*\.\d+$',input()) is not None)

class Main():
    def __init__(self):
        self= int(input())
        
        for i in range(self):
          n=input()
          
          if chr in n:
            print("False")
          elif "+" and "-" in n:
            print("False")
          elif ("+" or "-" or "." in n) and n.isdigit() and ("." in n ):
            print("True")
          else:
            print("False")
if __name__ == '__main__':
    obj = Main()

# import re

# class Main():
#     def _init_(self):
#         self.n = int(input())
        
#         for i in range(self.n):
#             self.s = input()
#             print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
                    
# if _name_ == '_main_':
#     obj = Main()


# count=int(input().strip())
# for _ in range(count):
#     ans=False
#     try:
#         string=input().strip()
#         number=float(string)
#         ans=True
#         number=int(string)
#         ans=False
#     except:
#         pass
#     print(ans)

https://www.codechef.com/MASH387