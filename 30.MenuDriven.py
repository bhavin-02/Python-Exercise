while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("You have selected option 1.")
    elif choice == 2:
        print("You have selected option 2.")
    elif choice == 3:
        print("You have selected option 3.")
    elif choice == 4:
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please enter a valid choise.")