from db import conn, cursor
from models.donor_management import *

def view_donors():

    query = "SELECT * FROM donor"

    cursor.execute(query)

    rows = cursor.fetchall()

    donor_list = []

    for row in rows:

        donor = DonorManagement(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[6],
            row[7]
        )

        donor_list.append(donor)

    return donor_list


def search_donor(blood_group):

    query = """
    SELECT *
    FROM donor
    WHERE blood_group=%s
    """

    cursor.execute(query, (blood_group,))

    rows = cursor.fetchall()

    donor_list = []

    for row in rows:

        donor = DonorManagement(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[6],
            row[7]
        )

        donor_list.append(donor)

    return donor_list

def update_donor_details(id,
                         donor_name,
                         age,
                         gender,
                         email,
                         blood_group,
                         phone):

    query = """
    UPDATE donor
    SET donor_name=%s,
        age=%s,
        gender=%s,
        email=%s,
        blood_group=%s,
        phone=%s
    WHERE id=%s
    """

    values = (
        donor_name,
        age,
        gender,
        email,
        blood_group,
        phone,
        id
    )

    cursor.execute(query, values)

    conn.commit()

    print("Donor Details Updated Successfully.")

def delete_donor_record(id):

    query = """
    DELETE FROM donor
    WHERE id=%s
    """

    cursor.execute(query, (id,))

    conn.commit()

    print("Donor Record Deleted Successfully.")