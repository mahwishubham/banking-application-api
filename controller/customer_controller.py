from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
# from exception.invalid_parameter import InvalidParameterError
from exception.exception_customer import CustomerNotFoundError

cc = Blueprint('customer_controller', __name__)

# Instantiate a UserService object
customer_service = CustomerService()


# Get all users (READ)
# Get user by id (READ)
# Add users (CREATE)
# Delete user by id (DELETE)
# Update user by id (UPDATE)


@cc.route('/customers', methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        data = request.get_json()  # reading data sent from postman
        res = customer_service.add_customer(data)
        return res
    elif request.method == "GET":
        res = customer_service.get_all_customers()
        return res


@cc.route('/customers/<string:customer_id>', methods=["GET", "PUT", "DELETE"])
def customer(customer_id):
    if request.method == "GET":
        res = customer_service.get_customer_by_id(customer_id)
        return res
    elif request.method == "PUT":
        data = request.get_json()
        res = customer_service.update_customer_by_id(customer_id, data)
        return res
    elif request.method == "DELETE":
        res = customer_service.delete_customer_by_id(customer_id)
        return res
