customer_data = [
    ('A', '01', 120),
    ('B', '02', 250),
    ('C', '03', 90)
]


sorted_customer_data = sorted(customer_data, key=lambda x: x[2])

print("Sorted customer data using sorted():")
print(sorted_customer_data)


customer_data_manual = [
    ('A', '01', 120),
    ('B', '02', 250),
    ('C', '03', 90)
]

n = len(customer_data_manual)
for i in range(n):
    for j in range(0, n-i-1):
        if customer_data_manual[j][2] > customer_data_manual[j+1][2]:
            customer_data_manual[j], customer_data_manual[j+1] = customer_data_manual[j+1], customer_data_manual[j]

print("Sorted customer data without using sorted() (Bubble Sort):")
print(customer_data_manual)
