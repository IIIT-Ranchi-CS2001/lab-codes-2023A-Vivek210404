str = input("Enter the string : ")
alphanumeric = False
for char in str:
    if (not char.isalnum()):
        alphanumeric = False
        break
    else:
        alphanumeric = True

print(alphanumeric)