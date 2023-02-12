# WAP to print 1 2 3 6 12 24...n

n = int(input("Enter a length of number : "))
a = 3

for i in range(n):
    if i < 2:
        print(i + 1, end=" ")
    else:
        print(a, end=" ")
        a *= 2
print()