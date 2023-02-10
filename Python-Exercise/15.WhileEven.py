# WAP TO GET 2 NUMBER FROM THE USER AND PRINT EVEN NUMBER USING WHILE LOOP

n1 = int(input("Enter start number: "))
n2 = int(input("Enter end number: "))

while n1 <= n2:
    if n1 % 2 == 0:
        print(n1, end=" ")
    n1 += 1
print()
