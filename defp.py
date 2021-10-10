def p(a):
    r=0
    for i in range(2,a):
        if a%i==0:
            r=r+1
            break
    if r==0:
        return("It's Prime!")
    else:
        return("No, it's not Prime!")
b=int(input("Enter a Number"))
print(p(b))