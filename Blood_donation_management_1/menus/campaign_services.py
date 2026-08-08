from db import conn,cursor
from models.campaign_m import Campaign

#ADD CAMPAIGN
def add_campaign():
    campaign_name=input("Enter name of campaign:")
    location=input("Enter location:")
    date=input("Enter Date(DD-MM-YYY):")
    time=input("Enter time(HH:MM):")
    
    c=Campaign(campaign_name,location,date,time)
    
    query="""
    insert into campaign(campaign_name,location,date,time)
    values(%s,%s,%s,%s)"""
    
    values=(c.campaign_name,c.location,c.date,c.time)
    
    cursor.execute(query,values)
    conn.commit()
    print("Campaign added successfully")
    
#VIEW CAMPAIGN
def view_campaign():
    query="select * from campaign"
    
    cursor.execute(query)
    rows=cursor.fetchall()
    
    print(" \nCampaign ID\tCampaign Name\tLocation\tDate\tTime")
    
    for r in rows:
        print(r[0], "\t\t", r[1], "\t", r[2], "\t", r[3], "\t", r[4])
        
#UPDATE CAMPAIGN
def update_campaign():
    campaign_id=int(input("Enter campaign ID to update:"))
    campaign_name=input("Enter new campaign name:")
    location=input("Enter new location:")
    date=input("Enter new date(DD-MM-YYYY):")
    time=input("Enter new time(HH:MM):")
    
    query="""
    update campaign
    set campaign_name=%s,location=%s,date=%s,time=%s
    where campaign_id=%s
    """
    values=(campaign_name,location,date,time,campaign_id)
    
    cursor.execute(query,values)
    conn.commit()
    print("Campaign updated successfully")
    
#DELETE CAMPAIGN
def delete_campaign():
    campaign_id=int(input("Enter campaign ID to delete:"))
    
    query="delete from campaign where campaign_id=%s"
    
    cursor.execute(query,(campaign_id,))
    conn.commit()
    print("Campaign deleted successfull")
    
#SEARCH CAMPAIGN
def search_campaign():
    campaign_id=int(input("Enter campaign ID to search:"))

    query="select * from campaign where campaign_id=%s"
    
    cursor.execute(query,(campaign_id,))
    row=cursor.fetchone()
    
    if row:
        print("\nCampaign Found\n")
        print("Campaign ID   :",row[0])
        print("Campaign Name :",row[1])
        print("Location      :",row[2])
        print("Date          :",row[3])
        print("Time          :",row[4])
    else:
        print("Campaign not found")
        
#VIEW REGISTRATION COUNT
def view_registration_count():

    query = """
    SELECT
        c.campaign_id,
        c.campaign_name,
        COUNT(cr.donor_id) AS total_members
    FROM campaign c
    LEFT JOIN campaign_registration cr
        ON c.campaign_id = cr.campaign_id
    GROUP BY c.campaign_id, c.campaign_name
    ORDER BY c.campaign_id
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nCampaign ID\tCampaign Name\tRegistered Members")
    print("--------------------------------------------------------")

    for row in rows:
        print(row[0], "\t\t", row[1], "\t\t", row[2])

#VIEW REGISTERED MEMBERS
def view_registered_members():

    campaign_id = int(input("Enter Campaign ID: "))

    query = """
    SELECT
        d.donor_id,
        d.donor_name,
        d.blood_group,
        d.gender,
        d.age,
        d.phone,
        d.email,
        cr.registration_date
    FROM campaign_registration cr
    INNER JOIN donor d
        ON cr.donor_id = d.donor_id
    WHERE cr.campaign_id = %s
    """

    cursor.execute(query, (campaign_id,))
    rows = cursor.fetchall()

    if rows:

        print("\n================ Registered Members ================")
        print("ID\tName\tBlood\tGender\tAge\tPhone\t\tEmail\t\t\tRegistered On")

        for row in rows:
            print(
                row[0], "\t",
                row[1], "\t",
                row[2], "\t",
                row[3], "\t",
                row[4], "\t",
                row[5], "\t",
                row[6], "\t",
                row[7]
            )

    else:
        print("No members registered for this campaign.")        

    
