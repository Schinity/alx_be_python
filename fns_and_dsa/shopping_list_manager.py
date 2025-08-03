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
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Your shopping list is empty.")
                continue
            else:
                item_index = int(input("Enter the index of the item to remove: "))
                if 0 <= item_index < len(shopping_list):
                    removed_item = shopping_list.pop(item_index)
                    print(f"Removed '{removed_item}' from the shopping list.")
                else:
                    print("Invalid index. Please try again.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Shopping List:")
                for idx in range(len(shopping_list)):
                    item = shopping_list[idx]
                    print(f"{idx}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()