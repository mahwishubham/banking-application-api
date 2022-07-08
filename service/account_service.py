# from exception.invalid_parameter import InvalidParameterError
# from exception.user_already_exists import UserAlreadyExistsError
from dao.account_dao import AccountDao
from exception.exception_account import AccountNotFoundError


class AccountService:

    def __init__(self):
        self.account_dao = AccountDao()

    # Get a list of User objects from the DAO layer
    # convert the User objects into dictionaries
    # return a list of dictionaries that each represent the users
    def get_all_accounts(self, amountGreaterThan, amountLessThan):
        list_of_account_objects = self.account_dao.get_accounts(amountGreaterThan, amountLessThan)

        # Method #1, use a for loop and do it manually
        list_of_account_dictionaries = []
        for account_obj in list_of_account_objects:
            list_of_account_dictionaries.append(account_obj.to_dict())

        return list_of_account_dictionaries

        # Method #2, use map
        # return list(map(lambda x: x.to_dict(), list_of_user_objects))

    def get_all_customer_account(self, customer_id, amountGreaterThan, amountLessThan):
        list_of_customer_account_objects = self.account_dao.get_customer_account(customer_id, amountGreaterThan,
                                                                                 amountLessThan)

        # Method #1, use a for loop and do it manually
        list_of_account_dictionaries = []
        for account_obj in list_of_customer_account_objects:
            list_of_account_dictionaries.append(account_obj.to_dict())

        return list_of_account_dictionaries

    # Get User object from DAO and convert into a dictionary
    def get_account_by_id(self, account_id):
        account_obj = self.account_dao.get_account(account_id)
        # object

        if account_obj is None:
            raise AccountNotFoundError(f"Account with id {account_id} was not found")

        return account_obj.to_dict()

    # If user is deleted successfully, then return None (implicitly)
    # If user does not exist, raise UserNotFoundException
    def delete_account_by_id(self, account_id):
        # Execute this block of code if user_dao.delete_user_by_id returns False (which means that we did not delete
        # any record)
        if not self.account_dao.delete_account(account_id):
            raise AccountNotFoundError(f"Account with id {account_id} was not found")

    # 1. Check if username is at least 6 characters
    # 2. Check if username contains spaces (not allowed)
    # 3. Check if user already exists
    # Invoke add_user in DAO, passing in a user_object
    # Return the dictionary representation of the return value from that method
    def add_account(self, customer_id, account_objects):
        # Validate data before posting

        added_account_object = []
        for acccount_obj in account_objects:
            added_account_object.append(self.account_dao.insert_accounts(customer_id, acccount_obj))

        return added_account_object.to_dict()

    def update_account_by_id(self, account_id, account_obj):
        updated_account_object = self.account_dao.update_account(account_id, account_obj)

        if updated_account_object is None:
            raise AccountNotFoundError(f"Account with id {account_obj.account_id} was not found")

        return updated_account_object.to_dict()
