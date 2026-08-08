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