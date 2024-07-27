#pascal triangle code

def fact(n):
    i=1
    s=1
    while i<=n:
        s=s*i
        i+=1
    return s


for i in range(0,6):
    for j in range(0,i+1):
        nm=fact(i)
        d1=fact(j)
        d2=fact(i-j)
        t=nm//(d1*d2)
        print(f"{t}",end=" ")
    print("\n")    
