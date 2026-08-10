from db import conn,cursor
from models.campaign import Campaign

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
        

def view_registered_members_for_campaign():

    query = """
    SELECT
        id,
        campaign_id,
        donor_name,
        age,
        gender,
        blood_group,
        phone
    FROM user_campaign
    ORDER BY campaign_id, donor_name
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    return rows
    
