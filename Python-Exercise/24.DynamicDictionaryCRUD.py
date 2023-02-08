# WAP TO CREATE DICTION DYNAMICALLY AND PERFORM UPDATE DEL AND ADD ACTION

dictionary = {}

while True:
    print("1. View dictionary\n2. Add to dictionary\n3. Update dictionary\n4. Delete from dictionary\n5. Exit")
    choise = int(input("Enter your choise: "))
    if choise == 1:
        print("Dictionary is :", dictionary)
        print()

    elif choise == 2:
        length = int(input("Enter a length of dictionary: "))
        for i in range(1, length+1):
            key = input(f"Enter element {i} key: ")
            value = input(f"Enter element {i} value: ")
            dictionary[key] = value
        print("Dictionary is :", dictionary)
        print()

    elif choise == 3:
        print(dictionary)
        key = input("Enter a key which you want to update: ")
        value = input("Enter a value to update: ")
        dictionary.update({key: value})
        print("Dictionary is :", dictionary)
        print()

    elif choise == 4:
        print(dictionary)
        key = input("Enter a key which you want to delete: ")
        dictionary.pop(key, "Enter a valid key")
        print("Dictionary is :", dictionary)
        print()

    elif choise == 5:
        exit()
        
    else:
        print("Enter a valid choise")
