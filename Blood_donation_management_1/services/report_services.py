from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

from db import conn, cursor


# ==========================================================
# GENERATE BILL
# ==========================================================

def generate_bill(payment):

    if not os.path.exists("bills"):
        os.makedirs("bills")

    # ======================================================
    # GET BOOKING DETAILS
    # ======================================================

    query = """
    SELECT
        blood_group,
        hospital_name,
        quantity,
        email,
        address
    FROM pre_booking
    WHERE booking_id = %s
    """

    cursor.execute(query, (payment.booking_id,))

    booking = cursor.fetchone()

    if booking:

        blood_group = booking[0]
        hospital_name = booking[1]
        quantity = booking[2]
        email = booking[3]
        address = booking[4]

    else:

        blood_group = "N/A"
        hospital_name = "N/A"
        quantity = "N/A"
        email = "N/A"
        address = "N/A"

    # ======================================================
    # PDF BILL
    # ======================================================

    pdf_bill_name = f"bills/Bill_{payment.booking_id}.pdf"

    pdf = canvas.Canvas(
        pdf_bill_name,
        pagesize=letter
    )

    # ======================================================
    # TITLE
    # ======================================================

    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawCentredString(
        300,
        750,
        "BLOOD DONATION SYSTEM"
    )

    pdf.setFont("Helvetica-Bold", 14)

    pdf.drawCentredString(
        300,
        720,
        "PAYMENT RECEIPT"
    )

    pdf.line(50, 700, 550, 700)

    # ======================================================
    # BILL INFORMATION
    # ======================================================

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        70,
        670,
        "Bill Information"
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        90,
        645,
        f"Bill ID        : {payment.booking_id}"
    )

    pdf.drawString(
        90,
        620,
        f"Date           : {datetime.now().strftime('%d-%m-%Y')}"
    )

    pdf.drawString(
        90,
        595,
        f"Time           : {datetime.now().strftime('%H:%M:%S')}"
    )

    # ======================================================
    # RECIPIENT DETAILS
    # ======================================================

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        70,
        550,
        "Recipient Details"
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        90,
        520,
        f"Name           : {payment.recipient_name}"
    )

    pdf.drawString(
        90,
        495,
        f"Email          : {email}"
    )

    pdf.drawString(
        90,
        470,
        f"Address        : {address}"
    )

    pdf.drawString(
        90,
        445,
        f"Blood Group    : {blood_group}"
    )

    pdf.drawString(
        90,
        420,
        f"Hospital       : {hospital_name}"
    )

    pdf.drawString(
        90,
        395,
        f"Quantity       : {quantity} Units"
    )

    # ======================================================
    # PAYMENT DETAILS
    # ======================================================

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        70,
        350,
        "Payment Details"
    )

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        90,
        325,
        f"Amount         : Rs.{payment.amount}"
    )

    pdf.drawString(
        90,
        300,
        f"Method         : {payment.payment_method}"
    )

    pdf.drawString(
        90,
        275,
        f"Status         : {payment.payment_status}"
    )

    # ======================================================
    # TOTAL BOX
    # ======================================================

    pdf.rect(
        70,
        205,
        450,
        45
    )

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        120,
        223,
        f"TOTAL PAID : Rs.{payment.amount}"
    )

    # ======================================================
    # FOOTER
    # ======================================================

    pdf.setFont(
        "Helvetica-Oblique",
        12
    )

    pdf.drawCentredString(
        300,
        155,
        "Thank You For Supporting Blood Donation"
    )

    pdf.drawCentredString(
        300,
        130,
        "Save Life - Donate Blood"
    )

    pdf.save()

    # ======================================================
    # TXT BILL
    # ======================================================

    txt_bill_name = f"bills/Bill_{payment.booking_id}.txt"

    with open(txt_bill_name, "w") as file:

        file.write(
            "========== BLOOD DONATION SYSTEM ==========\n"
        )

        file.write(
            "========== PAYMENT RECEIPT ==========\n\n"
        )

        file.write("Bill Information\n")
        file.write("-------------------------\n")

        file.write(
            f"Bill ID : {payment.booking_id}\n"
        )

        file.write(
            f"Date    : {datetime.now().strftime('%d-%m-%Y')}\n"
        )

        file.write(
            f"Time    : {datetime.now().strftime('%H:%M:%S')}\n\n"
        )

        file.write("Recipient Details\n")
        file.write("-------------------------\n")

        file.write(
            f"Name        : {payment.recipient_name}\n"
        )

        file.write(
            f"Email       : {email}\n"
        )

        file.write(
            f"Address     : {address}\n"
        )

        file.write(
            f"Blood Group : {blood_group}\n"
        )

        file.write(
            f"Hospital    : {hospital_name}\n"
        )

        file.write(
            f"Quantity    : {quantity} Units\n\n"
        )

        file.write("Payment Details\n")
        file.write("-------------------------\n")

        file.write(
            f"Amount : Rs.{payment.amount}\n"
        )

        file.write(
            f"Method : {payment.payment_method}\n"
        )

        file.write(
            f"Status : {payment.payment_status}\n\n"
        )

        file.write(
            f"TOTAL PAID : Rs.{payment.amount}\n\n"
        )

        file.write(
            "Thank You For Supporting Blood Donation\n"
        )

        file.write(
            "Save Life - Donate Blood\n"
        )

    print("\nBill Generated Successfully!")

    return pdf_bill_name


# ==========================================================
# VIEW REPORTS
# ==========================================================

def view_reports():

    print("\n========== PAYMENT REPORTS ==========")

    query = """
    SELECT
        p.payment_id,
        p.booking_id,
        p.recipient_name,
        pb.blood_group,
        pb.hospital_name,
        pb.quantity,
        p.amount,
        p.payment_method,
        p.payment_status,
        p.payment_date
    FROM payment p
    LEFT JOIN pre_booking pb
        ON p.booking_id = pb.booking_id
    """

    cursor.execute(query)

    data = cursor.fetchall()

    if not data:

        print("No Reports Found!")

        return

    for row in data:

        print("\n----------------------------")

        print("Payment ID :", row[0])
        print("Booking ID :", row[1])
        print("Recipient  :", row[2])
        print("Blood Group:", row[3] if row[3] else "N/A")
        print("Hospital   :", row[4] if row[4] else "N/A")
        print("Quantity   :", row[5] if row[5] else "N/A")
        print("Amount     : Rs.", row[6])
        print("Method     :", row[7])
        print("Status     :", row[8])
        print("Date       :", row[9])

    # ======================================================
    # PAYMENT SUMMARY
    # ======================================================

    summary_query = """
    SELECT
        COUNT(*),
        COALESCE(SUM(amount), 0),
        SUM(
            CASE
                WHEN payment_status = 'Paid'
                THEN 1
                ELSE 0
            END
        )
    FROM payment
    """

    cursor.execute(summary_query)

    summary = cursor.fetchone()

    total_payments = summary[0]
    total_amount = summary[1]
    paid_payments = summary[2]

    print("\n================================")
    print("       PAYMENT SUMMARY")
    print("================================")

    print("Total Payments :", total_payments)
    print("Total Amount   : Rs.", total_amount)
    print("Paid Payments  :", paid_payments)

    print("================================")