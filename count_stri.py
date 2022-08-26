def str(s):
    a=s.lower()
    b=" "
    for i in a:
        if i in b:
            pass
        elif i=="":
            pass
        else:
            b+=i+":"+("$"*a.count(i))+","
    return b[:-1]
print(str("accenture"))
    