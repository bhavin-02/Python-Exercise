# WAP to print 1 2 3 6 12 24...n

n = int(input("Enter a length of number : "))
a = 1
for i in range(1, n+1):
    if i <= 3:
        print(i, end=" ")
    else:
        print(a, end=" ")
        a = a * 2
print()

"""
1 4 9 16 25 36
 3 5 7  9  11
"""