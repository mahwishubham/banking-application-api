import psycopg
from flask import Flask, request
from datetime import date
app = Flask(__name__)


def insert_customers(data):
    command = (
        '''
        insert into customers(last_name, first_name, middle_initial, street, city, state, zip, phone, email) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
        '''
    )
    message = {}
    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                for customer in data:
                    cur.execute(command, (
                        customer.get('last_name'),
                        customer.get('first_name'),
                        customer.get('middle_initial'),
                        customer.get('street'),
                        customer.get('city'),
                        customer.get('state'),
                        customer.get('zip'),
                        customer.get('phone'),
                        customer.get('email')
                    ))
            conn.commit()
            message = {'status': 200, 'msg': 'data inserted success'}

    except Exception as e:
        print(e)
        print('create command failed')
        message = {'status': 404, 'msg': 'data inserted failed'}
    return message


def insert_accounts(customer_id, data):
    command = (
        '''
        insert into accounts(date_opened, description, balance, account_type_code, customer_id) 
        VALUES (%s,%s,%s,%s,%s);
        '''
    )
    message = {}
    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                for account in data:
                    cur.execute(command, (
                        date.today(),
                        account.get('description'),
                        account.get('balance'),
                        account.get('account_type_code'),
                        customer_id
                    ))
            conn.commit()
            message = {'status': 200, 'msg': 'data inserted success'}

    except Exception as e:
        print(e)
        print('create command failed')
        message = {'status': 404, 'msg': 'data inserted failed'}
    return message


def get_customers():
    command = "select * from customers;"
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                customers = cur.fetchall()  # fetching all rows from customer's table
                body = []
                for data in customers:
                    body.append({
                        "customer_id": data[0],
                         "last_name": data[1],
                         "first_name": data[2],
                         "middle_initial": data[3],
                         "street": data[4],
                         "city": data[5],
                         "state": data[6],
                         "zip": data[7],
                         "phone": data[8],
                         "email": data[9],

                    })
                message = {'status': 200, 'body': body}

    except Exception as e:
        print(e)
        message = {'status': 404, 'body': None}
    return message


def get_customer(customer_id):
    command = "select * from customers where customer_id = %s"
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command, [customer_id], binary=True)
                data = cur.fetchone()
                body = { "customer_id": data[0],
                            "last_name": data[1],
                            "first_name" : data[2],
                            "middle_initial":data[3],
                            "street":data[4],
                            "city":data[5],
                            "state":data[6],
                            "zip":data[7],
                            "phone":data[8],
                            "email":data[9],
                         }
                message = {'status': 200, 'body': body}

    except Exception as e:
        print(e)
        message = {'status': 404, 'body': None}
    return message


def get_customer_account(customer_id, amountGreaterThan, amountLessThan):
    command = f"select * from accounts WHERE balance BETWEEN  {amountGreaterThan} AND {amountLessThan} and customer_id=(%s);"
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command, [customer_id], binary=True)
                data = cur.fetchall()  # fetching all rows from customer's table
                body = []
                for account in data:
                    body.append(
                        {
                            "account_id": account[0],
                            "date_opened": account[1],
                            "description": account[2],
                            "balance": account[3],
                            "account_type_code": account[4],
                            "customer_id": account[5],
                        }
                    )
                message = {'status': 200, 'body': body}

    except Exception as e:
        print(e)
        message = {'status': 404, 'body': None}
    return message


def get_accounts(amountGreaterThan, amountLessThan):
    command = f"select * from accounts WHERE balance BETWEEN  {amountGreaterThan} AND {amountLessThan};"
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                data = cur.fetchall()  # fetching all rows from customer's table
                body = []
                for account in data:
                    body.append(
                        {
                            "account_id": account[0],
                            "date_opened": account[1],
                            "description": account[2],
                            "balance": account[3],
                            "account_type_code": account[4],
                            "customer_id": account[5],
                        }
                    )
                message = {'status': 200, 'body': body}

    except Exception as e:
        print(e)
        message = {'status': 404, 'body': None}
    return message


def get_account(account_id):
    command = "select * from accounts where account_id = %s"
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command, [account_id], binary=True)
                account = cur.fetchone()
                body = {
                            "account_id": account[0],
                            "date_opened": account[1],
                            "description": account[2],
                            "balance": account[3],
                            "account_type_code": account[4],
                            "customer_id": account[5],
                        }

                message = {'status': 200, 'body': body}

    except Exception as e:
        print(e)
        message = {'status': 404, 'body': None}
    return message


