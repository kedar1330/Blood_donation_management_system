class BloodRequestManagement:

    def __init__(self,
                 req_id,
                 hospital_name,
                 blood_group,
                 units_required,
                 request_date,
                 request_status,
                 remarks):

        self.req_id = req_id
        self.hospital_name = hospital_name
        self.blood_group = blood_group
        self.units_required = units_required
        self.request_date = request_date
        self.request_status = request_status
        self.remarks = remarks

    def __str__(self):
        return (
            f"Request ID      : {self.req_id}\n"
            f"Hospital Name   : {self.hospital_name}\n"
            f"Blood Group     : {self.blood_group}\n"
            f"Units Required  : {self.units_required}\n"
            f"Request Date    : {self.request_date}\n"
            f"Status          : {self.request_status}\n"
            f"Remarks         : {self.remarks}"
        )