# WAP TO CREATE DICTIONARY

length = int(input("Enter a length of dictionary: "))
dictionary = {}

for i in range(1,length+1):
    dictionary[i] = f"val {i}"

print("Dictionary is :", dictionary)