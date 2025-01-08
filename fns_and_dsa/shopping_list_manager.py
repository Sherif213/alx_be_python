def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input("Enter item name: "))
            pass
        elif choice == '2':
            removedItem = input("Enter item name: ")
            if removedItem in shopping_list:
                shopping_list.remove(removedItem)
            else:
                print("Item does not exist in the list") 
            pass
        elif choice == '3':
            for x in range(len(shopping_list)):
                print(f"item {x + 1} : {shopping_list[x]}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()