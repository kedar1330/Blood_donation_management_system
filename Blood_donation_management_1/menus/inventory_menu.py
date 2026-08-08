from services.inventory_services import *

def inventory_menu():
    pass
    while True:

        print("\n--- Blood Inventory Menu ---")
        print("1. Add Blood Inventory")
        print("2. View Blood Inventory")
        print("3. Update Blood Inventory")
        print("4. Delete Blood Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("How many blood records do you want to add? "))
        
            for i in range(n):
                print(f"\nEnter details for Blood Record {i+1}")
        
                blood_group = input("Enter Blood Group: ")
                units_available = int(input("Enter Units Available: "))
        
                add_blood_inventory(blood_group, units_available)

        elif choice == "2":

            inventory_list = view_blood_inventory()

            if inventory_list:

                print("\n------ Blood Inventory ------")

                for inventory in inventory_list:
                    print(inventory)

            else:
                print("No records found.")

        elif choice == "3":

            i_id = int(input("Enter Inventory ID to update: "))
            blood_group = input("Enter New Blood Group: ")
            units_available = int(input("Enter New Units Available: "))            
            update_blood_inventory(i_id, blood_group, units_available)
        elif choice == "4":
            i_id = int(input("Enter Inventory ID to delete: "))
            delete_blood_inventory(i_id)
        elif choice == "5":
            print("Exiting Blood Inventory Menu.")
            break

        else:

            print("Invalid Choice.")