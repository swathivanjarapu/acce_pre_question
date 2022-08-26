from re import A


def stri(n):
    vowel='aeiou'
    for i in vowel:
        a=n.replace(i,'')
        a=n.replace(i.upper(),'')
    return a

print(stri('This is Wonderfull Moment'))