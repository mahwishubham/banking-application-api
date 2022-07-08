from flask import Blueprint, request
from model.customer import Customer
from service.account_service import AccountService
# from exception.invalid_parameter import InvalidParameterError
from exception.exception_customer import CustomerNotFoundError

ac = Blueprint('customer_controller', __name__)

# Instantiate a UserService object
account_service = AccountService()


@ac.route('/customers/<string:customer_id>/accounts', methods=["POST", "GET"])
def customer_accounts(customer_id):
    if request.method == "POST":
        data = request.get_json()
        res = account_service.add_account(customer_id, data)
        return res
    elif request.method == "GET":
        # GET / customer / {customer_id} / accounts?amountLessThan = 1000 & amountGreaterThan = 300:
        # Get all accounts for customer id of X with balances between Y and Z ( if customer exists)
        amountLessThan = request.args.get("amountLessThan") or 2147483647
        amountGreaterThan = request.args.get("amountGreaterThan") or -2147483648
        res = account_service.get_all_customer_account(customer_id, amountGreaterThan, amountLessThan)
        return res


@ac.route('/customers/<string:customer_id>/accounts/<string:account_id>', methods=["GET", "PUT", "DELETE"])
def customer_account(customer_id, account_id):
    if request.method == "GET":
        res = account_service.get_account_by_id(account_id)
        return res
    elif request.method == "PUT":
        data = request.get_json()
        res = account_service.update_account_by_id(account_id, data)
        return res
    elif request.method == "DELETE":
        res = account_service.delete_account_by_id(account_id)
        return res

@ac.route('/accounts')
def accounts():
    amountLessThan = request.args.get("amountLessThan") or 2147483647
    amountGreaterThan = request.args.get("amountGreaterThan") or -2147483648
    return account_service.get_all_accounts(amountGreaterThan, amountLessThan)
