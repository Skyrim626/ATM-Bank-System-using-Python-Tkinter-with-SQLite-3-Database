import sqlite3

from cardHolder_Database import search_card_details

from datetime import date
from time import strftime

def create_history_table(id):
    """This creates user history table"""
    conn = sqlite3.connect('history.db')
    click = conn.cursor()
    
    user_history = "group_1_" + str(id)
    click.execute(f"CREATE TABLE IF NOT EXISTS {user_history}(date_history text, time_history text, this_history text, amount_history float, balance_history float)")
    
    conn.commit()
    conn.close()

def insert_data_history(id, cash, balance):
    """This inserts user history"""
    
    [records] = search_card_details(id)
    user_id = "group_1_" + str(records[3])
    
    current_date = str(date.today())
    current_time = strftime("%I:%M:%S %p")
    current_history = f"{records[0]} {records[1]} withdraw {str(cash)}!"
    
    conn = sqlite3.connect('history.db')
    click = conn.cursor()
    
    click.execute(f"INSERT INTO {user_id} VALUES (:date_history, :time_history, :this_history, :amount_history, :balance_history)", {'date_history': current_date, 'time_history': current_time, 'this_history': current_history, 'amount_history': cash, 'balance_history': balance})
    
    
    conn.commit()
    conn.close()

    
def display_history(id):
    """This displays user table of history in the homepage"""
    conn = sqlite3.connect('history.db')
    click = conn.cursor()

    user_history = "group_1_" + str(id)
    
    click.execute(f"SELECT * FROM {user_history}")


    return click.fetchall()


def share_data_history(id, cash, balance):
    """This inserts user history"""
    
    [records] = search_card_details(id)
    user_id = "group_1_" + str(records[3])
    
    current_date = str(date.today())
    current_time = strftime("%I:%M:%S %p")
    current_history = f"{records[0]} {records[1]} shares {str(cash)}!"
    
    conn = sqlite3.connect('history.db')
    click = conn.cursor()
    
    click.execute(f"INSERT INTO {user_id} VALUES (:date_history, :time_history, :this_history, :amount_history, :balance_history)", {'date_history': current_date, 'time_history': current_time, 'this_history': current_history, 'amount_history': cash, 'balance_history': balance})
    
    
    conn.commit()
    conn.close()



def claim_data_history(id, cash, balance):
    """This inserts user history"""
    
    [records] = search_card_details(id)
    user_id = "group_1_" + str(records[3])
    
    current_date = str(date.today())
    current_time = strftime("%I:%M:%S %p")
    current_history = f"{records[0]} {records[1]} received {str(cash)}!"
    
    conn = sqlite3.connect('history.db')
    click = conn.cursor()
    
    click.execute(f"INSERT INTO {user_id} VALUES (:date_history, :time_history, :this_history, :amount_history, :balance_history)", {'date_history': current_date, 'time_history': current_time, 'this_history': current_history, 'amount_history': cash, 'balance_history': balance})
    
    
    conn.commit()
    conn.close()








