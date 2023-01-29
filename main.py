from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mssg
from PIL import ImageTk, Image

from datetime import date
from time import strftime
from tkcalendar import*

import time
import customtkinter

#Database imports
from cardHolder_Database import search_card_details, update_balance
from history_database import create_history_table, insert_data_history, display_history, share_data_history, claim_data_history

#----To Trace my goddamn Errors!!!-----#
import traceback



class HomeForm:
    def __init__(self, Form= None, records= None):
        
        try:
            #Destroys a Form
            Form.destroy()
        except:
            pass
        
        home_window = Tk()
        home_window.title('Dashboard')
        
        [records] = search_card_details(records[3])
        #[records] = search_card_details(137491)
        self.records = records
        
        info_Frame = Frame(home_window, bg = '#1C1C1C', height = 664, width = 500, bd = 5, relief = SOLID)
        info_Frame.grid(row = 0, column = 0, sticky = ('n', 's'))
        #info_Frame.grid_propagate(False)
        info_Frame.grid_columnconfigure(0, minsize = 60)
        info_Frame.grid_columnconfigure(2, minsize = 60)
        info_Frame.grid_rowconfigure(0, minsize = 20)
        info_Frame.grid_rowconfigure(3, minsize = 20)
        
        logo_Frame = Frame(info_Frame, bg = '#1C1C1C')
        logo_Frame.grid(row = 1, column = 1, sticky = ('e', 'w', 'n', 's'))
        
        Label(logo_Frame, text = 'O R I O N', font = ('Courier', 25, 'bold'), bg = '#1C1C1C', fg = 'white').pack(anchor = CENTER)
        
        time_date_Frame =LabelFrame(info_Frame, text = 'Time|Date', font = ('Courier', 10, 'bold'), fg = 'white', bg = '#1C1C1C')
        time_date_Frame.grid(row = 2, column = 1, sticky = ('w', 'e'))
        
        time_date_Frame.grid_rowconfigure(0, minsize = 7)
        time_date_Frame.grid_columnconfigure(0, minsize = 30)
        time_date_Frame.grid_rowconfigure(3, minsize = 25)
        time_date_Frame.grid_columnconfigure(2, minsize = 30)
        time_date_Frame.grid_rowconfigure(6, minsize = 7)
        
        Label(time_date_Frame, text = 'DATE', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#1C1C1C').grid(row = 1, column = 1, sticky = ('w'))
        Label(time_date_Frame, text = str(date.today()), font = ('Courier', 15, 'bold'), fg = 'orange', bg = '#1C1C1C').grid(row = 2, column = 1, sticky = ('w', 'e'))
        Label(time_date_Frame, text = 'TIME', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#1C1C1C').grid(row = 4, column = 1, sticky = ('w'))
        self.timeLabel = Label(time_date_Frame, text = "00:00:00", font = ('Courier', 15, 'bold'), fg = 'orange', bg = '#1C1C1C')
        self.timeLabel.grid(row = 5, column = 1, sticky = ('w', 'e'))
        
        
        greeting_Frame = LabelFrame(info_Frame, text = 'Your Info', font = ('Courier', 10, 'bold'), fg = 'white', bg = '#1C1C1C')
        greeting_Frame.grid(row = 4, column = 1)
        
        greeting_Frame.grid_rowconfigure(0, minsize = 7)
        greeting_Frame.grid_columnconfigure(0, minsize = 30)
        greeting_Frame.grid_columnconfigure(2, minsize = 30)
        greeting_Frame.grid_rowconfigure(3, minsize = 25)
        greeting_Frame.grid_rowconfigure(6, minsize = 25)
        greeting_Frame.grid_rowconfigure(9, minsize = 7)
        
        Label(greeting_Frame, text = 'WELCOME', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#1C1C1C').grid(row = 1, column = 1, sticky = ('w'))
        
        self.greetingLabel = Label(greeting_Frame, text = "{} {}".format(self.records[0], self.records[1]), font = ('Courier', 15, 'bold'), fg = 'orange', bg = '#1C1C1C')
        self.greetingLabel.grid(row = 2, column = 1, sticky = ('w', 'n'))
        
        Label(greeting_Frame, text = 'YOUR INCOME', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#1C1C1C').grid(row = 4, column = 1, sticky = ('w'))
        self.income_Label = Label(greeting_Frame, text = f'₱{self.records[6]:,}', font = ('Courier', 15, 'bold'), fg = 'orange', bg = '#1C1C1C')
        self.income_Label.grid(row = 5, column = 1, sticky = ('w', 'n'))
        
        Label(greeting_Frame, text = 'YOUR BALANCE', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#1C1C1C').grid(row = 7, column = 1, sticky = ('w'))
        self.balance_Label = Label(greeting_Frame, text = f'₱{self.records[7]:,}', font = ('Courier', 15, 'bold'), fg = 'orange', bg = '#1C1C1C')
        self.balance_Label.grid(row = 8, column = 1, sticky = ('w', 'n'))
        
        
        
        
        
        global dashboard_Frame
        dashboard_Frame = Frame(home_window, bg = '#2F2F2F', width = 906, height = 664, bd = 5, relief = SOLID)
        dashboard_Frame.grid(row = 0, column = 1, sticky = ('n', 's'))
        
        #dashboard_Frame.grid_propagate(False)
        
        logout_Frame = Frame(dashboard_Frame, bg = "#1C1C1C")
        logout_Frame.grid(row = 0, column = 0, sticky = ('e', 'w'))
        logout_Frame.grid_columnconfigure(1, minsize = 800)
        
        Goback_button = Button(logout_Frame, text = 'Go Back', font = ('Courier', 10, 'bold'), bd = 5, relief = SOLID, background = '#4D4DFF', state = DISABLED, activebackground = 'red' , fg = 'white')
        Goback_button.grid(row = 0, column = 0, pady = 15)
        
        
        logout_button = Button(logout_Frame, text = 'Logout', font = ('Courier', 10, 'bold'), bd = 5, relief = SOLID, background = '#4D4DFF', activebackground = 'red' , fg = 'white', command = lambda:self.logout_(home_window))
        logout_button.grid(row = 0, column = 5, pady = 15)
        #logout_button.pack(pady = 15, anchor = "e", side = RIGHT)
        
        
        
        #-----Main Frame-----#
        #global main_Frame
        main_Frame = Frame(dashboard_Frame,bg = '#2F2F2F')
        main_Frame.grid(row = 1, column = 0)
        main_Frame.grid_rowconfigure(0, minsize = 10)
        main_Frame.grid_rowconfigure(2, minsize = 15)
        
        button_Frame = Frame(main_Frame,bg = '#2F2F2F')
        button_Frame.grid(row = 1, column = 0)
        
        button_Frame.grid_rowconfigure(0, minsize = 40)
        button_Frame.grid_rowconfigure(2, minsize = 40)
        button_Frame.grid_columnconfigure(0, minsize = 36)
        button_Frame.grid_columnconfigure(2, minsize = 36)
        button_Frame.grid_columnconfigure(4, minsize = 36)
        
        #-----Buttons-----#
        get_cash_Button = Button(button_Frame, text = "GET CASH", fg = 'white', font = ('Courier', 25, 'bold'), padx = 20, pady = 20, bg = 'blue', bd = 8, activebackground = '#00ff00', command = lambda: Withdraw_Income(home_window, Goback_button, main_Frame, records[3]))
        get_cash_Button.grid(row = 1, column = 1, sticky = ('e', 'w'))
        
        share_Button = Button(button_Frame, text = "DEPOSIT", fg = 'white', font = ('Courier', 25, 'bold'), padx = 20, pady = 20, bg = 'blue', bd = 8, activebackground = '#00ff00', command = lambda: ShareForm(home_window, Goback_button, main_Frame, records[3]))
        share_Button.grid(row = 1, column = 3, sticky = ('e', 'w'))
        
        account_Button = Button(button_Frame, text = "ACCOUNT", fg = 'white', font = ('Courier', 25, 'bold'), padx = 20, pady = 20, bg = 'blue', bd = 8, activebackground = '#00ff00', state = DISABLED, command = lambda:
            AccountForm(home_window, Goback_button, main_Frame, records))
        account_Button.grid(row = 3, column = 1, sticky = ('e', 'w'))
        
        other_Button = Button(button_Frame, text = "OTHER", fg = 'white', font = ('Courier', 25, 'bold'), padx = 20, pady = 20, bg = 'blue', bd = 8, activebackground = '#00ff00', state=DISABLED, command = lambda:Other_Window(home_window, Goback_button, main_Frame, records))
        other_Button.grid(row = 3, column = 3, sticky = ('e', 'w'))
        
        
        
        calendar_Frame = LabelFrame(main_Frame,bg = '#2F2F2F', text = 'C a l e n d a r', fg = 'white', font = ('Courier', 15, 'bold'))
        calendar_Frame.grid(row = 1, column = 1, sticky = ('n', 's'), padx = 6)
        
        
        #-----Displays Calendar-----#
        month_yr = [int(x) for x in str(date.today()).split('-')]
        
        calendar_Label = Calendar(calendar_Frame, selectmode = 'day', year = month_yr[0], month = month_yr[1], day = month_yr[2], font = ('Courier', 12), height = 200)
        calendar_Label.grid(sticky = ('n', 's'), pady = 5, padx = 5)
        
        #-----Treeview Frame-----#
        treeview_Frame = LabelFrame(main_Frame, bg = '#2F2F2F', text = 'Transaction History', font = ('Courier', 14, 'bold'), fg = 'white', bd = 5, relief = SUNKEN)
        treeview_Frame.grid(row = 3, column = 0, columnspan = 2, sticky = ('e', 'w'))
        
        #Scrollbar
        scrollbar = Scrollbar(treeview_Frame, orient = VERTICAL, background = '#1C1C1C')
        scrollbar.pack(side = RIGHT, fill = Y)
        
        history_Tree = ttk.Treeview(treeview_Frame, height = 5, yscrollcommand = scrollbar)
        history_Tree.pack()
        
        #Styles Treeview
        style1 = ttk.Style()
        style1.configure("Treeview", fieldbackground = '#1C1C1C')
        
        history_Tree['columns'] = ('Date', 'Time', 'History', 'Amount', 'Balance')
        
        history_Tree.column('#0', width = 70, anchor = 'w')
        history_Tree.column('Date', width = 140, anchor = CENTER)
        history_Tree.column('Time', width = 120, anchor = CENTER)
        history_Tree.column('History', width = 330, anchor = CENTER)
        history_Tree.column('Amount', width = 160, anchor = CENTER)
        history_Tree.column('Balance', width = 160, anchor = CENTER)
        
        #Styles Treeview Heading
        style = ttk.Style()
        style.configure("Treeview.Heading", font = ('Courier', 8, 'bold'), foreground = '#4D4DFF', background = '#2F2F2F')
        
        history_Tree.heading('#0', text = 'No.', anchor = CENTER)
        history_Tree.heading('Date', text = 'Date', anchor = CENTER)
        history_Tree.heading('Time', text = 'Time', anchor = CENTER)
        history_Tree.heading('History', text = 'History', anchor = CENTER)
        history_Tree.heading('Amount', text = 'Amount', anchor = CENTER)
        history_Tree.heading('Balance', text = 'Balance', anchor = CENTER)
        
        #Configure ScrollBar
        scrollbar.config(command = history_Tree.yview)
        
        #-----Tree stripe Color-----#
        history_Tree.tag_configure('odd', background = '#2F2F2F', foreground = 'white', font = ('Courier', 8, 'bold'))
        history_Tree.tag_configure('even', background = '#FFFDFA', foreground = '#2F2F2F', font = ('Courier', 8, 'bold'))
        
        
        #-----This displays user history in the table----#
        try:
            user_history = display_history(records[3])
            print(user_history)
            
            id_count = 1
            for history in user_history:
                if id_count % 2 == 0:
                    history_Tree.insert(parent = '', index = 'end', iid = id_count, text = id_count, values = (history[0], history[1], history[2], history[3], history[4]), tags = ('even',))
                
                else:
                    history_Tree.insert(parent = '', index = 'end', iid = id_count, text = id_count, values = (history[0], history[1], history[2], history[3], history[4]), tags = ('odd',))
                    
                id_count += 1
            
        except:
            pass
        
        
        
        
        #-----About Frame-----#
        about_Frame = Frame(dashboard_Frame,bg = '#1C1C1C')
        about_Frame.grid(row = 2, column = 0, sticky = ('e', 'w'))
        
        Label(about_Frame, text = 'Launced by: Orion', fg = 'white', bg = '#1C1C1C', font = ('Courier', 10, 'bold')).pack(side = RIGHT, pady = 7)
        
        #-----Refreshes Info Frame-----#
        self.update_income(self.income_Label)
        self.update_balance(self.balance_Label)
        
        #-----This initialize local time-----#
        self.initialize_time()
        
        
        home_window.resizable(False, False)
        home_window.mainloop()


    def initialize_time(self):
        """This initiates time"""
        time_format_string = strftime("%I:%M:%S %p")
        self.timeLabel.config(text = time_format_string)
        self.timeLabel.after(1000, self.initialize_time)
    
    def update_balance(self, color_label):
        """This updates color of balance label"""
        if self.records[7] < 5000:
            return color_label.config(fg = 'red')
        
        elif self.records[7] < 15000:
            return color_label.config(fg = 'orange')
            
        elif self.records[7] < 25000:
            return color_label.config(fg = "#C0C0C0")
        
        elif self.records[7] < 55000:
            return color_label.config(fg = "#FFD700")
            
        else:
            return color_label.config(fg = "#A0B2C6")
    
    def update_income(self, color_label):
        """This updates color of balance label"""
        
        if self.records[6] < 1500:
            return color_label.config(fg = 'red')
        
        elif self.records[6] < 5000:
            return color_label.config(fg = 'orange')
            
        elif self.records[6] < 10000:
            return color_label.config(fg = "#C0C0C0")
        
        elif self.records[6] < 50000:
            return color_label.config(fg = "#FFD700")
            
        else:
            return color_label.config(fg = "#A0B2C6")
        
    def logout_(self, Form = None):
        """Exits the dashboard"""
        LoginForm(Form)



class Withdraw_Income(HomeForm):
    def __init__(self, home_window, Goback_button, m_Frame, id):
        
        self.window = home_window
        """Hides Frame Area"""
        try:
            """Hides Frame Area"""
            m_Frame.grid_forget()
            m_Frame.winfo_manager() 
        
        except:
            pass
            
        #Get User Record
        [records] = search_card_details(id)
        print("Page 2")
        print(str(records[3]))
        
        
        
        main_Frame = Frame(dashboard_Frame,bg = '#2F2F2F')
        main_Frame.grid(row = 1, column = 0, sticky = ('e', 'w'))
        #main_Frame.grid_rowconfigure(0, minsize = 10)
        main_Frame.grid_columnconfigure(1, minsize = 50)
        main_Frame.grid_columnconfigure(3, minsize = 16)
        #main_Frame.grid_rowconfigure(2, minsize = 15)
        
        receipt_Frame = Frame(main_Frame, bg = 'whitesmoke', bd = 6, relief = SOLID)
        receipt_Frame.grid(row = 1, column = 0, sticky = ('w'))
        receipt_Frame.grid_rowconfigure(0, minsize = 10)
        receipt_Frame.grid_columnconfigure(0, minsize = 10)
        receipt_Frame.grid_rowconfigure(5, minsize = 10)
        receipt_Frame.grid_rowconfigure(9, minsize = 10)
        receipt_Frame.grid_rowconfigure(14, minsize = 5)
        receipt_Frame.grid_rowconfigure(16, minsize = 15)
        
        Label(receipt_Frame, text = "*******************************************************", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 1, column = 1, sticky = ('n'))
        Label(receipt_Frame, text = "O R I O N", font = ('Courier', 20, 'bold'), fg = '#2F2F2F', bg = 'whitesmoke').grid(row = 2, column = 1, sticky = ('e', 'w'))
        Label(receipt_Frame, text = "U N I B A N K. INC.", font = ('Courier', 10, 'bold'), fg = '#2F2F2F', bg = 'whitesmoke').grid(row = 3, column = 1, sticky = ('e', 'w'))
        Label(receipt_Frame, text = "*******************************************************", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 4, column = 1, sticky = ('s'))
        
        
        Label(receipt_Frame, text = f"Date: {date.today()}", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 6, column = 1, sticky = ('w'))
        self.time_update = Label(receipt_Frame, text = "Time: 00:00:00", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke')
        self.time_update.grid(row = 7, column = 1, sticky = ('w'))
        Label(receipt_Frame, text = "Location: Cagayan de Oro City", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 8, column = 1, sticky = ('w'))
        Label(receipt_Frame, text = "Transaction", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 10, column = 1, sticky = ('w'))
        Label(receipt_Frame, text = "Withdrawal Checking", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 11, column = 1, sticky = ('w'))
        Label(receipt_Frame, text = f"Account ID: ####{str(records[3])[4:6]}", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 12, column = 1, sticky = ('w'))
        
        self.amount_Label = Label(receipt_Frame, text = "Amount: ₱0.0", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke')
        self.amount_Label.grid(row = 13, column = 1, sticky = ('w'))
        self.balance_Label = Label(receipt_Frame, text = f"Balance: ₱{str(records[7])}", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke')
        self.balance_Label.grid(row = 15, column = 1, sticky = ('w'))
        Label(receipt_Frame, text = "*******************************************************", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 17, column = 1, sticky = ('n'))
        Label(receipt_Frame, text = "ENJOY THE CONVENIENCE OF 24/7 BANKING,PAY YOUR\nBILLS VIA Orion ATMS AND EARN\nORION REWARDS POINTS! VISIT ANY ORION BRANCH\nTO KNOW MORE", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 18, column = 1)
        Label(receipt_Frame, text = "*******************************************************\n", font = ('Courier', 8, 'bold'), fg = 'black', bg = 'whitesmoke').grid(row = 19, column = 1, sticky = ('n'))
        
        right_Frame = Frame(main_Frame, bg = '#2F2F2F')
        right_Frame.grid(row = 1, column = 2, sticky = ('e', 'n'))
        
        Currency_Frame = Frame(right_Frame,bg = '#2F2F2F', bd = 3)
        Currency_Frame.grid(row = 0, column = 0, sticky = ('n'))
        Currency_Frame.grid_rowconfigure(0, minsize = 10)
        Currency_Frame.grid_columnconfigure(0, minsize = 25)
        Currency_Frame.grid_columnconfigure(2, minsize = 25)
        Currency_Frame.grid_columnconfigure(4, minsize = 25)
        Currency_Frame.grid_columnconfigure(6, minsize = 25)
        
        Label(Currency_Frame, text = '0', font = ('Courier', 14, 'bold'), fg = '#f7931a', bg = '#2F2F2F').grid(row = 1, column = 1)
        Label(Currency_Frame, text = f'₱{str(records[6])}', font = ('Courier', 14, 'bold'), fg = '#f7931a', bg = '#2F2F2F').grid(row = 1, column = 3)
        self.user_balance = Label(Currency_Frame, text = f'₱{str(records[7])}', font = ('Courier', 14, 'bold'), fg = '#00ff00', bg = '#2F2F2F')
        self.user_balance.grid(row = 1, column = 5)
        
        Label(Currency_Frame, text = 'BTC', font = ('Courier', 11, 'bold'), fg = 'black', bg = '#2F2F2F').grid(row = 2, column = 1)
        Label(Currency_Frame, text = 'Income', font = ('Courier', 11, 'bold'), fg = 'black', bg = '#2F2F2F').grid(row = 2, column = 3)
        Label(Currency_Frame, text = 'Balance', font = ('Courier', 11, 'bold'), fg = 'black', bg = '#2F2F2F').grid(row = 2, column = 5)

        self.entry_code = Entry(right_Frame, bd = 8, relief = RIDGE, font = ('Courier', 23, 'bold'), fg = '#39FF14', bg = '#2F2F2F')
        self.entry_code.grid(row = 2, column = 0)
        
        button_Frame = Frame(right_Frame, bg = '#2F2F2F')
        button_Frame.grid(row = 3, column = 0, sticky = ('w', 'e'))
        
        self.button_1 = Button(button_Frame, text = '1', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("1"))
        self.button_1.grid(row = 0, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_2 = Button(button_Frame, text = '2', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("2"))
        self.button_2.grid(row = 0, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_3 = Button(button_Frame, text = '3', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("3"))
        self.button_3.grid(row = 0, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        self.button_4 = Button(button_Frame, text = '4', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("4"))
        self.button_4.grid(row = 1, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_5 = Button(button_Frame, text = '5', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("5"))
        self.button_5.grid(row = 1, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_6 = Button(button_Frame, text = '6', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("6"))
        self.button_6.grid(row = 1, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        self.button_7 = Button(button_Frame, text = '7', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("7"))
        self.button_7.grid(row = 2, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_8 = Button(button_Frame, text = '8', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("8"))
        self.button_8.grid(row = 2, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_9 = Button(button_Frame, text = '9', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("9"))
        self.button_9.grid(row = 2, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        
        self.button_dec = Button(button_Frame, text = '•', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("."))
        self.button_dec.grid(row = 4, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_0 = Button(button_Frame, text = '0', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("0"))
        self.button_0.grid(row = 4, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_00 = Button(button_Frame, text = '00', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 55, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("00"))
        self.button_00.grid(row = 4, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        command_Frame = Frame(right_Frame, bg = '#2F2F2F')
        command_Frame.grid(row = 4, column = 0, sticky = ('w', 'e'))
        
        clear_button = Button(command_Frame, bg = 'red', fg = 'whitesmoke', text = 'Clear', bd = 8, font = ('Courier', 14, 'bold'), activebackground = '#00ff00', pady = 10, padx = 60, command = self.clear)
        clear_button.grid(row = 0, column = 0, padx = 5)
        accept_button = Button(command_Frame, bg = '#1fd655', fg = 'whitesmoke', text = 'Accept', bd = 8, font = ('Courier', 14, 'bold'), activebackground = '#00ff00', pady = 10, padx = 77, command = lambda: self.submit(records[3],records[7]))
        accept_button.grid(row = 0, column = 1, padx = 5)

        Goback_button.config(state = 'normal', command = lambda: HomeForm(self.window, records))
        

    def click(self, number):
        """This clicks number buttons"""
        current = self.entry_code.get()
        self.entry_code.delete(0, END)
        self.entry_code.insert(0, str(current) + str(number))

    def clear(self):
        """This clears entry"""
        self.entry_code.delete(len(self.entry_code.get())-1, END)

    def submit(self,id, balance):
        """This submits your requested balance"""
        
        try:
            cash = float(self.entry_code.get())
            
            if cash <= 0:
                mssg.showwarning('Invalid!', 'Invalid command!')
            else:
                condition = mssg.askyesno('Cash Out?', f'Are you sure you want to withdraw ₱{str(cash)} cash?')
                if condition:
                    if cash > balance:
                        mssg.showwarning('Invalid!', 'You have not enough minerals(Starcraft reference)!')
                        
                    else:
                        balance = balance - cash
                        update_balance(id, balance)
                        self.entry_code.delete(0, END)
                        self.refresh_receipt(id, cash)
                        
                        #Adds this to fhe history
                        #Creaes a table for the user
                        create_history_table(id)
                        
                        #Inserts your recent history
                        insert_data_history(id, cash, balance)
                        #Pops up window
                        self.receipt_Screen()
        
        
        except Exception as e:
            mssg.showwarning('Invalid!', 'Invalid command!')
            pass


    def refresh_receipt(self, id, cash):
        """This refreshes receipt"""
        
        [records] = search_card_details(id)
        
        
        update_time = strftime("%I:%M:%S %p")
        self.time_update.config(text = f"Time: {update_time}")
        self.amount_Label.config(text = f"Amount: ₱{str(cash)}")
        self.balance_Label.config(text = f"Balance: ₱{str(records[7])}")
        self.user_balance.config(text = f'₱{str(records[7])}')


    def receipt_Screen(self):
        """This displays pop up screen"""
        receipt_window = Toplevel()
        receipt_window.configure(bg = "#2F2F2F")
        receipt_window.title('Your receipt!')
        
        Label(receipt_window, text = "Transactions Completed!", font = ("Courier", 18, 'bold'), fg = 'whitesmoke', bg = "#2F2F2F").pack(anchor = CENTER)
        
        
        receipt_window.resizable(False, False)
        

class ShareForm(HomeForm):
    
    def __init__(self, home_window, Goback_button, m_Frame, id):
        
        self.window = home_window
        """Hides Frame Area"""
        try:
            """Hides Frame Area"""
            m_Frame.grid_forget()
            m_Frame.winfo_manager() 
        
        except:
            pass
            
        #Get User Record
        [records] = search_card_details(id)
        print("Page 3")
        print(str(records[3]))
        
        main_Frame = Frame(dashboard_Frame,bg = '#2F2F2F')
        main_Frame.grid(row = 1, column = 0, sticky = ('e', 'w'))
        main_Frame.grid_rowconfigure(0, minsize = 10)
        main_Frame.grid_columnconfigure(0, minsize = 5)
        main_Frame.grid_columnconfigure(2, minsize = 55)
        main_Frame.grid_rowconfigure(2, minsize = 5)
        
        leftFrame = Frame(main_Frame, bg = "#2F2F2F")
        leftFrame.grid(row = 1, column = 1, sticky = ('w', 'n'))
        leftFrame.grid_rowconfigure(3, minsize = 50)
        
        search_Frame = Frame(leftFrame, bg = "#2F2F2F")
        search_Frame.grid(row = 0, column = 1, sticky = ('w'))
        
        self.search_entry = Entry(search_Frame, bd = 8, relief = RIDGE, font = ('Courier', 15, 'bold'), fg = '#39FF14', bg = '#2F2F2F')
        self.search_entry.grid(row = 2, column = 0)
        search_button = Button(search_Frame, text = "Search", font = ("Courier", 14, 'bold'), bd = 5, relief = RAISED, fg = 'whitesmoke', activebackground = '#00ff00', bg = '#1C1C1C', command = lambda: self.searching_user(id))
        search_button.grid(row = 2, column = 1, padx = 5)
        
        
        account_Frame = LabelFrame(leftFrame, bg = "#2F2F2F", text = "User Account", fg = 'white', font = ('Courier', 12, 'bold'), bd = 3)
        account_Frame.grid(row = 1, column = 1, sticky = ('w', 'e'), pady = 5)
        account_Frame.grid_columnconfigure(0, minsize = 3)
        account_Frame.grid_columnconfigure(2, minsize = 30)
        account_Frame.grid_rowconfigure(3, minsize = 15)
        account_Frame.grid_rowconfigure(6, minsize = 20)
        account_Frame.grid_rowconfigure(9, minsize = 20)
        
        
        self.first_name_Label = Label(account_Frame, text = "First Name: None", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.first_name_Label.grid(row = 1, column = 1, sticky = ('w'))
        self.last_name_Label = Label(account_Frame, text = "Last Name: None", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.last_name_Label.grid(row = 2, column = 1, sticky = ('w'))
        
        self.username_Label = Label(account_Frame, text = "Username: None@orion.com", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.username_Label.grid(row = 4, column = 1, sticky = ('w'))
        self.user_id_Label = Label(account_Frame, text = "Account ID: ######", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.user_id_Label.grid(row = 5, column = 1, sticky = ('w'))
        self.income_Label = Label(account_Frame, text = "Income: ₱0.0", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.income_Label.grid(row = 6, column = 1, sticky = ('w'))
        self.balance_Label = Label(account_Frame, text = "Balance: ₱0.0", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.balance_Label.grid(row = 7, column = 1, sticky = ('w'))
        bitcoin_Label = Label(account_Frame, text = "Bitcoin: BTC 0", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        bitcoin_Label.grid(row = 8, column = 1, sticky = ('w'))
        
        history_Frame = LabelFrame(leftFrame, text = "Recent History:", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        history_Frame.grid(row = 2, column = 1, sticky = ('w', 'e'))
        history_Frame.grid_rowconfigure(0, minsize = 7)
        history_Frame.grid_rowconfigure(2, minsize = 7)
        history_Frame.grid_columnconfigure(0, minsize = 7)
        
        self.history_Label = Label(history_Frame, text = "", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'))
        self.history_Label.grid(row = 1, column = 1, sticky = ('w'))
        
        self.progress_bar = ttk.Progressbar(leftFrame, orient = HORIZONTAL, length = 470, mode = "determinate")
        self.progress_bar.grid(row = 4, column = 1, sticky = ('w'))
        
        self.percent = StringVar()
        self.percentage = Label(leftFrame, text = "0%", fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 12, 'bold'), textvariable = self.percent)
        self.percentage.grid(row = 5, column = 1)
        self.percent.set("0%")
        
        
        right_Frame = Frame(main_Frame, bg = '#2F2F2F')
        right_Frame.grid(row = 1, column = 3, sticky = ('e', 'n'))
        
        Currency_Frame = Frame(right_Frame,bg = '#2F2F2F', bd = 3)
        Currency_Frame.grid(row = 0, column = 0, sticky = ('n'))
        Currency_Frame.grid_columnconfigure(0, minsize = 25)
        Currency_Frame.grid_columnconfigure(2, minsize = 25)
        Currency_Frame.grid_columnconfigure(4, minsize = 25)
        Currency_Frame.grid_columnconfigure(6, minsize = 25)
        
        Label(Currency_Frame, text = '0', font = ('Courier', 14, 'bold'), fg = '#f7931a', bg = '#2F2F2F').grid(row = 1, column = 1)
        Label(Currency_Frame, text = f'₱{str(records[6])}', font = ('Courier', 14, 'bold'), fg = '#f7931a', bg = '#2F2F2F').grid(row = 1, column = 3)
        self.user_balance = Label(Currency_Frame, text = f'₱{str(records[7])}', font = ('Courier', 14, 'bold'), fg = '#00ff00', bg = '#2F2F2F')
        self.user_balance.grid(row = 1, column = 5)
        
        Label(Currency_Frame, text = 'BTC', font = ('Courier', 11, 'bold'), fg = 'black', bg = '#2F2F2F').grid(row = 2, column = 1)
        Label(Currency_Frame, text = 'Income', font = ('Courier', 11, 'bold'), fg = 'black', bg = '#2F2F2F').grid(row = 2, column = 3)
        Label(Currency_Frame, text = 'Balance', font = ('Courier', 11, 'bold'), fg = 'black', bg = '#2F2F2F').grid(row = 2, column = 5)
        
        
        
        button_Frame = Frame(right_Frame, bg = '#2F2F2F')
        button_Frame.grid(row = 3, column = 0, sticky = ('e', 'w'))
        
        self.entry_code = Entry(right_Frame, bd = 8, relief = RIDGE, font = ('Courier', 23, 'bold'), fg = '#39FF14', bg = '#2F2F2F')
        self.entry_code.grid(row = 2, column = 0)
        
        self.button_1 = Button(button_Frame, text = '1', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("1"))
        self.button_1.grid(row = 0, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_2 = Button(button_Frame, text = '2', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("2"))
        self.button_2.grid(row = 0, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_3 = Button(button_Frame, text = '3', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("3"))
        self.button_3.grid(row = 0, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        self.button_4 = Button(button_Frame, text = '4', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("4"))
        self.button_4.grid(row = 1, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_5 = Button(button_Frame, text = '5', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("5"))
        self.button_5.grid(row = 1, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_6 = Button(button_Frame, text = '6', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("6"))
        self.button_6.grid(row = 1, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        self.button_7 = Button(button_Frame, text = '7', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("7"))
        self.button_7.grid(row = 2, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_8 = Button(button_Frame, text = '8', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("8"))
        self.button_8.grid(row = 2, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_9 = Button(button_Frame, text = '9', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("9"))
        self.button_9.grid(row = 2, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        
        self.button_dec = Button(button_Frame, text = '•', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("."))
        self.button_dec.grid(row = 4, column = 0, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_0 = Button(button_Frame, text = '0', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 60, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("0"))
        self.button_0.grid(row = 4, column = 1, sticky = ('e', 'w'), padx = 3, pady = 5)
        self.button_00 = Button(button_Frame, text = '00', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 15, 'bold'), bd = 8, relief = RAISED, padx = 55, pady = 10, highlightbackground = '#1C1C1C', command = lambda: self.click("00"))
        self.button_00.grid(row = 4, column = 2, sticky = ('e', 'w'), padx = 3, pady = 5)
        
        command_Frame = Frame(right_Frame, bg = '#2F2F2F')
        command_Frame.grid(row = 4, column = 0, sticky = ('w', 'e'))
        
        clear_button = Button(command_Frame, bg = 'red', fg = 'whitesmoke', text = 'Clear', bd = 8, font = ('Courier', 14, 'bold'), activebackground = '#00ff00', pady = 10, padx = 60, command = self.clear)
        clear_button.grid(row = 0, column = 0, padx = 5)
        accept_button = Button(command_Frame, bg = '#1fd655', fg = 'whitesmoke', text = 'Accept', bd = 8, font = ('Courier', 14, 'bold'), activebackground = '#00ff00', pady = 10, padx = 77, command = lambda: self.pop_up(id, records[3]))
        accept_button.grid(row = 0, column = 1, padx = 5)
        
        
        
        
        Goback_button.config(state = 'normal', command = lambda: HomeForm(self.window))

    def click(self, number):
        """This clicks number buttons"""
        current = self.entry_code.get()
        self.entry_code.delete(0, END)
        self.entry_code.insert(0, str(current) + str(number))

    def clear(self):
        """This clears entry"""
        self.entry_code.delete(len(self.entry_code.get())-1, END)

    
    def searching_user(self, duplicate_id):
        """This searches and displays user details"""
        try:
            if int(self.search_entry.get()) == duplicate_id:
                pass
                
            else:
                try:
                    [user_searched] = search_card_details(int(self.search_entry.get()))
                    
                    #Refreshes or Display Searched User
                    self.refresh_acc(user_searched)
                    
                    try:
                        user_history = display_history(user_searched[3])
                        print(user_history)
                        self.history_Label.config(text = user_history[-1][2])
                    
                    except Exception as e:
                        print(e)
                        self.history_Label.config(text = "No recent history founded...")
                
                except:
                    mssg.showwarning('Not Found!', 'The account you searched has not found!')
        except:
            mssg.showwarning('Invalid!', 'Invalid Options!')
            print(traceback.format_exc())
    
    def refresh_acc(self, user_searched):
        """This refreshes account label"""
        
        self.first_name_Label.config(text = "First Name: " + user_searched[0])
        self.last_name_Label.config(text = "Last Name: " + user_searched[1])
        self.username_Label.config(text = "Username: " + user_searched[2])
        self.user_id_Label.config(text = "Account ID: " + str(user_searched[3]))
        self.income_Label.config(text = f"Income: ₱{user_searched[6]:,}")
        self.balance_Label.config(text = f"Balance: ₱{user_searched[7]:,}")
    
    
    def pop_up(self, id, logged_id):
        """Pops up after pressing the Accept Button"""
        
        try:
            [acc_id] = search_card_details(id)
            if int(self.entry_code.get()) <= 0:
                mssg.showwarning('Invalid!', 'Invalid! Enter amount first!')
            
            if float(self.entry_code.get()) > acc_id[7]:
                mssg.showwarning('Invalid!', 'Your amount greater than your own balance!')
                
            if self.user_id_Label.cget("text").strip("Account ID: ") == "######":
                mssg.showwarning('Invalid!', 'No Account ID found...')
            
            else:
                pop_up = Toplevel()
                pop_up.title('Condition')
                
                Label(pop_up, text = "Are you sure you want to send this amount?", font = ('Courier', 16, 'bold'), fg = 'white', bg = '#2F2F2F').grid(row = 0, column = 0)
                condition_Frame = Frame(pop_up, bd = 3, bg = "#2F2F2F")
                condition_Frame.grid(row = 1, column = 0, sticky = ('w', 'e'))
                
                button_no = Button(condition_Frame, text = 'Decline', bg = 'red', bd = 7, relief = RAISED, activebackground = '#00ff00', font = ('Courier', 15, 'bold'), padx = 100, pady = 25, command = pop_up.destroy)
                button_no.grid(row = 0, column = 0, sticky = ('e', 'w'))
                
                button_yes = Button(condition_Frame, text = 'Accept', bg = '#00ff00', bd = 7, relief = RAISED, activebackground = '#00ff00', font = ('Courier', 15, 'bold'), padx = 120, pady = 25, command = lambda:[pop_up.destroy(), self.sending(logged_id)])
                button_yes.grid(row = 0, column = 1, sticky = ('e', 'w'))
                
                pop_up.resizable(False, False)
        
        except:
            mssg.showwarning('Invalid!', 'Invalid options!')
            print(traceback.format_exc())
    
    
    def sending(self, logged_id):
        """This sends the amount of user to other user"""
        print(self.entry_code.get())
        tasks = 10
        count = 0
        while(count<tasks):
            time.sleep(1)
            self.progress_bar['value'] += 10
            count += 1
            self.percent.set("Transmitting "+str(int((count/tasks)*100))+ '%')
            self.window.update_idletasks()
        
        #Sharing User amount
        acc_id = int(self.user_id_Label.cget("text").strip("Account ID: "))
        
        #Current User id
        [current] = search_card_details(logged_id)
        balance = current[7] - int(self.entry_code.get())
        #Updates User Balance
        update_balance(current[3], balance)
        
        #Checks if user already exists
        create_history_table(current[3])
        
        #Update Database Table History
        share_data_history(current[3], float(self.entry_code.get()), float(balance))
        
        [acc_id] = search_card_details(int(acc_id))
        balance = acc_id[7] + float(self.entry_code.get())
        #Updates User Balance
        update_balance(acc_id[3], balance)
        
        #Checks if user already exists
        create_history_table(acc_id[3])
        
        #Updates User Databadse Table History
        claim_data_history(acc_id[3], float(self.entry_code.get()), float(balance))
        
        #Refreshes Screen
        self.refresh_screen(current[3], acc_id[3])
        
        self.percent.set("Transmission Sent 100%")
        time.sleep(2)
        self.progress_bar['value'] = 0
        self.percent.set("0%")
            

    def refresh_screen(self, sender, receiver):
        """This refreshes screen after sending amount"""
        
        [sender_searched], [receiver_searched] = search_card_details(sender), search_card_details(receiver)
 
        
        #Sender Details
        self.user_balance.config(text = f'₱{str(sender_searched[7])}')
        
        #Receiver Details
        self.balance_Label.config(text = f"Balance: ₱{receiver_searched[7]:,}")
        
        user_history = display_history(receiver_searched[3])
        #Update History
        self.history_Label.config(text = user_history[-1][2])


class AccountForm(HomeForm):
    def __init__(self, home_window, Goback_button, m_Frame):
        
        self.window = home_window
        """Hides Frame Area"""
        try:
            """Hides Frame Area"""
            m_Frame.grid_forget()
            m_Frame.winfo_manager() 
        
        except:
            pass
            
        main_Frame = Frame(dashboard_Frame,bg = '#2F2F2F')
        main_Frame.grid(row = 1, column = 0)
        main_Frame.grid_rowconfigure(0, minsize = 10)
        main_Frame.grid_rowconfigure(2, minsize = 15)


        Goback_button.config(state = 'normal', command = lambda: HomeForm(self.window))




class Other_Window(HomeForm):
    def __init__(self, home_window, Goback_button, m_Frame):
        
        self.window = home_window
        """Hides Frame Area"""
        try:
            """Hides Frame Area"""
            m_Frame.grid_forget()
            m_Frame.winfo_manager() 
        
        except:
            pass
            
        main_Frame = Frame(dashboard_Frame,bg = '#2F2F2F')
        main_Frame.grid(row = 1, column = 0)
        main_Frame.grid_rowconfigure(0, minsize = 10)
        main_Frame.grid_rowconfigure(2, minsize = 15)


        Goback_button.config(state = 'normal', command = lambda: HomeForm(self.window))





class LoginForm:
    def __init__(self, Form = None):
        
        try:
            Form.destroy()
        
        except:
            pass
        
        window = Tk()
        window.title('Login')
        window.configure(relief = SOLID, bd = 7)
        
        leftFrame = Frame(window, bg = '#1C1C1C', width = 300, height = 100)
        leftFrame.grid(row = 0, column = 0, sticky = ('n', 's'))
        
        orion = Image.open("img/orion.png").resize((665, 647), Image.ANTIALIAS)

        orion_logo = ImageTk.PhotoImage(orion)

        Label(leftFrame, image = orion_logo).grid(sticky = ('n', 's'), row = 0, column= 0)
        
        #-----Right Frame-----#
        
        rightFrame = Frame(window, bg = '#2F2F2F', width = 500, height = 100)
        rightFrame.grid(row = 0, column = 1, sticky = ('n', 's'))
        
        greetingFrame = Frame(rightFrame, bg = '#1C1C1C')
        greetingFrame.grid(row = 0, column = 0, sticky = ('e', 'w'))
        
        Label(greetingFrame, text = 'W e l c o m e  T o  T h e  O r i o n', font = ('Courier', 18, 'bold'), fg = 'white', bg = '#1C1C1C').pack(anchor = CENTER, pady = 25, padx = 20)
        
        entry_Frame = Frame(rightFrame, bg = '#2F2F2F')
        entry_Frame.grid(row = 1, column = 0)
        
        entry_Frame.grid_rowconfigure(0, minsize=22)
        entry_Frame.grid_rowconfigure(3, minsize=15)
        entry_Frame.grid_rowconfigure(6, minsize=22)
        #entry_Frame.grid_columnconfigure(0, minsize=70)
        
        #entry_Frame.grid_columnconfigure(1, minsize=50)
        
        Label(entry_Frame, text = 'Account ID', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#2F2F2F'). grid(row = 1, column = 1, sticky = ('s', 'w'))
        
        self.acc_entry = customtkinter.CTkEntry(entry_Frame, placeholder_text = 'Enter Account ID', height = 55, text_font = ('Courier', 15, 'bold'), width = 450, fg_color = '#1C1C1C')
        self.acc_entry.grid(row = 2, column = 1, sticky = ('w', 'n'))
        
        Label(entry_Frame, text = 'Password 4-digit', font = ('Courier', 15, 'bold'), fg = 'white', bg = '#2F2F2F').grid(row = 4, column = 1, sticky = ('s', 'w'))
        self.pass_entry = customtkinter.CTkEntry(entry_Frame, placeholder_text = 'Enter Password', height = 55, text_font = ('Courier', 15, 'bold'), width = 450, show = '*', fg_color = '#1C1C1C')
        self.pass_entry.grid(row = 5, column = 1, sticky = ('w', 'n'))
        
        #-----Command Frame-----#
        
        command_Frame = LabelFrame(rightFrame, bg = '#2F2F2F', text = 'C o m m a n d', font = ('Courier', 10, 'bold'), fg = 'white')
        command_Frame.grid(row = 2, column = 0, sticky = ('e', 'w'))
        
        
        
        switch_Frame = Frame(command_Frame, bg = '#2F2F2F')
        switch_Frame.grid(row = 0, column = 0, sticky = ('n', 's'))
        
        self.Enter_acc_button = Button(switch_Frame, text = 'Enter Account ID', font = ('Courier', 10, 'bold'), bd = 3, padx = 10, pady = 18, activebackground='#00ff00', activeforeground = 'white', bg = '#4D4DFF', fg = 'white', command = lambda: self.switch_button('acc_entry'))
        self.Enter_acc_button.grid(row = 0, column = 0, sticky = ('e', 'w'), padx = 5)
        
        
        self.Enter_pass_button = Button(switch_Frame, text = 'Enter Password', font = ('Courier', 10, 'bold'), bd = 3, padx = 10, pady = 18, activebackground='#00ff00', activeforeground = 'white', bg = '#4D4DFF', fg = 'white', command = lambda: self.switch_button('pass_entry'))
        self.Enter_pass_button.grid(row = 1, column = 0, sticky = ('e', 'w'), padx = 5, pady = 7)
        
        login_button = Button(switch_Frame, text = 'L O G I N', font = ('Courier', 15, 'bold'), bd = 3, padx = 10, pady = 25, activebackground='#00ff00', activeforeground = 'white', bg = '#1C1C1C', fg = 'white', command = lambda: self.login_to_home(window))
        login_button.grid(row = 2, column = 0, sticky = ('e', 'w'), padx = 5)
        
        
        
        #-----Button Frame-----#
        
        button_Frame = Frame(command_Frame, bg = '#2F2F2F')
        button_Frame.grid(row = 0, column = 1, sticky = ('n','e', 'w'), padx = 5)
        
        self.button1 = Button(button_Frame, text = '1', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 20, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button1.grid(row = 0, column = 0, sticky = ('e', 'w'), padx = 3)
        self.button2 = Button(button_Frame, text = '2', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 23, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button2.grid(row = 0, column = 1, sticky = ('e', 'w'), padx = 3)
        self.button3 = Button(button_Frame, text = '3', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button3.grid(row = 0, column = 2, sticky = ('e', 'w'), padx = 3)
        
        
        self.button4 = Button(button_Frame, text = '4', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button4.grid(row = 1, column = 0, sticky = ('e', 'w'), padx = 3, pady = 3)
        self.button5 = Button(button_Frame, text = '5', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button5.grid(row = 1, column = 1, sticky = ('e', 'w'), padx = 3, pady = 3)
        self.button6 = Button(button_Frame, text = '6', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button6.grid(row = 1, column = 2, sticky = ('e', 'w'), padx = 3, pady = 3)
        
        self.button7 = Button(button_Frame, text = '7', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button7.grid(row = 2, column = 0, sticky = ('e', 'w'), padx = 3)
        self.button8 = Button(button_Frame, text = '8', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button8.grid(row = 2, column = 1, sticky = ('e', 'w'), padx = 3)
        self.button9 = Button(button_Frame, text = '9', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button9.grid(row = 2, column = 2, sticky = ('e', 'w'), padx = 3)
        
        self.clear_button = Button(button_Frame, text = '⌫', bg = 'red', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.clear_button.grid(row = 3, column = 0, sticky = ('e', 'w'), padx = 3, pady = 3)
        self.button0 = Button(button_Frame, text = '0', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button0.grid(row = 3, column = 1, sticky = ('e', 'w'), padx = 3, pady = 3)
        self.button_00 = Button(button_Frame, text = '00', bg = '#1C1C1C', fg = 'white', activebackground = '#00ff00', font = ('Courier', 13, 'bold'), bd = 8, relief = RAISED, padx = 17, pady = 5, highlightbackground = '#1C1C1C', command = None)
        self.button_00.grid(row = 3, column = 2, sticky = ('e', 'w'), padx = 3, pady = 3)
        
        
        #Insert Card Pic Image
        pic_frame = Frame(command_Frame, bg = '#2F2F2F')
        pic_frame.grid(row = 0, column = 2, sticky = 'n')
        
        insert_card_pic = Image.open("img/card_slot.jpg").resize((250, 170), Image.ANTIALIAS)

        insert_card = ImageTk.PhotoImage(insert_card_pic)
        
        
        
        Label(pic_frame, text = 'Insert Card Here', font = ('Courier', 10, 'bold'), bg = '#2F2F2D', fg = 'white').grid(row = 0, column = 0, sticky = 'n')
        Label(pic_frame, text = '↓↓↓', font = ('Courier', 10, 'bold'), bg = '#2F2F2D', fg = 'white').grid(row = 1, column = 0, sticky = 's')
        self.pic_Label = Label(pic_frame, image = insert_card, bd = 3, bg = '#2F2F2F')
        self.pic_Label.grid(row = 2, column = 0, sticky = ('e', 'n', 's'))
        
        
        footer_Frame = Frame(rightFrame, bg = '#1C1C1C')
        footer_Frame.grid(row = 3, column= 0, sticky = ('e', 'w', 's'))
        
        Label(footer_Frame, text = 'Launched By: Orion', font = ('Courier', 10, 'bold'), bg = '#1C1C1C', fg = 'white').pack(side = RIGHT, padx = 10, pady = 10)
        
        
        #Blink Effect
        self.blink_blue()
        #Default Button
        self.switch_button('acc_entry')
        
        
        
        window.resizable(False, False)
        window.mainloop()
        
    def login_to_home(self, Form):
        """This checks if the account exist and login"""
        try:
            [records] = search_card_details(int(self.acc_entry.get()))
            try:
                if int(self.pass_entry.get()) == records[5]:
                    #Login to user account
                    HomeForm(Form, records)
                
                else:
                    mssg.showwarning('Invalid!', 'Invalid Password!')
            except Exception as e:
                print(e)
                mssg.showwarning('Invalid!', 'Invalid Password!')
        except:
            mssg.showwarning('Not Found.', 'Sorry not found!')
        
    
    def click(self, path, number = None):
        """This will display number in entry"""
        
        if path == "acc_entry":
            current = self.acc_entry.get()
            self.acc_entry.delete(0, END)
            self.acc_entry.insert(0, str(current) + str(number))
        
        else:
            current = self.pass_entry.get()
            self.pass_entry.delete(0, END)
            self.pass_entry.insert(0, str(current) + str(number))
            
    def clear(self, path):
        """This clears entry"""
        
        if path == "acc_entry":
            self.acc_entry.delete(len(self.acc_entry.get())-1, END)
            
        else:
            self.pass_entry.delete(len(self.pass_entry.get())-1, END)
        
    
    def switch_button(self, path):
        """Switches button entry or pass"""
        
        if path == "acc_entry":
            self.Enter_acc_button.config(state = DISABLED)
            self.Enter_pass_button.config(state = 'normal')
            self.button1.config(command = lambda: self.click("acc_entry", '1'))
            self.button2.config(command = lambda: self.click("acc_entry", '2'))
            self.button3.config(command = lambda: self.click("acc_entry", '3'))
            self.button4.config(command = lambda: self.click("acc_entry", '4'))
            self.button5.config(command = lambda: self.click("acc_entry", '5'))
            self.button6.config(command = lambda: self.click("acc_entry", '6'))
            self.button7.config(command = lambda: self.click("acc_entry", '7'))
            self.button8.config(command = lambda: self.click("acc_entry", '8'))
            self.button9.config(command = lambda: self.click("acc_entry", '9'))
            self.button0.config(command = lambda: self.click("acc_entry", '0'))
            self.button_00.config(command = lambda: self.click("acc_entry", '0'))
            
            self.clear_button.config(command = lambda: self.clear("acc_entry"))
            
        
        else:
            self.Enter_pass_button.config(state = DISABLED)
            self.Enter_acc_button.config(state = 'normal')
            self.button1.config(command = lambda: self.click("pass_entry", '1'))
            self.button1.config(command = lambda: self.click("pass_entry", '1'))
            self.button2.config(command = lambda: self.click("pass_entry", '2'))
            self.button3.config(command = lambda: self.click("pass_entry", '3'))
            self.button4.config(command = lambda: self.click("pass_entry", '4'))
            self.button5.config(command = lambda: self.click("pass_entry", '5'))
            self.button6.config(command = lambda: self.click("pass_entry", '6'))
            self.button7.config(command = lambda: self.click("pass_entry", '7'))
            self.button8.config(command = lambda: self.click("pass_entry", '8'))
            self.button9.config(command = lambda: self.click("pass_entry", '9'))
            self.button0.config(command = lambda: self.click("pass_entry", '0'))
            self.button_00.config(command = lambda: self.click("pass_entry", '0'))
            
            self.clear_button.config(command = lambda: self.clear("pass_entry"))
            
    
    
    def blink_blue(self):
        """Blinks Blue"""
        
        self.pic_Label.config(bg = '#04d9ff')
        self.pic_Label.after(1500, self.blink_green)
        
    
    def blink_green(self):
        """Blinks Green"""
        self.pic_Label.config(bg = '#00ff00')
        self.pic_Label.after(1500, self.blink_blue)
        
        







if __name__ == '__main__':
    LoginForm()
    #HomeForm()


















