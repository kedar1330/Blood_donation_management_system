from db import conn, cursor

# VIEW DONORS
def view_donor():

    query = "SELECT * FROM donor"

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nDonor ID\tName\tBlood Group\tGender\tAge\tPhone\tEmail")

    for r in rows:
        print(r[0], "\t\t", r[1], "\t", r[2], "\t\t", r[3], "\t", r[4], "\t", r[5], "\t", r[6])


# UPDATE DONOR
def update_donor():

    donor_id = int(input("Enter Donor ID to Update: "))

    donor_name = input("Enter New Name: ")
    blood_group = input("Enter New Blood Group: ")
    gender = input("Enter New Gender: ")
    age = int(input("Enter New Age: "))
    phone = input("Enter New Phone Number: ")
    email = input("Enter New Email: ")

    query = """
    UPDATE donor
    SET donor_name=%s,
        blood_group=%s,
        gender=%s,
        age=%s,
        phone=%s,
        email=%s
    WHERE donor_id=%s
    """

    values = (
        donor_name,
        blood_group,
        gender,
        age,
        phone,
        email,
        donor_id
    )

    cursor.execute(query, values)
    conn.commit()

    print("Donor Updated Successfully")


# DELETE DONOR
def delete_donor():

    donor_id = int(input("Enter Donor ID to Delete: "))

    query = "DELETE FROM donor WHERE donor_id=%s"

    cursor.execute(query, (donor_id,))
    conn.commit()

    print("Donor Deleted Successfully")


# SEARCH DONOR
def search_donor():

    donor_id = int(input("Enter Donor ID to Search: "))

    query = "SELECT * FROM donor WHERE donor_id=%s"

    cursor.execute(query, (donor_id,))
    row = cursor.fetchone()

    if row:
        print("\n========== Donor Details ==========")
        print("Donor ID     :", row[0])
        print("Name         :", row[1])
        print("Blood Group  :", row[2])
        print("Gender       :", row[3])
        print("Age          :", row[4])
        print("Phone        :", row[5])
        print("Email        :", row[6])
    else:
        print("Donor Not Found")