"""
    1
    3 5
    7 9 11
    13 15 17 19
    ...n
"""

n = int(input("Enter a number of row : "))
a = 1

for i in range(n):
    for j in range(i + 1):
        print(a, end=" ")
        a += 2
    print()
