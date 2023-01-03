# WAP TO GET 2 NUMBER FROM THE USER AND PRINT PELINDROME NUMBER

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

for i in range(n1, n2+1):
    # convert the number to a string
    num_str = str(i)
    # check if the number is a palindrome
    if num_str == num_str[::-1]:
        print(i)

# for i in range(n1, n2+1):
#     temp = i
#     rev = 0
#     n = 0
#     while (n > 0):
#         dig = i % 10
#         rev = rev * 10 + dig
#         n = i // 10
#     print(temp == rev)
    # if (temp == rev):
    #     print(i, "is a palindrome")
    # else:
    #     print(i, "isn't a palindrome!")
