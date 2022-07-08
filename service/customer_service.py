from dao.customer_dao import CustomerDao
# from exception.invalid_parameter import InvalidParameterError
# from exception.user_already_exists import UserAlreadyExistsError
from exception.exception_customer import CustomerNotFoundError


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    # Get a list of User objects from the DAO layer
    # convert the User objects into dictionaries
    # return a list of dictionaries that each represent the users
    def get_all_customers(self):
        list_of_customer_objects = self.customer_dao.get_customers()

        # Method #1, use a for loop and do it manually
        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries

        # Method #2, use map
        # return list(map(lambda x: x.to_dict(), list_of_user_objects))

    # Get User object from DAO and convert into a dictionary
    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer(customer_id)
        # object

        if customer_obj is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()

    # If user is deleted successfully, then return None (implicitly)
    # If user does not exist, raise UserNotFoundException
    def delete_customer_by_id(self, customer_id):
        # Execute this block of code if user_dao.delete_user_by_id returns False (which means that we did not delete
        # any record)
        if not self.customer_dao.delete_customer(customer_id):
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

    # 1. Check if username is at least 6 characters
    # 2. Check if username contains spaces (not allowed)
    # 3. Check if user already exists
    # Invoke add_user in DAO, passing in a user_object
    # Return the dictionary representation of the return value from that method
    def add_customer(self, customer_objs):
        # Validate data before posting

        added_customer_object = []
        for customer in customer_objs:
            added_customer_object.append(self.customer_dao.insert_customers(customer))

        return added_customer_object.to_dict()

    def update_customer_by_id(self, customer_id, customer_obj):
        updated_customer_object = self.customer_dao.update_customer(customer_id, customer_obj)

        if updated_customer_object is None:
            raise CustomerNotFoundError(f"Customer with id {customer_obj.customer_id} was not found")

        return updated_customer_object.to_dict()

