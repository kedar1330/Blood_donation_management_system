from db import conn, cursor
from models.payment import Payment


def make_payment():

    print("\n========== Payment ==========")

    # ======================================================
    # BOOKING ID
    # ======================================================

    try:
        booking_id = int(input("Enter Booking ID : "))

    except ValueError:
        print("\nInvalid Booking ID!")
        return

    # ======================================================
    # CHECK BOOKING
    # ======================================================

    query = """
    SELECT
        booking_id,
        recipient_name,
        blood_group,
        quantity,
        status
    FROM pre_booking
    WHERE booking_id = %s
    """

    cursor.execute(query, (booking_id,))

    booking = cursor.fetchone()

    if booking is None:

        print("\nInvalid Booking ID!")
        print("Please Complete Pre Booking First.")

        return

    # ======================================================
    # CHECK BOOKING STATUS
    # ======================================================

    if booking[4] != "Pending":

        print("\nThis booking is already processed.")
        return

    recipient_name = booking[1]
    blood_group = booking[2]
    quantity = booking[3]

    # ======================================================
    # CHECK ALREADY PAID
    # ======================================================

    query = """
    SELECT payment_id
    FROM payment
    WHERE booking_id = %s
    """

    cursor.execute(query, (booking_id,))

    paid = cursor.fetchone()

    if paid:

        print("\nPayment Already Completed!")

        return

    # ======================================================
    # RECIPIENT NAME
    # ======================================================

    entered_name = input(
        "Enter Recipient Name : "
    ).strip()

    if entered_name == "":

        print("\nRecipient Name Cannot Be Empty!")

        return

    if entered_name.lower() != recipient_name.lower():

        print(
            "\nRecipient Name Does Not Match Booking!"
        )

        print("Payment Cancelled.")

        return

    # ======================================================
    # CHECK INVENTORY AGAIN
    # ======================================================

    query = """
    SELECT units_available
    FROM blood_inventory
    WHERE blood_group = %s
    """

    cursor.execute(
        query,
        (blood_group,)
    )

    inventory = cursor.fetchone()

    if inventory is None:

        print("\nBlood Group is no longer available.")

        return

    available_units = inventory[0]

    if available_units < quantity:

        print(
            f"\nOnly {available_units} unit(s) "
            f"of {blood_group} blood are currently available."
        )

        print(
            "Payment cannot be completed."
        )

        return

    # ======================================================
    # AMOUNT
    # ======================================================

    try:

        amount = float(
            input("Enter Amount : ")
        )

    except ValueError:

        print("\nInvalid Amount!")

        return

    if amount <= 0:

        print("\nAmount Must Be Greater Than 0!")

        return

    # ======================================================
    # PAYMENT METHOD
    # ======================================================

    print("\nPayment Methods")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    try:

        choice = int(
            input("Select Payment Method : ")
        )

    except ValueError:

        print("\nInvalid Payment Method!")

        return

    if choice == 1:

        payment_method = "UPI"

    elif choice == 2:

        payment_method = "Card"

    elif choice == 3:

        payment_method = "Cash"

    else:

        print("\nInvalid Payment Method!")

        return

    # ======================================================
    # CREATE PAYMENT OBJECT
    # ======================================================

    payment = Payment(
        booking_id,
        entered_name,
        amount,
        payment_method,
        "Paid"
    )

    try:

        # ==================================================
        # INSERT PAYMENT
        # ==================================================

        payment_query = """
        INSERT INTO payment
        (
            booking_id,
            recipient_name,
            amount,
            payment_method,
            payment_status,
            payment_date
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            CURDATE()
        )
        """

        payment_values = (
            payment.booking_id,
            payment.recipient_name,
            payment.amount,
            payment.payment_method,
            payment.payment_status
        )

        cursor.execute(
            payment_query,
            payment_values
        )

        # ==================================================
        # DEDUCT BLOOD UNITS
        # ==================================================

        inventory_query = """
        UPDATE blood_inventory
        SET units_available = units_available - %s
        WHERE blood_group = %s
        AND units_available >= %s
        """

        cursor.execute(
            inventory_query,
            (
                quantity,
                blood_group,
                quantity
            )
        )

        if cursor.rowcount == 0:

            conn.rollback()

            print(
                "\nBlood inventory changed."
            )

            print(
                "Payment could not be completed."
            )

            return

        # ==================================================
        # UPDATE BOOKING STATUS
        # ==================================================

        booking_query = """
        UPDATE pre_booking
        SET status = 'Confirmed'
        WHERE booking_id = %s
        """

        cursor.execute(
            booking_query,
            (booking_id,)
        )

        # ==================================================
        # COMMIT EVERYTHING
        # ==================================================

        conn.commit()

    except Exception as e:

        conn.rollback()

        print("\nPayment Failed!")
        print("Error:", e)

        return

    # ======================================================
    # SUCCESS
    # ======================================================

    print("\n===== Payment Successful =====")

    print("Booking ID      :", payment.booking_id)
    print("Recipient Name  :", payment.recipient_name)
    print("Blood Group     :", blood_group)
    print("Units Booked    :", quantity)
    print("Amount          :", payment.amount)
    print("Payment Method  :", payment.payment_method)
    print("Payment Status  :", payment.payment_status)
    print("Booking Status  : Confirmed")

    return payment