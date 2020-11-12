a=int(input("Introduceti lungimea laturii : "))
b=int(input("Introduceti lungimea laturii : "))
c=int(input("Introduceti lungimea laturii : "))
if ((a+b>c)and(a+c>b)and(b+c>a)):
    if ((a==b)and(a==c)and(b==c)):
        print("Formeaza un triunghi echilateral")
    elif ((a!=b)and(a!=c)and(b!=c)):
        print("Formeaza un triunghi scalen")
    else:
        print("Formeaza un triunghi isoscel")
else:
    print("Nu formeaza un triunghi")
 
