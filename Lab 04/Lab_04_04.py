singers_input = input("Enter names of singers : ").split()
dancers_input = input("Enter names of dancers : ").split()


singers = {singer for singer in singers_input}
dancers = {dancer for dancer in dancers_input}

print(f"Singers: {singers}")
print(f"Dancers: {dancers}")

# All artists: union of singers and dancers
all_artists = singers | dancers
print(f"All artists: {all_artists}")

# Allrounders: intersection of singers and dancers
allrounders = singers & dancers
print(f"Allrounders: {allrounders}")

# Dancers but not singers: difference of dancers and singers
dancers_not_singers = dancers - singers
print(f"Dancers but not singers: {dancers_not_singers}")

# Singers but not dancers: difference of singers and dancers
singers_not_dancers = singers - dancers
print(f"Singers but not dancers: {singers_not_dancers}")

# Dancers but not singers cum Singers but not dancers: symmetric difference
exclusive = dancers ^ singers
print(f"Dancers but not singers cum Singers but not dancers: {exclusive}")
