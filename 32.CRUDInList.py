# CREATE A FUNCTION FOR ADD UPDATE AND DELETE DATA FROM THE LIST

list = []

def display():
    print("List is :", list)

def add():
    length = int(input("Enter a length of List: "))
    for i in range(1, length+1):
        value = input(f"Enter element {i} value: ")
        list.append(value)
    print("New List is :", list)

def update():
    print(list)
    index = int(input("Enter a index which you want to update: "))
    value = input("Enter a value to update: ")
    list[index] = value
    print("Updated List is :", list)

def delete():
    print(list)
    index = int(input("Enter a index which you want to delete: "))
    deleted = list.pop(index)
    print(f"Deleted value {deleted} from index {index}")
    print("List is :", list)

while True:
    print("1. View List\n2. Add to List\n3. Update List\n4. Delete from List\n5. Exit")
    choise = int(input("Enter your choise: "))
    if choise == 1:
        display()
        print()

    elif choise == 2:
        add()
        print()

    elif choise == 3:
        update()
        print()

    elif choise == 4:
        delete()
        print()

    elif choise == 5:
        exit()

    else:
        print("Enter a valid choise")
