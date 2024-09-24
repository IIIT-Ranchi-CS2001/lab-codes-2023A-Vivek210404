n = int(input("Enter the number : "))
a =0
b=1
i=0
print(f"Fibonacci series of first {n} terms : ")
while(i<n):
    print(a,end=" ")
    x = a+b
    a=b
    b=x
    i=i+1
