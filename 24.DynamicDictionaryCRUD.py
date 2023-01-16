# WAP TO CREATE DICTION DYNAMICALLY AND PERFORM UPDATE DEL AND ADD ACTION

print("""
1. View dictionary
2. Add to dictionary
3. Update dictionary
4. Delete from dictionary
""")

choise = int(input("Enter your choise: "))
dictionary = []

if choise == 1:
    print("Dictionary is :", dictionary)

elif choise == 2:
    length = int(input("Enter a length of dictionary: "))

    for i in range(1,length+1):
        j = input(f"""Enter element {i}: """)
        dictionary.append(j)

elif choise == 3:
    pass
elif choise == 4:
    pass
else:
    print("Enter a valid choise")

print("Dictionary is :", dictionary)