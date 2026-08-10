from db import conn, cursor
from models.donor import donor


# ==========================================================
# SEARCH CAMPAIGN
# ==========================================================

def search_campaign():

    campaign_id = int(input("Enter campaign ID to search: "))

    query = """
    SELECT *
    FROM campaign
    WHERE campaign_id = %s
    """

    cursor.execute(query, (campaign_id,))
    row = cursor.fetchone()

    if row:
        print("\n------------- Campaign Found -------------")
        print("Campaign ID   :", row[0])
        print("Campaign Name :", row[1])
        print("Location      :", row[2])
        print("Date          :", row[3])
        print("Time          :", row[4])

    else:
        print("Campaign not found.")


# ==========================================================
# USER REGISTRATION FOR CAMPAIGN
# ==========================================================

def user_registration_campaigns():

    # ------------------------------------------------------
    # Show Available Campaigns
    # ------------------------------------------------------

    cursor.execute("""
        SELECT campaign_id, campaign_name
        FROM campaign
    """)

    rows = cursor.fetchall()

    if not rows:
        print("\nNo campaigns available.")
        return

    print("\n========== AVAILABLE CAMPAIGNS ==========")

    for row in rows:
        print(row[0], "-", row[1])

    # ------------------------------------------------------
    # Select Campaign
    # ------------------------------------------------------

    campaign_id = int(input("\nEnter Campaign ID: "))

    # ------------------------------------------------------
    # Check Campaign ID
    # ------------------------------------------------------

    cursor.execute(
        "SELECT * FROM campaign WHERE campaign_id = %s",
        (campaign_id,)
    )

    campaign = cursor.fetchone()

    if campaign is None:
        print("Invalid Campaign ID.")
        return

    # ------------------------------------------------------
    # Take Donor Details
    # ------------------------------------------------------

    donor_name = input("Enter donor name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    blood_group = input("Enter your blood group: ")
    phone = input("Enter your phone number: ")

    # ------------------------------------------------------
    # Insert Registration
    # ------------------------------------------------------

    query = """
    INSERT INTO user_campaign
    (
        campaign_id,
        donor_name,
        age,
        gender,
        blood_group,
        phone
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        campaign_id,
        donor_name,
        age,
        gender,
        blood_group,
        phone
    )

    cursor.execute(query, values)
    conn.commit()

    print("\nSuccessfully registered for the campaign!")


# ==========================================================
# DONOR LOGIN
# ==========================================================

def login():

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    query = """
    SELECT *
    FROM donor
    WHERE email = %s
    AND password = %s
    """

    cursor.execute(query, (email, password))

    result = cursor.fetchone()

    if result:

        print("\nLogin successful!")

        return True

    else:

        print("\nInvalid email or password. Please try again.")

        return False


# ==========================================================
# DONOR REGISTRATION
# ==========================================================

def registration():

    donor_name = input("Enter donor name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    blood_group = input("Enter your blood group: ")
    phone = input("Enter your phone number: ")

    # ------------------------------------------------------
    # Create Donor Object
    # ------------------------------------------------------

    donor_obj = donor(
        donor_name,
        age,
        gender,
        email,
        password,
        blood_group,
        phone
    )

    # ------------------------------------------------------
    # Insert Donor
    # ------------------------------------------------------

    query = """
    INSERT INTO donor
    (
        donor_name,
        age,
        gender,
        email,
        password,
        blood_group,
        phone
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        donor_obj.donor_name,
        donor_obj.age,
        donor_obj.gender,
        donor_obj.email,
        donor_obj.password,
        donor_obj.blood_group,
        donor_obj.phone
    )

    cursor.execute(query, values)

    conn.commit()

    print("\nSuccessfully registered as a donor!")