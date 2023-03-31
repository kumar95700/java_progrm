import pprint
inventory = {
             }
inventory1 = {'paint': 100,
             'wall_putty': 500,
             'roller': 100,
             'M.tape': 100 }

def add_new_item():
    for count in range(2):
        item_code = input("Enter the item code: ")
        no_of_item = input("Enter the number of items): ")
        inventory[item_code] = no_of_item
        count = count+1


def Delete_added_item():
    item_delete = input("Enter the item to be deleted:")
    if item_delete in  inventory:
        print("The key is present in the dictonary")
        del inventory[item_delete]
    else:
        print("key is not present in the dictonary")

def Display_Inventory():
    pprint.pprint(inventory)

def update_inventory():
    item_code = input("Enter the item code: ")
    print(type(item_code))
    update_inventory = input("Enter the number of items): ")
    inventory[item_code] = update_inventory


def main():
    while True:
        # Display the menu options
        print("..........................................")
        print("Menu:")
        print("1. Add item:")
        print("2. Delete item:")
        print("3. Display Inventory:")
        print("4. Update Inventory:")
        print("5. Exit Inventory:")
        print("..........................................")


        # Get the user's choice
        choice = input("Enter your choice (1-5): ")

        # Execute the corresponding code based on the user's choice
        if choice == 1:
            add_new_item()
        # Add code to execute Option 1 here
        elif choice == 2:
            Delete_added_item()
        # Delete Added item code Option 2 here
        elif choice == 3:
            Display_Inventory()
        # To display added item code 3 here
        elif choice == 4:
            update_inventory()

        elif choice == 5:    
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")



if __name__ == "__main__":
    main()

