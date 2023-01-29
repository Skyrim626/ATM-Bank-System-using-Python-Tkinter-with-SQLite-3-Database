from registration_machine import CardHolder
from cardHolder_Database import check_card_number_info




def check_digit(first_name, last_name):
    
    if check_length('check_name', first_name, last_name):
        complete_name = first_name + last_name
        for alphabet in complete_name:
            if alphabet.isdigit():
                print('Name has digit! Try Again!')
                return False
                
        return True
   

def check_length(path, key1 = None, key2 = None, key3 = None):
    
    if path == 'check_name':
        if len(key1) <= 2 or len(key2) <= 2:
            print("Name is too short! Must not atleast 2 alphabet")
            return False
            
        return True
            
    elif path == 'check_username': #Check if username already exists
        if len(key1) <= 6 or len(key1) >= 11:
            print('Username is short or high! Must at least 7 or 10')
            return False
            
        return True if check_if_already_exist(key1) else False #Checks if info is already exist
        
    elif path == 'check_digit':
        if key1 == 'check_zip' and len(key2) > 11 and len(key2) > 3:
            print('Zip Code must between 4 or 10 digits only!')
            return False
            
        elif key1 == 'check_acc_num':
            if len(key2) != 6:
                print('Account Number must only need 6 digits code!')
                return False
                
            if not check_if_already_exist(key2):
                return False
        
        elif key1 == 'check_password' and len(key2) != 4:
            print('Password must only need 4 digit code')
            return False
            
        return True


def check_if_already_exist(sample):
    
    id_record = check_card_number_info()
    for user_record in id_record:
        for record in user_record:
            if sample == record:
                print('This Acc is already exists! Use different info!')
                return False
                
    return True
                
    """try:
        with open("Account_ID.txt", "r") as existed:
            for id in existed.readlines():
                if sample == id.strip():
                    print('This Acc is already exists! Use different info!')
                    return False
            
        return True
    except:
        pass"""

while True:
    print("Fill up the details to get your credit card: ")
    condition = False
    while not condition:

        first_name = input("Enter user first name: ")
        last_name = input("Enter user last name: ")
        
        condition = check_digit(first_name, last_name)
    
    condition = False
    while not condition:
        username = input("Enter your username: ")
        condition = check_length('check_username', username)
        
    condition = False
    while not condition:
        try:
            while not condition:
                zip_code = int(input("Enter zip code maximum of 10 digits and not lower than 4 digits: "))
                condition = check_length('check_digit', 'check_zip', str(zip_code))
            
            condition = False
            while not condition:
                account_number = int(input("Enter 6-digit code for account ID: "))
                condition = check_length('check_digit', 'check_acc_num', str(account_number))
            
            condition = False
            while not condition:
                password = int(input("Enter 4-digit code for password: "))
                condition = check_length('check_digit', 'check_password', str(password))
                
        
        except Exception as e:
            print('Account ID, Zip Code and Password must only contain digits not alphabets!')
            
    
    
    if condition:
        prompt = CardHolder(first_name, last_name, username, zip_code, account_number, password)
        
        condition = False
        while not condition:
            accept = input("\nAre you sure you want to create a user card?[Yes][No]: ").lower()
            
            if accept == 'yes':
                #Prints if the user has been registered
                print(prompt.register())
                condition = True
                
            elif accept == 'no':
                print('Details cancelled!')
                condition = True
                    
            else:
                print('Invalid option!')
         
    while True:
        option = input('\nContinue Register?[Yes][No]: ').lower()
        if option == 'yes':
            break
        elif option == 'no':
            print()
        else:
            print('Invalid option!')




print('\nProgam Ended. Thank You!')