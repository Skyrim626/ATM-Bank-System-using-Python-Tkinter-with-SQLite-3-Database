from time import strftime
from datetime import date

from cardHolder_Database import generate_card, search_username_details as copy_username, search_card_details as copy_id, update_card_details
#from cardHolder_Database import check_card_number_info

"""class CardHolder:
    
    def __init__(self, first_name, last_name, username, zip_code, account_number, password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.zip_code = zip_code
        self.account_number = account_number
        self.password = password
        
    def register(self):
        time_format = strftime("%I:%M %p")
        with open('Customer_Registrations/Customer Account.txt', 'a') as f:
            f.write(f'\n\nDate registered: {date.today()}\nTime: {time_format}\nFirst name: {self.first_name}\nLast name: {self.last_name}\nUsername: {self.username}\nAccount number: {self.account_number}\nPassword: {self.password}\nZip code: {self.zip_code}\n\n')
            
        with open('Customer_Registrations/Account_ID.txt', 'a') as f:
            f.write(f"\n{self.account_number}\n{self.username}")
        
        generate_card(self.first_name, self.last_name, self.username, self.zip_code, self.account_number, self.password)
        
        return 'Congratulations! Your info has been registered! You may now login at Orion ATM Bank!'"""
        



class CardHolder:
    def __init__(self, first_name, last_name, username, zip_code, account_number, password, income):
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username.replace('@orion.com', '').replace(' ', '')
        self.zip_code = zip_code
        self.account_number = account_number
        self.password = password
        self.income = income
        
    def create_Card(self, path):
        """This creates/updates a card"""
     
        """first_name = self.first_name
        last_name = self.last_name
        username = self.username
        zip_code = self.zip_code
        account_number = self.account_number
        password = self.password"""
        
        if self.income == "":
            self.income = 1500.0
        
        self.message = ''
        
            
        if self.check_length('check_name', self.first_name, self.last_name):
            return False, self.message
                
        if self.check_digit(self.first_name + self.last_name):
            return False, self.message
                    
        if self.check_length('check_username', self.username):
            return False, self.message
                
        if self.if_already_exist('username', self.username):
            return False, self.message
        
        try:
            zip_code = int(self.zip_code)
        
            if self.check_length('check_zipcode', str(self.zip_code)):
                    
                return False, self.message
                    
            account_number = int(self.account_number)
            if self.check_length('check_acc_num', str(self.account_number)):
                    
                return False, self.message
                    
            password = int(self.password)
            if self.check_length('check_pass', str(self.password)):
                return False, self.message
            
        except:
            self.message = 'Account ID, Zip Code and Password must only contain digits not alphabets!'
            return False, self.message
        
        try:
            self.income = float(self.income)
            
        except:
            self.message = 'Income must be numbers!'
            return False, self.message
        
        if path == 'create_card':
            print(self.account_number)
            print(type(self.account_number))
            #-----This creates a card-----#
            generate_card(self.first_name, self.last_name, self.username + '@orion.com', int(self.account_number), int(self.zip_code), int(self.password), self.income)
            
            #Saves through text file
            self.register()
            
            self.message = 'Congratulations! Your info has been registered! You may now login at Orion ATM Bank!'
            
            return True, self.message
            
            
            
    def update_user_card(self):
        """This updates users card"""
        
        if self.income == "" or self.income == "0.0":
            self.income = 1500.0
            
        
        if self.check_length('check_name', self.first_name, self.last_name):
            
            return False, self.message
        
        try:
            zip_code = int(self.zip_code)
        
            if self.check_length('check_zipcode', str(self.zip_code)):
                    
                return False, self.message
                    
            account_number = int(self.account_number)
            
            password = int(self.password)
            if self.check_length('check_pass', str(self.password)):
                return False, self.message
            
        except:
            self.message = 'Account ID, Zip Code and Password must only contain digits not alphabets!'
            return False, self.message
        
        try:
            self.income = float(self.income)
            
        except:
            self.message = 'Income must be numbers!'
            return False, self.message
        
        #-----This creates a card-----#
        update_card_details(self.first_name, self.last_name, self.username + '@orion.com', self.account_number, self.zip_code, self.password, float(self.income))
            
        self.message = 'User card has been updated!'
        
        return True, self.message
    
    
    
    def if_already_exist(self, path, key):
        """Check if this account already exists"""
        
        if path == 'username':
            try:
                if key == copy_username(key+'@orion.com')[2]:
                    self.message = 'This Username is already exists! Use different username!'
                    return True
                
                
            except:
                return False
                
        else:
            try:
                if int(key1) == copy_id(key1)[3]:
                    self.message = 'This Acc ID is already exists! Use different ID!'
                    return True
                
            except:
                return False
    
    
    def check_digit(self, complete_name):
        """Returns True if a string contain digits"""
        
        for alphabet in complete_name:
            if alphabet.isdigit():
                self.message = 'Name has digit! Try Again!'
                return True
        
        return False
    
    
    def check_length(self, path, key1 = None, key2 = None):
        """Return True of the length of the string is exceed from the expectations"""

        if path == 'check_name':
            if len(key1) <= 2 or len(key2) <= 2:
                self.message = "Name is too short! Must not atleast 2 alphabet"
                return True
            
        elif path == 'check_username':
            if len(key1) <= 4 or len(key1) >= 11:
                self.message = 'Username is short or high! Must at least 7 or 10'
                return True
                
                
        elif path == 'check_zipcode':
            if len(key1) > 11 or len(key1) < 4:
                self.message = 'Zip Code must between 4 or 10 digits only!'
                return True
                
        elif path == 'check_acc_num':
            if len(key1) != 6:
                self.message = 'Account Number must only need 6 digits code!'
                return True
            
        else:
            if len(key1) != 4:
                self.message = 'Password must only need 4 digit code'
                return True

    
    def register(self):
        time_format = strftime("%I:%M %p")
        
        with open('Customer_Registrations/Customer Account.txt', 'a') as f:
            f.write(f'\n\nDate registered: {date.today()}\nTime: {time_format}\nFirst name: {self.first_name}\nLast name: {self.last_name}\nUsername: {self.username}\nAccount number: {self.account_number}\nPassword: {self.password}\nZip code: {self.zip_code}\n\n')
            
        with open('Customer_Registrations/Account_ID.txt', 'a') as f:
            f.write(f"\n{self.account_number}\n{self.username}")














            