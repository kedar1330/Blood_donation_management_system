from db import conn, cursor
from models.pre_booking import PreBooking
from models.recipient import Recipient


# ==========================================================
# SEARCH BLOOD GROUP
# ==========================================================

def search_blood_group():

    blood_group = input("Enter Blood Group : ").upper().strip()

    valid_groups = [
        "A+", "A-", "B+", "B-",
        "AB+", "AB-", "O+", "O-"
    ]

    if blood_group not in valid_groups:
        print("\nInvalid Blood Group!")
        return

    recipient = Recipient(blood_group)

    check_availability(recipient)


def check_availability(recipient):

    query = """
    SELECT blood_group, units_available
    FROM blood_inventory
    WHERE blood_group = %s
    """

    cursor.execute(query, (recipient.blood_group,))

    data = cursor.fetchall()

    display_available(data)


def display_available(data):

    if not data:
        print("\nBlood Not Available")
        return

    print("\n===== Available Blood =====")

    for row in data:

        print("--------------------------------")
        print("Blood Group     :", row[0])
        print("Available Units :", row[1])


# ==========================================================
# PRE BOOKING
# ==========================================================

def pre_book():

    print("\n===== Pre Booking =====")

    # ------------------------------------------------------
    # Recipient Name
    # ------------------------------------------------------

    recipient_name = input("Enter Recipient Name : ").strip()

    if recipient_name == "":
        print("\nRecipient Name Cannot Be Empty!")
        return

    # ------------------------------------------------------
    # Phone
    # ------------------------------------------------------

    phone = input("Enter Phone Number : ").strip()

    if len(phone) != 10 or not phone.isdigit():
        print("\nInvalid Phone Number!")
        return

    # ------------------------------------------------------
    # Email
    # ------------------------------------------------------

    email = input("Enter Email : ").strip()

    if email == "":
        print("\nEmail Cannot Be Empty!")
        return

    if "@" not in email or "." not in email:
        print("\nInvalid Email Address!")
        return

    # ------------------------------------------------------
    # Address
    # ------------------------------------------------------

    address = input("Enter Address : ").strip()

    if address == "":
        print("\nAddress Cannot Be Empty!")
        return

    # ------------------------------------------------------
    # Blood Group
    # ------------------------------------------------------

    blood_group = input("Enter Blood Group : ").upper().strip()

    valid_groups = [
        "A+", "A-", "B+", "B-",
        "AB+", "AB-", "O+", "O-"
    ]

    if blood_group not in valid_groups:
        print("\nInvalid Blood Group!")
        return

    # ------------------------------------------------------
    # Quantity
    # ------------------------------------------------------

    try:
        quantity = int(input("Enter Quantity : "))

    except ValueError:
        print("\nQuantity Must Be a Number!")
        return

    if quantity <= 0:
        print("\nQuantity Must Be Greater Than 0!")
        return

    # ======================================================
    # CHECK BLOOD INVENTORY
    # ======================================================

    query = """
    SELECT units_available
    FROM blood_inventory
    WHERE blood_group = %s
    """

    cursor.execute(query, (blood_group,))

    data = cursor.fetchone()

    if data is None:
        print("\nBlood Group Not Available!")
        return

    available_quantity = data[0]

    if available_quantity == 0:

        print(f"\n{blood_group} blood is Out of Stock.")
        print("Pre Booking Failed!")

        return

    # ------------------------------------------------------
    # Quantity validation
    # ------------------------------------------------------

    if quantity > available_quantity:

        print(
            f"\nOnly {available_quantity} unit(s) "
            f"of {blood_group} blood is available."
        )

        return

    # ======================================================
    # HOSPITAL
    # ======================================================

    hospital_name = "Blood Bank"

    # ======================================================
    # CREATE BOOKING OBJECT
    # ======================================================

    booking = PreBooking(
        recipient_name,
        phone,
        blood_group,
        quantity,
        hospital_name
    )

    # ======================================================
    # INSERT PRE BOOKING
    # ======================================================

    insert_query = """
    INSERT INTO pre_booking
    (
        recipient_name,
        phone,
        email,
        address,
        blood_group,
        quantity,
        hospital_name,
        booking_date,
        status
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        CURDATE(),
        'Pending'
    )
    """

    values = (
        booking.recipient_name,
        booking.phone,
        email,
        address,
        booking.blood_group,
        booking.quantity,
        booking.hospital_name
    )

    try:

        cursor.execute(insert_query, values)

        booking_id = cursor.lastrowid

        conn.commit()

    except Exception as e:

        conn.rollback()

        print("\nPre Booking Failed!")
        print("Error:", e)

        return

    # ======================================================
    # SUCCESS MESSAGE
    # ======================================================

    print("\n===== Pre Booking Successful =====")

    print("Booking ID     :", booking_id)
    print("Recipient Name :", booking.recipient_name)
    print("Phone          :", booking.phone)
    print("Email          :", email)
    print("Address        :", address)
    print("Blood Group    :", booking.blood_group)
    print("Booked Units   :", booking.quantity)
    print("Blood Bank     :", booking.hospital_name)

    print("\nStatus         : Pending")

    print(
        "\nPlease complete payment to confirm your booking."
    )