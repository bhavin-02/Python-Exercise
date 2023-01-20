# WAP TO PERFORM ARITHMATIC OPERATION USING FUNCTION

n1 = int(input("Enter a 1st number : "))
n2 = int(input("Enter a 2nd number : "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choise = int(input("Enter your choise : "))

def add():
    print(f"Addition of {n1} + {n2} =", n1 + n2)

def sub():
    print(f"Subtraction of {n1} - {n2} =", n1 - n2)

def mul():
    print(f"Multplication of {n1} * {n2} =", n1 * n2)

def div():
    print(f"Division of {n1} / {n2} =", n1 / n2)

if choise == 1:
    add()

elif choise == 2:
    sub()

elif choise == 3:
    mul()

elif choise == 4:
    div()

else:
    print("Please enter a valid choise")