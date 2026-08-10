from services.donor_services import login, registration
from menus.donor_menu import donor_menu
from menus.recipient_menu import recipient_menu


def user_panel():

    while True:

        print("\n===== Blood Donation Management System =====")
        print("1. Donor")
        print("2. Recipient")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:

            # ==========================================
            # DONOR
            # ==========================================

            case 1:

                while True:

                    print("\n==== Donor Menu ====")
                    print("1. Registration")
                    print("2. Login")
                    print("3. Back")

                    try:
                        choice = int(
                            input("Enter your choice: ")
                        )

                    except ValueError:
                        print("Please enter a valid number.")
                        continue

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
                            print("Invalid choice.")


            # ==========================================
            # RECIPIENT
            # ==========================================

            case 2:

                recipient_menu()


            # ==========================================
            # EXIT USER PANEL
            # ==========================================

            case 3:

                print("\nThank You!")
                break


            # ==========================================
            # INVALID CHOICE
            # ==========================================

            case _:

                print(
                    "Invalid Choice! "
                    "Please enter a number between 1 and 3."
                )