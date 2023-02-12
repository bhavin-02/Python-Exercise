# WAP TO CREATE DYNAMIC LIST AND PRINT ALL NUMBER WITH POSITION (Use len() to find length)

list = []

length = int(input("Enter a length of list: "))
for i in range(length):
    value = input(f"Enter element {i + 1} value: ")
    list.append(value)
print()

for i in range(len(list)):
    print(f"Element at position {i + 1}: {list[i]}")
