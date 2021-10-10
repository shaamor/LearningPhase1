n=int(input("Enter a number"))
def p(a):
    r=0
    for i in range(2,a):
        if a%i==0:
            r=r+1
            break
    if r==0:
        return(0)
    else:
        return(1)
for i in range (1,(n-2)):
    y=p(n-i)
    if y==0:
        if n%(n-i)==0:
            print(n-i)
            break