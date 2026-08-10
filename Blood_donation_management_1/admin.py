from menus.inventory_menu import inventory_menu
from menus.hospital_menu import hospital_menu
from menus.blood_request_management_menu import blood_request_management_menu
from menus.campaign_menu import *
from menus.donor_management_menu import donor_management_menu
def admin_menu():

    while True:

        print("\n========== ADMIN PANEL ==========")
        print("1. Blood Inventory Management")
        print("2. Blood Request Management")
        print("3. Hospital Management")
        print("4. Campaign Management")
        print("5. Donor Management")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            inventory_menu()

        elif choice == "2":
            blood_request_management_menu()


        elif choice == "3":
            hospital_menu()

        elif choice == "4":
            campaign_menu()

        elif choice == "5":
            donor_management_menu()

        elif choice == "6":
            print("Exiting Admin Panel.")
            break