from services.donor_services import login, registration
from menus.donor_menu import donor_menu


def user_panel():
 
    while True:

        print("\n===== Blood Donation Management System =====")
        print("1. Donor")
        print("2. Recipient")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:

                while True:

                    print("\n====Donor Menu ====")
                    print("1. Registration")
                    print("2. Login")
                    print("3. Exit")

                    choice = int(input("Enter your choice: "))

                    match choice:

                        case 1:
                            registration()

                        case 2:
                            status = login()

                            if status:
                                donor_menu()

                        case 3:
                            break

                        case _:
                            print("Invalid choice")

            case 2:
                print("Recipient Panel")

            case 3:
                print("Thank You!")
                break

            case _:
                print("Invalid Choice! Please enter a number between 1 and 3.")