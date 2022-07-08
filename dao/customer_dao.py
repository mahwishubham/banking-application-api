import psycopg
from model.customer import Customer


class CustomerDao:

    def insert_customers(self, customer):
        command = (
            '''
            insert into customers(last_name, first_name, middle_initial, street, city, state, zip, phone, email) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *;
            '''
        )
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
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
                inserted_row = cur.fetchone()
                return Customer(*inserted_row)

        except Exception as e:
            print(e)
        return None

    def get_customers(self):
        command = "select * from customers;"
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command)
                    customers = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for data in customers:
                        body.append(Customer(*data))
                    return body

        except Exception as e:
            print(e)
        return None

    def get_customer(self, customer_id):
        command = "select * from customers where customer_id = %s"

        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [customer_id], binary=True)
                    data = cur.fetchone()
                    body = Customer(*data)
                    return body

        except Exception as e:
            print(e)
        return None

    def update_customer(self, customer_id, data):
        command = ('''UPDATE customers SET 
                        last_name=(%s), 
                        first_name=(%s), 
                        middle_initial=(%s), 
                        street=(%s), 
                        city=(%s),
                        state=(%s), 
                        zip=(%s), 
                        phone=(%s), 
                        email=(%s) where customer_id = %s RETURNING *''')

        customer_data = self.get_customer(customer_id)
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    print(customer_data)
                    cur.execute(command, (data.get("last_name") or customer_data.get('body').get("last_name"),
                                          data.get("first_name") or customer_data.get('body').get("first_name"),
                                          data.get("middle_initial") or customer_data.get('body').get("middle_initial"),
                                          data.get("street") or customer_data.get('body').get("street"),
                                          data.get("city") or customer_data.get('body').get("city"),
                                          data.get("state") or customer_data.get('body').get("state"),
                                          data.get("zip") or customer_data.get('body').get("zip"),
                                          data.get("phone") or customer_data.get('body').get("phone"),
                                          data.get("email") or customer_data.get('body').get("email"),
                                          customer_id)
                                )
                    conn.commit()
                    updated_data = cur.fetchone()
                    if updated_data is None:
                        body = None
                    else:
                        print("updated data")
                        body = Customer(*updated_data)
                    return body

        except Exception as e:
            print(e)

        return None

    def delete_customer(self, customer_id):
        command = ("DELETE FROM customers WHERE customer_id = %s")

        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [customer_id], binary=True)
                    conn.commit()
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

