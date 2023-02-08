"""
    1
    1 2
    3 5 8
    13 21 34
    ...n
"""
n = int(input("Enter a number of row : "))

a = 0
b = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(b, end=" ")
        c = a + b
        a = b
        b = c
    print()
