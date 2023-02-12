# WAP to print 1 4 9 16 25 36...n

n = int(input("Enter a length : "))
a = b = 1

for i in range(n):
    print(a, end=" ")
    b += 2
    a += b
print()
