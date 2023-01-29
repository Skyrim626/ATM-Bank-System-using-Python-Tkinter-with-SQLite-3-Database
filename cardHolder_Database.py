import sqlite3

def create_table():
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("""CREATE TABLE IF NOT EXISTS Customers_Card(
                f_name text,
                l_name text,
                username text,
                acc_num integer,
                password integer,
                zip_code integer,
                income float,
                balance float)""")
    
    conn.commit()
    conn.close()
    
def generate_card(first_name, last_name, username, account_number, password, zip_code, income):
    """Creates a Card"""
    
    balance = 0
    #income = 0
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("INSERT INTO Customers_Card VALUES (:f_name, :l_name, :username, :acc_num, :password, :zipcode, :income, :balance)", {'f_name': first_name, 'l_name': last_name, 'username': username, 'acc_num': account_number, 'password': password, 'zipcode': zip_code, 'income': income, 'balance': float(balance)})
    
    conn.commit()
    conn.close()


def check_card_number_info():
    """Return a bunch of id numbers"""
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("SELECT * FROM Customers_Card ORDER BY l_name")
    id_record = click.fetchall()
    
    return id_record


def search_card_details(id):
    """Returns a specific account depend on what id search for login system"""
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("SELECT * FROM Customers_Card WHERE acc_num = :acc_num", {'acc_num': id})
    
    return click.fetchall()
    
def delete_card_holder(id):
    """Deletes the account"""
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("DELETE FROM Customers_Card WHERE acc_num = :acc_num", {'acc_num': id})
    
    conn.commit()
    conn.close()


def search_username_details(username_):
    """Returns the searched username"""
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("SELECT * FROM Customers_Card WHERE username = :username", {'username': username_})
    
    return click.fetchone()
    
 
def update_card_details(first_name, last_name, username, account_number, password, zipcode, income):
    """This updates the card of the user"""
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("""UPDATE Customers_Card SET 
                    f_name = :f_name,
                    l_name = :l_name,
                    username = :username,
                    password = :password,
                    zip_code = :zip_code,
                    income = :income
                    
                    WHERE acc_num = :acc_num""",
                    {
                        'f_name': first_name,
                        'l_name': last_name,
                        'username': username,
                        'acc_num': account_number,
                        'password': password,
                        'zip_code': zipcode,
                        'income': income
                    
                    })
    
    conn.commit()
    conn.close()

def update_balance(id, balance):
    """Updates balance to all users"""
    
    conn = sqlite3.connect('Card_Holders.db')
    click = conn.cursor()
    
    click.execute("UPDATE Customers_Card SET balance = :balance WHERE acc_num = :acc_num", {'balance': balance, 'acc_num': id})
    id_record = click.fetchall()
    
    conn.commit()
    conn.close()


#create_table()










