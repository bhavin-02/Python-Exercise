"""
     1
     4 9
     16 25 36
     49 64 81 100
     ...n
"""

n = int(input("Enter a number of row : "))
a = 1
b = 1
i = 1

while i < n:
    j = 1
    while j <= i:
        print(a, end=" ")
        b += 2
        a += b
        j += 1
    i += 1
    print()
