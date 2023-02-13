# WAP TO CREATE DICTION DYNAMICALLY AND PERFORM UPDATE DEL AND ADD ACTION

dictionary = {}

while True:
    print("1. View dictionary\n2. Add to dictionary\n3. Update dictionary\n4. Delete from dictionary\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Dictionary is :", dictionary)
        print()

    elif choice == 2:
        length = int(input("Enter a length of dictionary: "))
        for i in range(length):
            key = input(f"Enter element {i + 1} key: ")
            value = input(f"Enter element {i + 1} value: ")
            dictionary[key] = value
        print("Dictionary is :", dictionary)
        print()

    elif choice == 3:
        print(dictionary)
        key = input("Enter a key which you want to update: ")
        value = input("Enter a value to update: ")
        dictionary.update({key: value})
        print("Dictionary is :", dictionary)
        print()

    elif choice == 4:
        print(dictionary)
        key = input("Enter a key which you want to delete: ")
        dictionary.pop(key, "Enter a valid key")
        print("Dictionary is :", dictionary)
        print()

    elif choice == 5:
        exit()
        
    else:
        print("Enter a valid choice")
