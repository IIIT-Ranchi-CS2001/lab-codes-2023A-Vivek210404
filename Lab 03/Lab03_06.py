str = input("Enter a string : ")
char = input("Enter a character that you want to check in string : ")
count =0
for i in str:
    if(i==char):
        count += 1
print(f"Number of occurence of {char} in given string is {count}")