class DonorManagement:

    def __init__(self,
                 donor_id,
                 donor_name,
                 age,
                 gender,
                 email,
                 blood_group,
                 phone):

        self.donor_id = donor_id
        self.donor_name = donor_name
        self.age = age
        self.gender = gender
        self.email = email
        self.blood_group = blood_group
        self.phone = phone

    def __str__(self):

        return (
            f"Donor ID      : {self.donor_id}\n"
            f"Name          : {self.donor_name}\n"
            f"Age           : {self.age}\n"
            f"Gender        : {self.gender}\n"
            f"Email         : {self.email}\n"
            f"Blood Group   : {self.blood_group}\n"
            f"Phone         : {self.phone}"
        )