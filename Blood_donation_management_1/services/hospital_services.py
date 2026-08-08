from models.hospital import Hospital
from db import conn, cursor


def add_hospital(h_name, address, email):

    hospital = Hospital(h_name, address, email)

    query = """
    INSERT INTO hospital_management(H_name,address,email)
    VALUES(%s,%s,%s)
    """

    cursor.execute(query, (hospital.h_name,
                           hospital.address,
                           hospital.email))

    conn.commit()

    print("Hospital Added Successfully.")


def view_hospital():

    query = "SELECT * FROM hospital_management"

    cursor.execute(query)

    return cursor.fetchall()


def update_hospital(h_id, h_name, address, email):

    query = """
    UPDATE hospital_management
    SET H_name=%s,
        address=%s,
        email=%s
    WHERE H_id=%s
    """

    cursor.execute(query, (h_name, address, email, h_id))

    conn.commit()

    print("Hospital Updated Successfully.")


def delete_hospital(h_id):

    query = "DELETE FROM hospital_management WHERE H_id=%s"

    cursor.execute(query, (h_id,))

    conn.commit()

    print("Hospital Deleted Successfully.")