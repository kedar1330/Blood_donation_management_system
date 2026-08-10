class BloodInventory:
    def __init__(self, i_id, blood_group, units_available):
        self.i_id = i_id
        self.blood_group = blood_group
        self.units_available = units_available

    def __str__(self):
        return (f"ID: {self.i_id} | "
                f"Blood Group: {self.blood_group} | "
                f"Units Available: {self.units_available}")