import os
from pony.orm import Database, PrimaryKey, Required, sql_debug, db_session

pg_conn_string = os.environ["PG_CONN_STRING"]

db = Database()


class Drug(db.Entity):
    _table_ = 'drugs'
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    inventory = Required(int)
    price = Required(float)


db.bind('postgres', pg_conn_string)  # Bind Database object to the real database
# Create tables if they do not exist. Noop if they do exist
db.generate_mapping(create_tables=True)

@db_session
def create_drug(name, inventory, price):
    Drug(name=name, inventory=inventory, price=price)

@db_session
def get_drug(name):
    drug = Drug.get(name=name)
    if drug is None:
        return None
    else:
        return drug.to_dict()

@db_session
def update_stock(name, new_inventory):
    drug = Drug.get(name=name)
    drug.inventory = new_inventory

@db_session
def delete_drug(name):
    drug = Drug.get(name)
    drug.delete()
 
#create_drug("Mustard", 150, 3.99)
#a_drug = get_drug("Salt")
#update_stock(a_drug['name'], a_drug['inventory']-1)
#print(a_drug)
