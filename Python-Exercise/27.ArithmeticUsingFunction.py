# WAP TO PERFORM ARITHMATIC OPERATION USING FUNCTION

n1 = int(input("Enter a 1st number : "))
n2 = int(input("Enter a 2nd number : "))

def add():
    print(f"Addition of {n1} + {n2} =", n1 + n2)

def sub():
    print(f"Subtraction of {n1} - {n2} =", n1 - n2)

def mul():
    print(f"Multplication of {n1} * {n2} =", n1 * n2)

def div():
    print(f"Division of {n1} / {n2} =", n1 / n2)

def modulus():
    print(f"Modulus of {n1} % {n2} =", n1 % n2)

def expo():
    print(f"Division of {n1} ** {n2} =", n1 ** n2)

def fd():
    print(f"Floor Division of {n1} // {n2} =", n1 // n2)
    
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n7. Floor division")
choice = int(input("Enter your choice : "))

if choice == 1:
    add()

elif choice == 2:
    sub()

elif choice == 3:
    mul()

elif choice == 4:
    div()

elif choice == 5:
    modulus()

elif choice == 6:
    expo()

elif choice == 7:
    fd()

else:
    print("Please enter a valid choice")