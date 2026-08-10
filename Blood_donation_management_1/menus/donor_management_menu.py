from services.donor_management_services import *


def donor_management_menu():

    while True:

        print("\n========== DONOR MANAGEMENT ==========")
        print("1. View All Donors")
        print("2. Search Donor By Blood Group")
        print("3. Update Donor Details")
        print("4. Delete Donor Record")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            donors = view_donors()

            if donors:

                print("\n========== DONOR LIST ==========\n")

                for donor in donors:
                    print(donor)
                    print("-" * 50)

            else:

                print("No Donor Records Found.")

        elif choice == "2":

            blood_group = input("Enter Blood Group: ")

            donors = search_donor(blood_group)

            if donors:

                print("\n========== SEARCH RESULT ==========\n")

                for donor in donors:
                    print(donor)
                    print("-" * 50)

            else:

                print("No Donors Found.")

        elif choice == "3":

            id = int(input("Enter Donor ID: "))
            donor_name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            gender = input("Enter New Gender: ")
            email = input("Enter New Email: ")
            blood_group = input("Enter New Blood Group: ")
            phone = input("Enter New Phone Number: ")

            update_donor_details(
                id,
                donor_name,
                age,
                gender,
                email,
                blood_group,
                phone
            )

        elif choice == "4":

            id = int(input("Enter Donor ID to Delete: "))

            delete_donor_record(id)

        elif choice == "5":

            print("Returning to Admin Panel...")
            break

        else:

            print("Invalid Choice.")