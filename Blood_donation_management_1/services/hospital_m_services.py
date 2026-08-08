from db import conn, cursor
from models.hospital_m import Hospital


# ADD HOSPITAL
def add_hospital():
    hospital_name = input("Enter Hospital Name: ")
    address = input("Enter Address: ")
    email = input("Enter Email: ")

    h = Hospital(hospital_name, address, email)

    query = """
    INSERT INTO hospital(hospital_name,address,email)
    VALUES(%s,%s,%s)
    """

    values = (h.hospital_name, h.address, h.email)

    cursor.execute(query, values)
    conn.commit()

    print("Hospital Added Successfully")


# VIEW HOSPITAL
def view_hospital():

    query = "SELECT * FROM hospital"

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nHospital ID\tHospital Name\tAddress\t\tEmail")

    for r in rows:
        print(r[0], "\t\t", r[1], "\t", r[2], "\t", r[3])


# UPDATE HOSPITAL
def update_hospital():

    hospital_id = int(input("Enter Hospital ID to Update: "))
    hospital_name = input("Enter New Hospital Name: ")
    address = input("Enter New Address: ")
    email = input("Enter New Email: ")

    query = """
    UPDATE hospital
    SET hospital_name=%s,
        address=%s,
        email=%s
    WHERE hospital_id=%s
    """

    values = (hospital_name, address, email, hospital_id)

    cursor.execute(query, values)
    conn.commit()

    print("Hospital Updated Successfully")


# DELETE HOSPITAL
def delete_hospital():

    hospital_id = int(input("Enter Hospital ID to Delete: "))

    query = "DELETE FROM hospital WHERE hospital_id=%s"

    cursor.execute(query, (hospital_id,))
    conn.commit()

    print("Hospital Deleted Successfully")


# SEARCH HOSPITAL
def search_hospital():

    hospital_id = int(input("Enter Hospital ID to Search: "))

    query = "SELECT * FROM hospital WHERE hospital_id=%s"

    cursor.execute(query, (hospital_id,))
    row = cursor.fetchone()

    if row:
        print("\nHospital Found\n")
        print("Hospital ID   :", row[0])
        print("Hospital Name :", row[1])
        print("Address       :", row[2])
        print("Email         :", row[3])
    else:
        print("Hospital Not Found")