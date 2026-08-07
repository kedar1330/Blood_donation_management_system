# Blood_donation_management_system
A Python &amp; MySQL based Blood Donation Management System with Admin, Hospital, and Donor panels featuring blood inventory management, emergency blood requests, donor management, campaign management, and email notifications.
### This is the entire actual project structure for reference
## 📂 Project Structure

```text
Blood_Donation_Management_System/
│
├── models/              # Contains all model classes
├── services/            # Business logic and database operations
├── menus/               # Menu-driven interface for Admin, Donor, and Hospital
│
├── admin.py             # Admin panel entry point
├── user.py              # Donor/User panel entry point
├── hospital.py          # Hospital panel entry point
├── db.py                # Database connection configuration
├── main.py              # Main application entry point
│
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignored files
└── Blood_Donation_DB.sql # MySQL database schema
```
## 🌳 System Hierarchy

```text
Blood Donation Management System
│
├── 👨‍💼 Admin Panel
│   │
│   ├── Blood Inventory Management
│   │   ├── Add Blood Inventory
│   │   ├── View Blood Inventory
│   │   ├── Update Blood Inventory
│   │   └── Delete Blood Inventory
│   │
│   ├── Blood Request Management
│   │   ├── View All Blood Requests
│   │   ├── Check Blood Inventory
│   │   ├── Approve Blood Request
│   │   ├── Update Request Status
│   │   └── Reject Blood Request
│   │
│   ├── Hospital Management
│   │   ├── Add Hospital
│   │   ├── View Hospitals
│   │   ├── Update Hospital
│   │   └── Delete Hospital
│   │
│   ├── Campaign Management
│   │   ├── Add Campaign
│   │   ├── View Campaigns
│   │   ├── Update Campaign
│   │   ├── Delete Campaign
│   │   └── View Registered Members
│   │
│   ├── Donor Management
│   │   ├── View Donors
│   │   ├── Search Donor by Blood Group
│   │   ├── Update Donor Details
│   │   └── Delete Donor Record
│   │
│   └── Exit
│
├── 🧑 User Panel
│   │
│   ├── 🩸 Donor
│   │   ├── Search Campaign
│   │   └── Register for Campaign
│   │
│   └── 🏥 Recipient
│       ├── Search Blood Group
│       ├── Pre-book Blood Units
│       ├── Payment
│       └── Bill Generation
│
└── 🏥 Hospital Panel
    │
    ├── Hospital Login
    ├── Emergency Blood Request
    └── Logout
```
## 🗄️ Database Tables

- blood_inventory
- request_management
- hospital_management
- donor
- campaign
- user_campaign
## 📦 Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Import the SQL database into MySQL.

4. Update database credentials in `db.py`.

5. Run the project

```bash
python main.py
```

---

## 📚 Concepts Used

- Object-Oriented Programming
- Modular Programming
- CRUD Operations
- SQL JOIN
- Foreign Keys
- MySQL Connectivity
- SMTP Email Notifications
- Menu Driven Programming

---
# All the best guys!

## 👨‍💻 Developed By

**Kedar V. Marathe(Linkcode Technologies)**
