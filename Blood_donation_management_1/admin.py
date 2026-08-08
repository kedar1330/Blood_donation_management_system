from menus.inventory_menu import inventory_menu
from menus.hospital_menu import hospital_menu
from menus.blood_request_management_menu import blood_request_management_menu
def admin_menu():

    while True:

        print("\n========== ADMIN PANEL ==========")
        print("1. Blood Inventory")
        print("2. Request Management")
        print("3. Hospital Management")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            inventory_menu()

        elif choice == "2":
            blood_request_management_menu()


        elif choice == "3":
            hospital_menu()

        elif choice == "4":
            print("Invalid Choice.")