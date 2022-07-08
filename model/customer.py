class Customer:
    def __init__(self, customer_id, first_name, last_name, middle_initial, street, city, state, zip, phone, email):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_initial = middle_initial
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def to_dict(self):
        '''
        This function is used return dictionary of the customer object
        '''
        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_initial": self.middle_initial,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "phone": self.phone,
            "email": self.email
        }