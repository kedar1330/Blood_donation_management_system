from admin import admin_menu
from menus.h_hospital_menu import h_hospital_menu
from hospital import *
from user import *
def main():

    while True:

        print("\n========== BLOOD DONATION MANAGEMENT SYSTEM ==========")
        print("1. Admin Panel")
        print("2. User Panel")
        print("3. Hospital Panel")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()

        elif choice == "2":
            user_panel()

        elif choice == "3":
            hospital_panel()

        elif choice == "4":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid Choice.")

main()