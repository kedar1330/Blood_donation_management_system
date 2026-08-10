import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Kedar1234#",database="Blood_donation_db")
print("Connection established")
cursor=conn.cursor()
print("Cursor established")