# WAP TO GET 2 NUMBER FROM THE USER AND PRINT PELINDROME NUMBER

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

for i in range(n1, n2+1):
    num_str = str(i)
    if num_str == num_str[::-1]:
        print(i)