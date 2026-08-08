from db import conn, cursor
from models.blood_request_management import BloodRequestManagement


# ==========================
# View All Blood Requests
# ==========================

def view_all_requests():

    query = """
    SELECT
        r.req_id,
        h.H_name,
        r.blood_group,
        r.units_required,
        r.request_date,
        r.R_status,
        r.remarks
    FROM request_management r
    INNER JOIN hospital_management h
    ON r.Hospital_id = h.H_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    request_list = []

    for row in rows:

        request = BloodRequestManagement(
            row[0],   # Request ID
            row[1],   # Hospital Name
            row[2],   # Blood Group
            row[3],   # Units Required
            row[4],   # Request Date
            row[5],   # Status
            row[6]    # Remarks
        )

        request_list.append(request)

    return request_list


# ==========================
# Check Blood Inventory
# ==========================

def check_blood_inventory():

    query = "SELECT * FROM blood_inventory"

    cursor.execute(query)

    rows = cursor.fetchall()

    return rows


# ==========================
# Approve Blood Request
# ==========================

def approve_request(req_id):

    # Get request details

    query = """
    SELECT blood_group,
           units_required
    FROM request_management
    WHERE req_id=%s
    """

    cursor.execute(query, (req_id,))

    request = cursor.fetchone()

    if request is None:
        print("Request ID not found.")
        return

    blood_group = request[0]
    units_required = request[1]

    # Check Inventory

    query = """
    SELECT units_available
    FROM blood_inventory
    WHERE blood_group=%s
    """

    cursor.execute(query, (blood_group,))

    inventory = cursor.fetchone()

    if inventory is None:

        print("Blood Group not available in inventory.")
        return

    units_available = inventory[0]

    if units_available < units_required:

        print("Insufficient Blood Units.")
        return

    # Reduce Inventory

    query = """
    UPDATE blood_inventory
    SET units_available = units_available-%s
    WHERE blood_group=%s
    """

    cursor.execute(query, (units_required, blood_group))

    # Update Request Status

    query = """
    UPDATE request_management
    SET R_status='Approved'
    WHERE req_id=%s
    """

    cursor.execute(query, (req_id,))

    conn.commit()

    print("Blood Request Approved Successfully.")


# ==========================
# Update Request Status
# ==========================

def update_request_status(req_id, status):

    query = """
    UPDATE request_management
    SET R_status=%s
    WHERE req_id=%s
    """

    cursor.execute(query, (status, req_id))

    conn.commit()

    print("Request Status Updated Successfully.")


# ==========================
# Reject Blood Request
# ==========================

def reject_request(req_id):

    query = """
    UPDATE request_management
    SET R_status='Rejected'
    WHERE req_id=%s
    """

    cursor.execute(query, (req_id,))

    conn.commit()

    print("Blood Request Rejected Successfully.")

    # SMTP functionality will be added later.