# 1 2 3 6 12 24 48 ...N

# n = int(input("Enter a number : "))
n = 10
a = 1
for i in range(1 , n + 1):
    if (i <= 2):
        print(a)
        a += 1
    else:
        print(a)
        a *= 2