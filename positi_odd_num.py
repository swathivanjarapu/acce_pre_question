def odd_count(n):
    if n%2==0:
        return n//2
    else:
        return (n-1)/2
print(odd_count(int(input("enter number "))))