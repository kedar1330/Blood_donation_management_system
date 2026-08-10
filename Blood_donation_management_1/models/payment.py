class Payment:

    def __init__(self, booking_id, recipient_name, amount, payment_method, payment_status):
        self.booking_id = booking_id
        self.recipient_name = recipient_name
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status