import math
a = int(input("Enter first coefficient of quadratic equation : "))
b = int(input("Enter second coefficient of quadratic equation : "))
c = int(input("Enter third coefficient of quadratic equation : "))

d = (b**2)-(4*a*c)

if(d==0):
    print("Both roots are same")
    print("First root : ",(-b/(2*a)))
    print("Second root : ",(-b/(2*a)))
elif(d>0):
    print("Both roots are real and distinct")
    print("First root : ",(-b+math.sqrt(d))/(2*a))
    print("Second root : ",(-b-math.sqrt(d))/(2*a))
else:
    print("Both roots are imaginary and exist in conjugate pair")
    real = -b/(2*a)
    imaginary = math.sqrt(-d)/(2*a)
    print("First root : ",real,"+",imaginary,"i")
    print("Second root : ",real,"-",imaginary,"i")