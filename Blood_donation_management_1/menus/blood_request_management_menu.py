from services.blood_request_management_services import *


def blood_request_management_menu():

    while True:

        print("\n========== BLOOD REQUEST MANAGEMENT ==========")
        print("1. View All Blood Requests")
        print("2. Check Blood Inventory")
        print("3. Approve Blood Request")
        print("4. Update Request Status")
        print("5. Reject Blood Request")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            request_list = view_all_requests()

            if request_list:

                print("\n========== ALL BLOOD REQUESTS ==========\n")

                for request in request_list:
                    print(request)
                    print("-" * 50)

            else:

                print("No Blood Requests Found.")

        elif choice == "2":

            inventory = check_blood_inventory()

            if inventory:

                print("\n========== BLOOD INVENTORY ==========\n")

                print("ID\tBlood Group\tUnits Available")

                for row in inventory:
                    print(f"{row[0]}\t{row[1]}\t\t{row[2]}")

            else:

                print("Blood Inventory is Empty.")

        elif choice == "3":

            req_id = int(input("Enter Request ID to Approve: "))

            approve_request(req_id)

        elif choice == "4":

            req_id = int(input("Enter Request ID: "))
            status = input("Enter New Status (Pending/Approved/Rejected): ")

            update_request_status(req_id, status)

        elif choice == "5":

            req_id = int(input("Enter Request ID to Reject: "))

            reject_request(req_id)

        elif choice == "6":

            print("Returning to Admin Panel...")
            break

        else:

            print("Invalid Choice. Please Try Again.")