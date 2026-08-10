from db import conn, cursor
from models.h_hospital import H_Hospital


def hospital_login(h_id, email):

    query = """
    SELECT H_id, H_name, email
    FROM hospital_management
    WHERE H_id=%s AND email=%s
    """

    cursor.execute(query, (h_id, email))

    row = cursor.fetchone()

    if row:
        return H_Hospital(row[0], row[1], row[2])

    return None


def emergency_blood_request(hospital_id,
                            blood_group,
                            units_required,
                            request_date,
                            remarks):

    query = """
    INSERT INTO request_management
    (Hospital_id,
     blood_group,
     units_required,
     request_date,
     R_status,
     remarks)

    VALUES(%s,%s,%s,%s,%s,%s)
    """

    values = (
        hospital_id,
        blood_group,
        units_required,
        request_date,
        "Pending",
        remarks
    )

    cursor.execute(query, values)

    conn.commit()

    print("\nEmergency Blood Request Submitted Successfully.")

def view_status(hospital_id):

    query = """
    SELECT
        req_id,
        blood_group,
        units_required,
        request_date,
        R_status,
        remarks,
        admin_response
    FROM request_management
    WHERE Hospital_id=%s
    ORDER BY request_date DESC
    """

    cursor.execute(query, (hospital_id,))

    rows = cursor.fetchall()

    if not rows:
        print("\nNo blood requests found.")
        return

    print("\n========== MY BLOOD REQUESTS ==========")

    for row in rows:

        print("\nRequest ID      :", row[0])
        print("Blood Group     :", row[1])
        print("Units Required  :", row[2])
        print("Request Date    :", row[3])
        print("Status          :", row[4])
        print("Your Remarks    :", row[5])
        print("Admin Response  :", row[6])

        print("----------------------------------------")