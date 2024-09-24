str = input("Enter the sentence : ")

words = str.lower().split()


count = sum(word == word[::-1] for word in words)

print(f"Number of palindrome words: {count}")
