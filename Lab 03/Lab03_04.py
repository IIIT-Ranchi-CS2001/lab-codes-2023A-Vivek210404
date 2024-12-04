n = int(input("Enter a number : "))
l = int(input("Enter the specified limit : "))

print(f"Multiplication table of {n} upto the limit {l}: ")
for i in range(1,l+1):
    print(f"{n} X {i} = {n*i}")