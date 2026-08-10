from services.h_hospital_services import *


def h_hospital_menu():

    print("\n========== HOSPITAL LOGIN ==========")

    h_id = int(input("Enter Hospital ID: "))
    email = input("Enter Hospital Email: ")

    hospital = hospital_login(h_id, email)

    if hospital:

        while True:

            print(f"\nWelcome {hospital.h_name}")

            print("\n========== HOSPITAL PANEL ==========")
            print("1. Emergency Blood Request")
            print("2. View Request Status")
            print("3. Logout")

            choice = input("Enter your choice: ")


            if choice == "1":

                blood_group = input("Enter Blood Group: ")
                units_required = int(input("Enter Required Units: "))
                request_date = input(
                    "Enter Required Date (DD-MM-YYYY): "
                )
                remarks = input("Enter Remarks: ")

                emergency_blood_request(
                    hospital.h_id,
                    blood_group,
                    units_required,
                    request_date,
                    remarks
                )

            elif choice == "2":

                view_status(hospital.h_id)


            elif choice == "3":

                print("Logging Out...")
                break

            else:

                print("Invalid Choice. Please try again.")

    else:

        print("\nInvalid Hospital ID or Email.")