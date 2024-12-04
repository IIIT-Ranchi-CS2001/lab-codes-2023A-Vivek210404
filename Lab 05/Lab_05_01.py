import math
point1 = (3,4,5)
point2 = (7,1,9)
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
print(f"Distance between {point1} and {point2} is : {distance}")