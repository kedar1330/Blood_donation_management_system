from db import conn,cursor
from models.donor import *


def search_campaign():
    campaign_id=int(input("Enter campaign ID to search:"))
    
    query="select * from campaign where campaign_id=%s"
        
    cursor.execute(query,(campaign_id,))
    row=cursor.fetchone()

    if row:
        print("\n-------------campaign found---------------")
        print("campaign id :",row[0])
        print("campaign_name :",row[1])
        print("location :",row[2])
        print("date :",row[3])
        print("time : ",row[4])
    else:
        print("campaign not found" )

def  user_registration_campaigns():

    # Show Campaigns
    cursor.execute("SELECT campaign_id, campaign_name FROM campaign")
    rows = cursor.fetchall()

    print("\nAvailable Campaigns")
    for row in rows:
        print(row[0], "-", row[1])

    campaign_id = int(input("Enter Campaign ID: "))

    # Check Campaign ID
    cursor.execute("SELECT * FROM campaign WHERE campaign_id=%s", (campaign_id,))
    campaign = cursor.fetchone()

    if campaign is None:
        print("Invalid Campaign ID")
        return
    # donor details
    donor_name=input("enter donor name:")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    blood_group=input("enter your blood group :")
    phone=int(input("enter your phone number :")) 
    query="insert into user_campaign(donor_name,age,gender,blood_group,phone)values(%s,%s,%s,%s,%s,%s)"
    values=(donor_name,age,gender,blood_group,phone)
    cursor.execute(query,values)
    conn.commit()
    print("Successfully Registration complete!")

def login():
    email=input("enter your email :")
    password=input("enter your password :")
    query="select * from donor where email=%s and password=%s"
    cursor.execute(query,(email,password))
    result=cursor.fetchone()
    if result:
        print("login successfully!")
        return True
    else:
        print("invalid email and password!.please try again!")
        return False

def registration():    
    donor_name=input("enter donor name:")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    email=input("enter your email :")
    password=input("enter your password :")
    blood_group=input("enter your blood group :")
    phone=int(input("enter your phone number :"))
    donor_obj=donor(donor_name,age,gender,email,password,blood_group,phone)
    query="insert into donor(donor_name,age,gender,email,password,blood_group,phone)values(%s,%s,%s,%s,%s,%s,%s)"
    values=(donor_obj.donor_name,donor_obj.age,donor_obj.gender,donor_obj.email,donor_obj.password,donor_obj.blood_group,donor_obj.phone)
    cursor.execute(query,values)
    conn.commit()
    print("Successfully Registration complete!")





 