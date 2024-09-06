Name = input("Enter Student's Name : ")
Roll = int(input("Enter Student's Roll Number : "))
Marks = int(input("Enter Student's Marks : "))
print("Name : " + Name)
print("Roll Number : ",Roll)
print("Marks : ",Marks)
if(Marks>=90):
    print("Grade Point : 10")
    print("Remarks : OUTSTANDING")
elif(Marks<90 and Marks>=80):
    print("Grade Point : 9")
    print("Remarks : VERY GOOD")
elif(Marks<80 and Marks>=70):
    print("Grade Point : 8")
    print("Remarks : GOOD")
elif(Marks<70 and Marks>=60):
    print("Grade Point : 7")
    print("Remarks : AVERAGE")
elif(Marks<60 and Marks>=50):
    print("Grade Point : 6")
    print("Remarks : PASS")
else:
    print("Grade Point : 0")
    print("Remarks : FAIL")