s1 = "Maha Bharat"
# “mAHA bHARAT”
s2 = s1.swapcase()
print(s2)

# “Bharat”
s3 = s1.split()
print(s3[1])

# “BharatBharatBharat”
s4 = s3[1]*3
print(s4)

# “Mera Bharat”
s5 = "Mera " + s3[1]
print(s5)

# “Mera Bharat Mahan”
s6 = s5 + " Mahan"
print(s6)
