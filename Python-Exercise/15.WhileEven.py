# WAP TO GET 2 NUMBER FROM THE USER AND PRINT EVEN NUMBER USING WHILE LOOP

n1 = int(input("Enter start number: "))
n2 = int(input("Enter end number: "))
i = n1
while i <= n2:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()
