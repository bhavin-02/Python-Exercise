# WAP TO CHECK NUMBER IS ARMSTRONG OR NOT

n = int(input("Enter a number: "))
pw = int(input("Enter power of number: "))

sum = 0
for i in str(n):
    sum += int(i)**pw
if n == sum:
    print(n, "is armstrong number")
else:
    print(n, "is not armstrong number")
