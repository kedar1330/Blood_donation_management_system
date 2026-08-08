from services.hospital_services import *


def hospital_menu():

    while True:

        print("\n====== HOSPITAL MANAGEMENT ======")
        print("1. Add Hospital")
        print("2. View Hospitals")
        print("3. Update Hospital")
        print("4. Delete Hospital")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            h_name = input("Enter Hospital Name: ")
            address = input("Enter Address: ")
            email = input("Enter Email: ")

            add_hospital(h_name, address, email)

        elif choice == "2":

            rows = view_hospital()

            print("\nHospital Records")

            for row in rows:

                print(f"""
                     Hospital ID : {row[0]}
                     Hospital Name : {row[1]}
                     Address : {row[2]}
                     Email : {row[3]}
                     ----------------------------
                     """)

        elif choice == "3":

            h_id = int(input("Enter Hospital ID: "))
            h_name = input("Enter New Hospital Name: ")
            address = input("Enter New Address: ")
            email = input("Enter New Email: ")

            update_hospital(h_id, h_name, address, email)

        elif choice == "4":

            h_id = int(input("Enter Hospital ID to Delete: "))

            delete_hospital(h_id)

        elif choice == "5":

            break

        else:

            print("Invalid Choice.")