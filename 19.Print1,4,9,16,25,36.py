# WAP to print 1 4 9 16 25 36...n

n = int(input("Enter a length : "))
a = 1
b = 1

for i in range(1, n+1):
    print(a, end=" ")
    b += 2
    a += b
print()