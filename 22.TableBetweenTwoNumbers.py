# WAP TO GET 2 NUMBER FROM THE USERS AND PRINT TABLE BETWEEN ALL THE NUMBRES USIGN WHILE AND FOR

n1 = int(input("Enter a 1st number : "))
n2 = int(input("Enter a 2nd number : "))

print("""
1. Table using for loop
2. Table using while loop
""")

choise = int(input("Enter your choise: "))

if choise == 1:
    for i in range(n1, n2+1):
        for j in range(1, 11):
            print(f"""{i} * {j} = {i * j}""")
        print()

elif choise == 2:
    while n1 <= n2:
        j = 1
        while j <= 10:
            print(f"""{n1} * {j} = {n1 * j}""")
            j += 1
        n1 += 1
        print()
        
else:
    print("Enter a valid choise")