"""
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    ...n
"""

n = int(input("Enter a number of row : "))

for i in range(1, n + 1):
    a = 0
    for j in range(0, i):
        a = j+1
        print(a, end=" ")
    print()
