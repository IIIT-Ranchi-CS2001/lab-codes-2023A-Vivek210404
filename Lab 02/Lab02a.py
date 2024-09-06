s1 = "Maha Bharat"
# “mAHA bHARAT”
s2 = s1.swapcase()
print(s2)

# “Bharat”
print(s1[5:])


# “BharatBharatBharat”
print(s1[5:]*3)


# “Mera Bharat”
s3 = s1.replace("Maha","Mera")
print(s3)

# “Mera Bharat Mahan”
print(s3+" Mahan")
