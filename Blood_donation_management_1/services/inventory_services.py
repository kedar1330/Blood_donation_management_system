from models.inventory import BloodInventory
from db import conn, cursor
def add_blood_inventory(blood_group, units_available):

    new_inventory = BloodInventory(None, blood_group, units_available)

    query = """
    INSERT INTO blood_inventory (blood_group, units_available)
    VALUES (%s, %s)
    """

    values = (
        new_inventory.blood_group,
        new_inventory.units_available
    )

    cursor.execute(query, values)
    conn.commit()

    print("Blood inventory added successfully.")

def view_blood_inventory():

    query = "SELECT * FROM blood_inventory"

    cursor.execute(query)

    rows = cursor.fetchall()

    inventory_list = []

    for row in rows:

        inventory = BloodInventory(
            row[0],   # i_id
            row[1],   # blood_group
            row[2]    # units_available
        )

        inventory_list.append(inventory)

    return inventory_list

def update_blood_inventory(i_id, blood_group, units_available):

    query = """
    UPDATE blood_inventory
    SET blood_group = %s, units_available = %s
    WHERE i_id = %s
    """

    values = (blood_group, units_available, i_id)

    cursor.execute(query, values)
    conn.commit()

    print("Blood inventory updated successfully.")

def delete_blood_inventory(i_id):

    query = "DELETE FROM blood_inventory WHERE i_id = %s"

    cursor.execute(query, (i_id,))
    conn.commit()

    print("Blood inventory deleted successfully.")
    
