'''Write a python program to find
a) Area and perimeter of triangle when all three sides are given(take user input)
hint : use heroine equation
b) find all three angles of the above triangle
Display inputs and outputs  20/08/2024'''

import math
a = float(input("Enter 1st side of triangle : "))
b = float(input("Enter 2nd side of triangle : "))
c = float(input("Enter 3rd side of triangle : "))
print("a = ",a)
print("b = ",b)
print("c = ",c)
perimeter = a+b+c 
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Perimeter = ",perimeter)
print("Area = ",area)

first_angle = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
second_angle = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
third_angle = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))

print("First Angle : ",first_angle)
print("Second Angle : ",second_angle)
print("Third Angle : ",third_angle)
