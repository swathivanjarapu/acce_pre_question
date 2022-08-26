def strin(s):
    if s==s[::-1]:
        return "yes"
    else:
        return "no"
print(strin("bab"))
