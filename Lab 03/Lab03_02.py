n = int(input("Enter a number : "))
sum = 0
a = n
while(n!=0):
    digit = n%10
    sum += digit
    n = n//10
print(f"Sum of digits of {a} is {sum}")