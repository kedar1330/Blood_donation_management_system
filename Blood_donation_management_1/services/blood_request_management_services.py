from db import conn, cursor
from models.blood_request_management import BloodRequestManagement

import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



load_dotenv()
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

    # ==========================================
    # Get request details
    # ==========================================

    query = """
    SELECT blood_group, units_required
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

    # ==========================================
    # Check Blood Inventory
    # ==========================================

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

    # ==========================================
    # Check sufficient blood
    # ==========================================

    if units_available < units_required:
        print("Insufficient Blood Units.")
        return

    # ==========================================
    # Reduce Blood Inventory
    # ==========================================

    query = """
    UPDATE blood_inventory
    SET units_available = units_available - %s
    WHERE blood_group=%s
    """

    cursor.execute(query, (units_required, blood_group))

    # ==========================================
    # Update Request Status
    # ==========================================

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

def update_request_status(req_id, status, admin_response):

    query = """
    UPDATE request_management
    SET R_status=%s,
        remarks=%s
    WHERE req_id=%s
    """

    cursor.execute(
        query,
        (status, admin_response, req_id)
    )

    conn.commit()

    print("Request Status and Admin Response Updated Successfully.")


# ==========================================
# Reject Blood Request
# ==========================================

def reject_request(req_id):

    # Get request and hospital details
    query = """
    SELECT
        r.blood_group,
        r.units_required,
        r.request_date,
        h.H_name
    FROM request_management r
    INNER JOIN hospital_management h
    ON r.Hospital_id = h.H_id
    WHERE r.req_id=%s
    """

    cursor.execute(query, (req_id,))

    request = cursor.fetchone()

    if request is None:
        print("Request ID not found.")
        return

    blood_group = request[0]
    units_required = request[1]
    request_date = request[2]
    hospital_name = request[3]

    # Reject the request
    query = """
    UPDATE request_management
    SET R_status='Rejected'
    WHERE req_id=%s
    """

    cursor.execute(query, (req_id,))

    conn.commit()

    print("Blood Request Rejected Successfully.")

    # ==========================================
    # Find donors with required blood group
    # ==========================================

    query = """
    SELECT donor_name, email
    FROM donor
    WHERE blood_group=%s
    """

    cursor.execute(query, (blood_group,))

    donors = cursor.fetchall()

    if not donors:
        print("No donors found with this blood group.")
        return

    # ==========================================
    # Get Email Credentials
    # ==========================================

    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("Email credentials are not configured.")
        return

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, sender_password)

        # ==========================================
        # Send Email to Matching Donors
        # ==========================================

        for donor in donors:

            donor_name = donor[0]
            donor_email = donor[1]

            subject = "Emergency Blood Requirement"

            body = f"""
                   Dear {donor_name},
                   
                   An emergency blood requirement has been reported.
                   
                   Hospital: {hospital_name}
                   Required Blood Group: {blood_group}
                   Units Required: {units_required}
                   Required Date: {request_date}
                   
                   If you are eligible and available to donate blood,
                   please contact the hospital or blood donation center
                   as soon as possible.
                   
                   Your contribution can help save a life.
                   
                   Thank you,
                   Blood Donation Management System
                   """

            message = MIMEMultipart()

            message["From"] = sender_email
            message["To"] = donor_email
            message["Subject"] = subject

            message.attach(
                MIMEText(body, "plain")
            )

            server.sendmail(
                sender_email,
                donor_email,
                message.as_string()
            )

            print(f"Email sent to {donor_email}")

        server.quit()

        print("Emergency blood request emails sent successfully.")

    except Exception as e:

        print("Error while sending emails:", e)