def update_customer(customer_id, data):
    command = ('''UPDATE customers SET 
                    last_name=(%s), 
                    first_name=(%s), 
                    middle_initial=(%s), 
                    street=(%s), 
                    city=(%s),
                    state=(%s), 
                    zip=(%s), 
                    phone=(%s), 
                    email=(%s) where customer_id = %s''')
    message = {}
    customer_data = get_customer(customer_id)
    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                print(customer_data)
                cur.execute(command, ( data.get("last_name") or customer_data.get('body').get("last_name"),
                                    data.get("first_name") or customer_data.get('body').get("first_name"),
                                    data.get("middle_initial") or customer_data.get('body').get("middle_initial") ,
                                    data.get("street") or customer_data.get('body').get("street"),
                                    data.get("city") or customer_data.get('body').get("city"),
                                    data.get("state") or customer_data.get('body').get("state"),
                                    data.get("zip") or customer_data.get('body').get("zip"),
                                    data.get("phone") or customer_data.get('body').get("phone"),
                                    data.get("email") or customer_data.get('body').get("email"),
                                    customer_id)
                         )
                conn.commit()
                message = {'status': 200, 'msg': "data update successfull"}

    except Exception as e:
        print(e)
        message = {'status': 404, 'msg': "unsuccessfull!"}
    return message


def update_account(account_id, data):
    command = ('''UPDATE accounts SET 
                    description=(%s), 
                    balance=(%s) where account_id=(%s)''')
    message = {}
    account_data = get_account(account_id)
    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command, (
                    data.get("description") or account_data.get("body").get("description"),
                    data.get("balance") or account_data.get("body").get("balance"),
                    account_id))
                conn.commit()
                message = {'status': 200, 'msg': "data update successfull"}

    except Exception as e:
        print(e)
        message = {'status': 404, 'msg': "unsuccessfull!"}
    return message


def delete_customer(customer_id):
    command = ("DELETE FROM customers WHERE customer_id = %s")
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command, [customer_id], binary=True)
                conn.commit()
                message = {'status': 200, 'msg': "Customer Deleted Success!"}

    except Exception as e:
        print(e)
        message = {'status': 404, 'msg': "Customer Deleted Fail!"}
    return message


def delete_account(account_id):
    command = ("DELETE FROM accounts WHERE account_id = %s")
    message = {}

    try:
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute(command, [account_id], binary=True)
                conn.commit()
                message = {'status': 200, 'msg': "Account Deleted Success!"}

    except Exception as e:
        print(e)
        message = {'status': 404, 'msg': "Account Deleted Fail!"}
    return message


@app.route('/')
def homepage():
    return 'Welcome to Flask WebServer'


@app.route('/customers', methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        data = request.get_json()  # reading data sent from postman
        res = insert_customers(data)
        return res
    elif request.method == "GET":
        res = get_customers()
        return res


@app.route('/customers/<string:customer_id>', methods=["GET", "PUT", "DELETE"])
def customer(customer_id):
    if request.method == "GET":
        res = get_customer(customer_id)
        return res
    elif request.method == "PUT":
        data = request.get_json()
        res = update_customer(customer_id, data)
        return res
    elif request.method == "DELETE":
        res = delete_customer(customer_id)
        return res


@app.route('/customers/<string:customer_id>/accounts', methods=["POST", "GET"])
def customer_accounts(customer_id):
    if request.method == "POST":
        data = request.get_json()
        res = insert_accounts(customer_id, data)
        return res
    elif request.method == "GET":
        # GET / customer / {customer_id} / accounts?amountLessThan = 1000 & amountGreaterThan = 300:
        # Get all accounts for customer id of X with balances between Y and Z ( if customer exists)
        amountLessThan = request.args.get("amountLessThan") or 2147483647
        amountGreaterThan = request.args.get("amountGreaterThan") or -2147483648
        res = get_customer_account(customer_id, amountGreaterThan, amountLessThan)
        return res


@app.route('/customers/<string:customer_id>/accounts/<string:account_id>', methods=["GET", "PUT", "DELETE"])
def customer_account(customer_id, account_id):
    if request.method == "GET":
        res = get_account(account_id)
        return res
    elif request.method == "PUT":
        data = request.get_json()
        res = update_account(account_id, data)
        return res
    elif request.method == "DELETE":
        res = delete_account(account_id)
        return res

@app.route('/accounts')
def accounts():
    amountLessThan = request.args.get("amountLessThan") or 2147483647
    amountGreaterThan = request.args.get("amountGreaterThan") or -2147483648
    return get_accounts(amountGreaterThan, amountLessThan)