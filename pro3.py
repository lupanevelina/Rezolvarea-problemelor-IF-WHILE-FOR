m=int(input("Introdu numarul : "))
n=int(input("Introdu numarul : "))
p=0
if m<n:
     while m**p<=n:
        p+=1
        if m**p==n:
            print("Este puterea",p)
        
else:
    print("Nu este puterea")
