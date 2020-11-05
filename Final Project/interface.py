"""
This is the user interface where the program interacts with the user.
USAGE: 1. Go to sqlconfig.conf file and change the username and password
          values to the ones from you are using in your mysql instance
       2. Open a terminal windows and run the following command:
       python3 user_interface.py
"""
registered_users = []
logged_users = {}

def write_in_file(query, file):
    with open(file, 'a') as f:
       f.write(query)


def joins(table, attribute_from_table, attribute_from_main_table):
    query = """ JOIN {} ON {} = {} """.format(table, attribute_from_table, attribute_from_main_table)
    return query


#def select_query(table):
   #query = """SELECT * from products"""
   #join1 = joins("checkOut", "checkOut.check_out_id", "products.check_out_id")
    #return query + join1


def show_tables_by_role(role):
    query = """SELECT tablename FROM table_permissions WHERE user_role = %s"""
    values = role
    tables = db.select(query, values)
    for table in tables:
        print(table)


def show_menu():
    """
    Prints in console the main menu
    :return: VOID
    """
    print("User Menu \n"
          "1. Create Account \n"
          "2. Login \n"
          "3. Search \n"
          "4. Insert \n"
          "5. Update \n"
          "6. Delete \n"
          "7. Exit \n")


def show_table_names(tables):
    """
    Show all the tables names
    :param tables: a list with the tables names.
                   You can get it by calling the method
                   get_table_names() from DB object
    :return: VOID
    """
    index = 1
    print("\nTables:")
    for table in tables:
        print(table[0])  # print tables names
        index += 1

def create_account():
    username = input("Your username: ")
    password = input("Password: ")
    roles = input("Role, enter [admin] or [user]: ")
    query = """INSERT INTO Account (username, password, roles) VALUES (%s, %s, %s)"""
    transaction_query = """INSERT INTO Account (username, password, roles) VALUES ({}, {}, {});""".format(username, password, roles)
    values = (username, password, roles)
    if db.insert(query=query, values=values):
        print("Account created") # true
        write_in_file(transaction_query, "transactions.sql")
    else:
        print("Failed")


def login():
    username = input("Your username: ")
    password = input("Password: ")
    query = """SELECT username, password, roles from Account where username = %s AND password = %s"""
    values = (username, password)
    results = db.select(query, values)
    if len(results) == 0:
        print("You are not in the system")
    else:
        for result in results:
            username = result[0]
            password = result[1]
            role_from_table = result[2]
            user_data = {'user': username, 'password': password, 'roles': role_from_table}
            print("you are logged into the system")
            return user_data


def option3(db_object, tables):
    """
    Search option
    :param db_object: database object
    :param tables: the name of the tables in the database, I only listed out 10 example tables, for trying option3,
                   please choose any one of the ten tables
    :return: VOID
    """
    try:
        # get user input
        table_selected = input("\nSelect a table to search: ")
        attribute_selected = input("Search by (i.e name)? ")
        value_selected = input("Enter the value: ")

        columns = db_object.get_column_names(table_selected)  # get columns names for the table selected

        # build queries with the user input
        query = """SELECT* FROM {} WHERE {} = %s""".format(table_selected, attribute_selected)
        if table_selected == "businessOwner":
            query = """SELECT * FROM businessOwner WHERE businessOwner.{} = %s""".format(attribute_selected)
        elif table_selected == "company":
            query = """SELECT * FROM company WHERE company.{} = %s""".format(attribute_selected)
        elif table_selected == "department":
            query = """SELECT * FROM department  WHERE department.{} = %s""".format(attribute_selected)
        elif table_selected == "store":
            query = """SELECT * FROM store WHERE store.{} = %s""".format(attribute_selected)
        elif table_selected == "warehouse":
            query = """SELECT * FROM warehouse WHERE warehouse.{} = %s""".format(attribute_selected)
        elif table_selected == "person":
            query = """SELECT person.SSN, person.name, person.email, person.dob, person.date_joined, 
            person.is_supervisor, person.company_id, company.company_id, company.name, company.email, 
            company.address, company.phone 
            FROM person JOIN company ON company.company_id=person.company_id
            WHERE person.{} = %s""".format(attribute_selected)
            columns = columns + db_object.get_column_names("company")
        elif table_selected == "products":
            query = """SELECT products.product_id, products.product_name, products.product_SKU, products.check_out_id,
            checkOut.check_out_id, checkOut.total, checkOut.quantity 
            FROM products JOIN checkOut ON checkOut.check_out_id = products.check_out_id
            WHERE products.{} = %s""".format(attribute_selected)
            columns = columns + db_object.get_column_names("checkOut")

        elif table_selected == "delivery":
            query = """SELECT delivery.delivery_id, delivery.shipping_company_id, delivery.customer_id, 
            delivery.delivery_date, shippingCompany.shipping_company_id, shippingCompany.phone_number, 
            shippingCompany.name, customer.customer_id, customer.email, customer.shipping_address
            FROM delivery
            JOIN shippingCompany ON shippingCompany.shipping_company_id = delivery.shipping_company_id
            JOIN customer ON customer.customer_id = delivery.customer_id
            WHERE delivery.{} = %s""".format(attribute_selected)
            columns = columns + db_object.get_column_names("shippingCompany")+db_object.get_column_names("customer")
        elif table_selected == "request":
            query = """SELECT request.request_id, request.manager_id, request.supplier_id, manager.manager_id,
             manager.SSN, manager.name, supplier.supplier_id, supplier.company_name, supplier.address
            FROM request
            JOIN manager ON manager.manager_id = request.manager_id
            JOIN supplier ON supplier.supplier_id = request.supplier_id
            WHERE request.{} = %s""".format(attribute_selected)
            columns = columns + db_object.get_column_names("manager") + db_object.get_column_names("supplier")
        elif table_selected == "relation":
            query = """SELECT relation.relationship_id, relation.SSN, relation.dependent_id,
            person.SSN, person.name, person.email, person.dob, person.date_joined, 
            person.is_supervisor, person.company_id, dependent.dependent_id, dependent.name, dependent.address
            FROM relation
            JOIN person ON person.SSN = relation.SSN
            JOIN dependent ON dependent.dependent_id= relation.dependent_id
            WHERE relation.{} = %s""".format(attribute_selected)
            columns = columns + db_object.get_column_names("person") + db_object.get_column_names("dependent")
        elif table_selected == "onlineStore": # the store_id starts from 4, I have 4,5,6 in the insert.sql
            query = """SELECT onlineStore.URL, onlineStore.bestseller, onlineStore.store_id, store.store_id, 
            store.address, store.phone
            FROM onlineStore
            JOIN store ON onlineStore.store_id= store.store_id
            WHERE onlineStore.{} = %s""".format(attribute_selected)
            columns = columns + db_object.get_column_names("store")
        else:
            print("No valid table selected!")
        value = value_selected
        # get the results from the above query
        results = db_object.select(query=query, values=value)
        column_index = 0

        # print results
        print("\n")
        print("Results from: " + table_selected)
        for column in columns:
            values = []
            for result in results:
                values.append(result[column_index])
            print("{}: {}".format(column[0], values)) # print attribute: value
            column_index+= 1
        print("\n")

    except:  # handle error
         print("The data requested couldn't be found\n")


