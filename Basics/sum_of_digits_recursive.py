n=int(input("n: "))
def sumd(n):
    if n==0:
        return 0
    else:
        return n%10+sumd(int(n/10))
print(sumd(n))
