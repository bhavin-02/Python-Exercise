# WAP TO CREATE DICTIONARY

length = int(input("Enter a length of dictionary: "))
dictionary = {}

for i in range(length):
    dictionary[i] = f"val {i + 1}"

print("Dictionary is :", dictionary)