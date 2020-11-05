"""
This is the user interface where the program interacts with the user.
USAGE: 1. Go to sqlconfig.conf file and change the username and password
          values to the ones from you are using in your mysql instance
       2. Open a terminal windows and run the following command:
       python3 user_interface.py
"""
registered_users = []
logged_users = []

def write_in_file(query, file):
    with open(file, 'a') as f:
       f.write(query)


def joins(table, attribute_from_table, attribute_from_main_table):
    query = """ JOIN {} ON {} = {} """.format(table, attribute_from_table, attribute_from_main_table)
    return query


def select_query(table):
    query = """SELECT * from track"""
    join1 = joins("album", "Album.id", "Track.album")
    return query + join1



def show_tables_by_role(role):
    query = """SELECT table FROM table_permissions WHERE role = %s"""
    values = role
    tables = db.select(query, values)
    for table in tables:
        print(table)

def create_account():
    username = input("Your username: ")
    password = input("Password: ")
    role = input("Role: ")
    query = """INSERT INTO Account (username, passsword, role) VALUES (%s, %s, %s)"""
    values = (username, password, role)
    if db.insert(query, values):
        print("Account created") # true


    else:
        print("Failed")



def login():
    username = input("Your username: ")
    password = input("Password: ")
    query = """SELECT username, password, role from Account where username = %s AND password = %s"""
    values = (username, password)
    results = db.select(query, values)
    if len(results) == 0:
        print("You are not in the system")
    else:
        for result in results:
            username_from_table = result[0]
            password_from_table = result[1]
            role_from_table = result[2]
            user_data = {'user': username, 'password': password, 'role': role_from_table}
            logged_users.append(user_data)








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

def option1 (db_object, tables):
    def __init__(self):
        self.credintials = {}

    def register(self, email, password):
        self.credintials[email] = password


    Stop = False

    while Stop == False:
        Email = (input('Please enter email'))
        Pword = (input('Please enter password'))
        option1.register(Email, Pword)
        print("You have successfully create the account!")

def option2(db_object, tables):
    def check(self, user_email, pas):
        print(self.credintials)
        if user_email in self.credintials.keys() and pas == self.credintials[user_email]:
            print("Welcome, you have successfully logged in!")
        else:
            print('Wrong email or password')

    LoginInfoUserEmail = (input('Please enter email'))
    LoginInfoPassword = (input('Please enter password'))
    option2.check(LoginInfoUserEmail,LoginInfoPassword)

def option3(db_object, tables):
    """
    Search option
    :param db_object: database object
    :param tables: the name of the tables in the database
    :return: VOID
    """
    try:
        # shows that tables names in menu
        show_table_names(tables)

        # get user input
        table_selected = input("\nSelect a table to search: ")
        attribute_selected = input("Search by (i.e name)? ")
        value_selected = input("Enter the value: ")

        columns = db_object.get_column_names(table_selected)  # get columns names for the table selected

        # build queries with the user input
        query = """SELECT * FROM {} WHERE {} = %s""".format(table_selected, attribute_selected)

        if table_selected == "track":  # only if the table selected is track because we want to join
            query = """SELECT album.title as AlbumTitle, artist.name, track.id, track.length, track.title FROM track 
                           JOIN {}} ON {}.id = track.album_id
                           JOIN {}} ON {}.id = track.artist_id
                           WHERE track.{} = %s""".format(attribute_selected)
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
            print("{}: {}".format(column[0], values) ) # print attribute: value
            column_index+= 1
        print("\n")

    except Exception as err:  # handle error
         print("The data requested couldn't be found\n")



# option 4 when user selects insert
def option4(db_object, tables):
    try:
        # show tables names
        show_table_names(tables)

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
        sql = ""
        if db_object.insert(table=table, attributes=attributes, values=values):
            write_in_file(sql, "transactions.sql")
            print("Data successfully inserted into {} \n".format(table))

    except: # data was not inserted, then handle error
        print("Error:", values_str, "failed to be inserted in ", table, "\n")

# option 5 when user selects insert
def option5(db_object, tables):
    # implement all the logic for option 5
    table = input("Table to update: ")
    attribute = input("Attribute to be updated: ")
    where_condition = input("condition: ")
    old_value = input("Old value: ")
    new_value = input("New value: ")
    query = """UPDATE {} SET {} = %s WHERE {} = %s""".format (table, attribute, where_condition)
    values =(new_value, old_value)
    if db.update (query, values):
        print(" {} was updated in {}". format (new_value, table))
    else:
        print("Update fail")

# option 6 when user deletes data
def option6(db_object, tables):
    try:
        # show tables names
        show_table_names(tables)

        # get user input for delete
        table = input("\nEnter a table to delete data: ")
        attributes = input("Enter attribute")
        value = input("value: ")

        query = """delete from {} where {} = %s""".format(table,attributes)
        values = value
        if db_object.delete(query, values):
            print("Data successfully deleted from {} \n".format(table))

    except: # data was not inserted, then handle error
        print("Error:", value, "failed to deleted from ", table, "\n")

##### Driver execution.....
from database import DB

print("Setting up the database......\n")

# DB API object
db = DB(config_file="sqlconfig.conf")

# create a database (must be the same as the one is in your config file)
database = "jose"
if db.create_database(database=database, drop_database_first=True):
    print("Created database {}".format(database))
else:
    print("An error occurred while creating database {} ".format(database))

# create all the tables from databasemodel.sql
db.run_sql_file("StoreDB.sql")

# insert sample data from insert.sql
db.run_sql_file("inserts.sql")

if db._transaction == 1:
    db.run_sql_file("transaction.sql")


print("\nSet up process finished\n")

tables = db.get_table_names()

show_menu()
option = int(input("Select one option from the menu: "))
while option != 7:


    if option == 1:
        create_account()
    elif option == 2:
        login()
    elif option == 3:
        option3(db, tables)
    elif option == 4:
        option4(db, tables)
    elif option == 5:
        option4(db, tables)
    elif option == 6:
        option4(db, tables)
    show_menu()
    option = int(input("Select one option from the menu: "))
print("You are exiting, bye!")

