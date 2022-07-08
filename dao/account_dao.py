import psycopg
from datetime import date
from model.account import Account


class AccountDao:

    def get_customer_account(self, customer_id, amountGreaterThan, amountLessThan):
        command = f"select * from accounts WHERE balance BETWEEN  {amountGreaterThan} AND {amountLessThan} and customer_id=(%s);"
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [customer_id], binary=True)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for account in data:
                        body.append(Account(*account))

                    return body

        except Exception as e:
            print(e)
        return None

    def get_accounts(self, amountGreaterThan, amountLessThan):
        command = f"select * from accounts WHERE balance BETWEEN  {amountGreaterThan} AND {amountLessThan};"
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for account in data:
                        body.append(Account(*account))

                    return body

        except Exception as e:
            print(e)
        return None

    def get_account(self, account_id):
        command = "select * from accounts where account_id = %s"

        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [account_id], binary=True)
                    account = cur.fetchone()
                    account_obj = Account(*account)
                    return account_obj

        except Exception as e:
            print(e)
        return None

    def update_account(self, account_id, data):
        command = ('''UPDATE accounts SET 
                        description=(%s), 
                        balance=(%s) where account_id=(%s) RETURNING *''')

        account_data = self.get_account(account_id)
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (
                        data.get("description") or account_data.get("body").get("description"),
                        data.get("balance") or account_data.get("body").get("balance"),
                        account_id))
                    conn.commit()
                    updated_data = cur.fetchone()
                    if updated_data is None:
                        body = None
                    else:
                        print("updated data")
                        body = Account(*updated_data)
                    return body

        except Exception as e:
            print(e)

        return None

    def delete_account(self, account_id):
        command = ("DELETE FROM accounts WHERE account_id = %s")

        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [account_id], binary=True)
                    # Check number of rows that were deleted
                    rows_deleted = cur.rowcount

                    if rows_deleted != 1:
                        return False
                    else:
                        conn.commit()
                        return True

        except Exception as e:
            print(e)
        return False

    def insert_accounts(self, customer_id, account):
        command = (
            '''
            insert into accounts(date_opened, description, balance, account_type_code, customer_id) 
            VALUES (%s,%s,%s,%s,%s) RETURNING *;
            '''
        )
        message = {}
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (
                        date.today(),
                        account.get('description'),
                        account.get('balance'),
                        account.get('account_type_code'),
                        customer_id
                    ))
                    conn.commit()
                    inserted_row = cur.fetchone()
                    return Account(*inserted_row)

        except Exception as e:
            print(e)

        return None
