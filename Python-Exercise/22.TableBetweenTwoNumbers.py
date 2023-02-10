# WAP TO GET 2 NUMBER FROM THE USERS AND PRINT TABLE BETWEEN ALL THE NUMBERS USING WHILE AND FOR

n1 = int(input("Enter a 1st number : "))
n2 = int(input("Enter a 2nd number : "))

print("""
1. Table using for loop
2. Table using while loop
""")

choice = int(input("Enter your choice: "))

if choice == 1:
    for i in range(n1, n2+1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")
        print()

elif choice == 2:
    while n1 <= n2:
        j = 1
        while j <= 10:
            print(f"{n1} * {j} = {n1 * j}")
            j += 1
        n1 += 1
        print()
        
else:
    print("Enter a valid choice")