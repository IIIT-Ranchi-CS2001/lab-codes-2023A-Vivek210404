numbers = input("Enter numbers: ")
num_list = [int(x) for x in numbers.split()]

# Calculate mean
mean = sum(num_list) / len(num_list)
print(f"Mean: {mean}")


#Calculating median
num_list.sort()
n = len(num_list)
if(n%2==0):
    median = (num_list[n//2 - 1] + num_list[n//2])/2;
else:
    median = (num_list[n//2])

print(f"Median : {median}")

#Calculating Mode
frequency = {}
for num in num_list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_frequency = max(frequency.values())
modes = [num for num, freq in frequency.items() if freq == max_frequency]

if len(modes) == 1:
    print(f"Mode: {modes[0]}")
else:
    print(f"Modes: {modes}")
