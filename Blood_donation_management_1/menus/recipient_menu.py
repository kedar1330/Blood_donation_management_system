from services.recipient_services import *
from services.payment_services import *
from services.report_services import *
from db import conn, cursor
from models.payment import Payment


def recipient_menu():

    while True:

        try:

            ch = int(input("""
========== Recipient ==========

1. Search Blood Group
2. Pre Book
3. Payment
4. Generate Bill
5. View Reports
6. Back

Enter Choice :
"""))

        except ValueError:

            print("\nPlease enter a valid number.")
            continue

        match ch:

            # ==========================================
            # SEARCH BLOOD GROUP
            # ==========================================

            case 1:

                search_blood_group()


            # ==========================================
            # PRE BOOK
            # ==========================================

            case 2:

                pre_book()


            # ==========================================
            # PAYMENT
            # ==========================================

            case 3:

                payment = make_payment()


            # ==========================================
            # GENERATE BILL
            # ==========================================

            case 4:

                try:

                    booking_id = int(
                        input("Enter Booking ID : ")
                    )

                except ValueError:

                    print("\nInvalid Booking ID!")
                    continue


                query = """
                SELECT
                    booking_id,
                    recipient_name,
                    amount,
                    payment_method,
                    payment_status
                FROM payment
                WHERE booking_id = %s
                """

                cursor.execute(
                    query,
                    (booking_id,)
                )

                row = cursor.fetchone()


                if row:

                    payment = Payment(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4]
                    )

                    generate_bill(payment)

                else:

                    print(
                        "\nPlease make payment first."
                    )


            # ==========================================
            # VIEW REPORTS
            # ==========================================

            case 5:

                view_reports()


            # ==========================================
            # BACK
            # ==========================================

            case 6:

                choice = input(
                    "\nAre you sure you want to go back? (yes/no): "
                ).lower().strip()

                if choice == "yes":

                    break

                elif choice == "no":

                    continue

                else:

                    print(
                        "Invalid input. "
                        "Please enter 'yes' or 'no'."
                    )


            # ==========================================
            # INVALID CHOICE
            # ==========================================

            case _:

                print("\nInvalid Choice!")