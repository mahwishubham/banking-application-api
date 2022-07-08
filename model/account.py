class Account():
    def __init__(self, account_id, date_opened, description, account_type_code, balance, customer_id):
        self.account_id = account_id
        self.date_opened = date_opened
        self.description = description
        self.balance = balance
        self.account_type_code = account_type_code
        self.customer_id = customer_id

    def to_dict(self):
        '''
        This function is used return dictionary of the account object
        '''
        return {
            "account_id": self.account_id,
            "date_opened": self.date_opened,
            "description": self.description,
            "balance": self.balance,
            "account_type_code": self.account_type_code,
            "customer_id": self.customer_id
        }
