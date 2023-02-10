# WAP TO GET 2 NUMBER FROM THE USER AND PRINT FIBONACCI SERIES.

n1 = int(input("Enter start number: "))
n2 = int(input("How many numbers you want to print?: "))

for i in range(n1, n2):
    if i <= 0:
        print("Incorrect input")
    elif i == 1:
        print(0, end=" ")
    elif i == 2:
        print(1, 1, end=" ")
    else:
        print((i-1) + (i-2), end=" ")
print()
