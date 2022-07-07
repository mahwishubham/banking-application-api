CREATE TABLE account_types (
	account_type_code text PRIMARY key CHECK (account_type_code in ('SLRY','CURR','SAVE')),
	description VARCHAR(200) NOT null
);


insert into account_types(account_type_code, description) values ('SLRY', 'Salary Account');
insert into account_types(account_type_code, description) values ('CURR', 'current Account');
insert into account_types(account_type_code, description) values ('SAVE', 'SAVING Account');


CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  last_name VARCHAR (20) NOT NULL,
  first_name VARCHAR (20) NOT NULL,
  middle_initial VARCHAR (1),
  street VARCHAR (100) NOT NULL,
  city VARCHAR (30) NOT NULL,
  state VARCHAR (30) NOT NULL,
  zip INT NOT NULL,
  phone VARCHAR (12) NOT null CHECK(phone SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
  email VARCHAR (50) unique NOT null check (email like '%_@__%.__%')
)

CREATE TABLE accounts(
	account_id serial primary key,
	date_opened Date Not Null,
	description VARCHAR(200) NOT NULL,
	balance integer not null,
	account_type_code text REFERENCES account_types (account_type_code),
	customer_id serial REFERENCES customers (customer_id)
)