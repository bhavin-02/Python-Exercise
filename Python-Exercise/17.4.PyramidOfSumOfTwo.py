"""
    1
    1 2
    3 5 8
    13 21 34 55
    ...n
"""
n = int(input("Enter a number of row : "))

a = 0
b = 1

for i in range(n):
    for j in range(i + 1):
        print(b, end=" ")
        c = a + b
        a = b
        b = c
    print()