# option 4 when user selects insert
def option4(db_object, tables):
    try:
        # get user input for insert
        table = input("\nEnter a table to insert data: ")
        attributes_str = input("Enter the name attribute/s separated by comma? ")
        values_str = input("Enter the values separated by comma: ")

        # from string to list of attributes and values
        if "," in attributes_str:  # multiple attributes
            attributes = attributes_str.split(",")
            values = values_str.split(",")
        else:  # one attribute
            attributes = [attributes_str]
            values = [values_str]
        transaction_query = """INSERT INTO userInsert (table, attributes_str, values_str) VALUES ({}, {}, {});""".format(table, attributes_str, values_str)
        if db_object.insert(table=table, attributes=attributes, values=values):
            write_in_file(transaction_query, "transactions.sql")
            print("Data successfully inserted into {} \n".format(table))

    except: # data was not inserted, then handle error
        print("Error:", values, "failed to be inserted in ", table, "\n")

# option 5 when user selects insert
def option5(db_object, tables):
    # implement all the logic for option 5
    table = input("Table to update: ")
    attribute = input("Attribute to be updated: ")
    where_condition = input("condition: ")
    old_value = input("Old value: ")
    new_value = input("New value: ")
    query = """UPDATE {} SET {} = %s WHERE {} = %s""".format (table, attribute, where_condition)
    transaction_query = """UPDATE {} SET {} = %s WHERE {} = {}""".format (table, attribute, where_condition, new_value)
    values =(new_value, old_value)
    if db.update (query, values):
        write_in_file(transaction_query, "transactions.sql")
        print(" {} was updated in {}". format (new_value, table))
    else:
        print("Update fail")

# option 6 when user deletes data
def option6(db_object, tables):
    try:
        # get user input for delete
        table = input("\nEnter a table to delete data: ")
        attributes = input("Enter attribute")
        value = input("value: ")

        query = """delete from {} where {} = %s""".format(table,attributes)
        transaction_query = """delete from {} where {} = %s""".format(table,attributes)
        values = value
        if db_object.delete(query=query, values=values):
            write_in_file(transaction_query, "transactions.sql")
            print("Data successfully deleted from {} \n".format(table))

    except: # data was not inserted, then handle error
        print("Error:", value, "failed to deleted from ", table, "\n")

##### Driver execution.....
from database import DB

print("Setting up the database......\n")

# DB API object
db = DB(config_file="sqlconfig.conf")

# create a database (must be the same as the one is in your config file)
database = "storedb"


if db.create_database(database=database, drop_database_first=True):
    print("Created database {}".format(database))
else:
    print("An error occurred while creating database {} ".format(database))


# create all the tables from databasemodel.sql
db.run_sql_file("databasemodel.sql")

# insert sample data from insert.sql
db.run_sql_file("insert.sql")




#tables = db.get_table_names()
tables = None



show_menu()
option = int(input("Select one option from the menu: "))
while option != 7:
    if logged_users:  # if there is a user logged into the system
        role = logged_users['roles']
        print("This is the role " + role)
        tables = show_tables_by_role(role)
    else:
        print("You are not logged into the system")
    if option == 1:
        create_account()
    elif option == 2:
        logged_users = login()
    elif option == 3:
        option3(db, tables)
    elif option == 4:
        option4(db, tables)
    elif option == 5:
        option5(db, tables)
    elif option == 6:
        option6(db, tables)
    show_menu()
    option = int(input("Select one option from the menu: "))
print("You are exiting, bye!")
