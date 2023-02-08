"""
    1
    3 5
    7 9 11
    13 15 17 19
    ...n
"""

n = int(input("Enter a number of row : "))
a = 0

for i in range(1, n+1):
    for j in range(1, i + 1):
        a += 1
        print(2 * a - 1, end=" ")
    print()
