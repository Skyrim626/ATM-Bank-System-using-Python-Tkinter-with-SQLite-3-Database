from tkinter import*
from tkinter import ttk
from tkinter import messagebox as mssg
from time import strftime
from PIL import ImageTk, Image

import tkinter.font as tkFont
import customtkinter

from cardHolder_Database import check_card_number_info as all_cards, search_card_details as searched_record, delete_card_holder as delete_card, update_balance


from registration_machine import CardHolder



def commit_paycheck():
    """Bayaran ang mga customer babyyyy!!!"""
    
    condition = mssg.askyesno('Paycheck?', 'Is it paycheck already?')
    
    if condition:
        records = all_cards()
        
        for record in records:
            balance = record[6] + record[7]
            update_balance(record[3], balance)
        
        #Refreshes Treeview
        display_all_records()




def display_all_records():
    
    """This displays all card holder records"""
    try:
        #Clears Treeview
        for record in card_tree.get_children():
            card_tree.delete(record)
        
        accounts = all_cards()
    
        id_count = 1
        for account in accounts:
            if id_count % 2 == 0:
                card_tree.insert(parent = '', index = 'end', iid = id_count, text = id_count, values = (account[0], account[1], account[2], account[3], account[4], account[5], '₱'+str(account[6]), '₱'+str(account[7])), tags = ('even',))
            
            else:
                card_tree.insert(parent = '', index = 'end', iid = id_count, text = id_count, values = (account[0], account[1], account[2], account[3], account[4], account[5], '₱'+str(account[6]), '₱'+str(account[7])), tags = ('odd',))
                
            id_count += 1
        
        
        #Clears all entries
        clear_all_entries()
    
    except Exception as Z:
        print(Z)
        pass




def logout():
    """This exits the Management System"""
    x = mssg.askyesno('Quit Management System?', 'Do you wish to exit this program?')
    if x:
        window.destroy()


def display_time():
    """This displays Time"""
    time_format_string = strftime("%I:%M:%S %p")
    time_label.config(text = f"Time: {time_format_string}")
    time_label.after(1000, display_time)




def create_card():
    """This creates a user card"""
    
    #Initialize User details
    register = CardHolder(f_name_entry.get(), l_name_entry.get(), username_entry.get(), zip_code_entry.get(), acc_num_entry.get(), password_entry.get(), income_entry.get())
    
    #Returns True/False and message box
    condition, message = register.create_Card('create_card')
    
    if not condition:
        mssg.showwarning('Invalid Details', str(message))
    
    else:
        #Clears all entries
        clear_all_entries()
        mssg.showinfo('Success!', str(message))
        #Refreshes Treeview Records
        display_all_records()


def update_record():
    """This updates the card of the user"""
    
    #Initialize User details
    register = CardHolder(f_name_entry.get(), l_name_entry.get(), username_entry.get(), zip_code_entry.get(), acc_num_entry.get(), password_entry.get(), income_entry.get())
    
    #Returns True/False and message box
    condition, message = register.update_user_card()
    
    if not condition:
        mssg.showwarning('Invalid Details', str(message))
    
    else:
        #Clears all entries
        clear_all_entries()
        mssg.showinfo('Success!', str(message))
        #Refreshes Treeview Records
        display_all_records()



def select_record(e):
    """This selectes a record"""
    try:
        #Toggles the entry to edited
        create_button.config(state = DISABLED)
        
        #Clears all entries
        clear_all_entries()
        balance_entry.config(state = 'normal')
        selected = card_tree.focus()
        values = card_tree.item(selected, 'values')
        
        f_name_entry.insert(0, values[0])
        l_name_entry.insert(0, values[1])
        username_entry.insert(0, values[2].replace('@orion.com', ''))
        zip_code_entry.insert(0, values[4])
        acc_num_entry.insert(0, values[3])
        password_entry.insert(0, values[5])
        income_entry.insert(0, values[6].strip('₱'))
        balance_entry.insert(0, values[7].strip('₱'))
        
        #Toggles the entry to edited
        #balance_entry.config(state = DISABLED)
        
        #Toggles the entry to edited
        create_button.config(state = DISABLED)
        balance_entry.config(state = DISABLED)
    
    except:
        pass
    
    

def clear_all_entries():
    
    #Toggles the entry to edited
    create_button.config(state = 'normal')
    balance_entry.config(state = 'normal')
    
    """This clears all entries"""
    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    username_entry.delete(0, END)
    zip_code_entry.delete(0, END)
    acc_num_entry.delete(0, END)
    password_entry.delete(0, END)
    income_entry.delete(0, END)
    balance_entry.delete(0, END)
    
    balance_entry.config(state = DISABLED)




"""Calculator Frame Functions"""

def click(number):
    """Inserts number in the entries"""
    current = search_entry.get()
    search_entry.delete(0, END)
    search_entry.insert(0, str(current) + str(number))


def clear_digit():
    """This clears digits in search entry"""
    search_entry.delete(len(search_entry.get())-1, END)


def search_record():
    """This displays the searched Account ID"""
    
    try:
        accounts = searched_record(int(search_entry.get()))
        
        #Clears Treeview
        for record in card_tree.get_children():
            card_tree.delete(record)
        
        id_count = 1
        for account in accounts:
            card_tree.insert(parent = '', index = 'end', iid = id_count, text = id_count, values = (account[0], account[1], account[2], account[3], account[4], account[5], '₱'+str(account[6]), '₱'+str(account[7])), tags = ('even',))

    except:
        mssg.showwarning('Invalid!', 'Entry must be numbers')



def delete_account():
    """Deletes the account of a card holder permanently"""
    
    try:
    
        selected = card_tree.selection()
        card_tree.delete(selected)
        
        delete_card(int(acc_num_entry.get()))
        
        #Refreshes Treeview Records
        display_all_records()
        #Clears Entries
        clear_all_entries()
    
    except Exception as Z:
        print(Z)
        mssg.showwarning('Invalid!', 'Make sure the id is a number')




window = Tk()
window.title('Card Management System')
window.configure(bg = '#2F2F2F')

window.grid_rowconfigure(1, minsize = 20)


Big_Font = tkFont.Font(family = 'Courier', size = 19, weight = 'bold')


#topFrame = Frame(window)
#topFrame.grid(row = 0, column = 0)

TitleFrame = Frame(window, bd = 8, width = 1340, height = 100, bg = '#1C1C1C')
TitleFrame.grid(row = 0, column = 0, sticky = ('e', 'w'))

time_label = Label(TitleFrame, text = "Time: 00:00:00", font = ('Courier',15, 'bold'), fg = 'white', bg = '#1C1C1C')
time_label.pack(padx = 10, pady = 7, side = LEFT)

titlelabel = Label(TitleFrame, text = ' C a r d   H o l d e r  M a n a g e m e n t', font = Big_Font, fg = 'white', bg = '#1C1C1C')
titlelabel.pack(padx = 10, pady = 7, anchor = CENTER, side = LEFT)

logout_button = Button(TitleFrame, text = 'Logout', font = ('Courier', 10, 'bold'), bd = 5, relief = SOLID, background = '#4D4DFF', activebackground = 'red' , fg = 'white', command = logout)
logout_button.pack(anchor = "e", side = RIGHT)

mainFrame = Frame(window, width = 1120, height = 120, bg = '#2F2F2F')
mainFrame.grid(row = 2, sticky = ('e', 'w'))


#-----Treeview-----#
treeview_frame =  LabelFrame(mainFrame, bg = '#2F2F2F', relief = RIDGE, text = "Account Treeview", font = ('Courier', 12, 'bold'), fg = 'whitesmoke', bd = 5)
treeview_frame.grid(row = 0, column = 0, sticky = ('e', 'w'))

#Scrollbar
scrollbar = Scrollbar(treeview_frame, orient = VERTICAL, background = 'green')
scrollbar.pack(side = RIGHT, fill = Y)


card_tree = ttk.Treeview(treeview_frame, yscrollcommand = scrollbar)

style = ttk.Style()
style.configure("Treeview.Heading", font = ('Courier', 8, 'bold'), foreground = '#4D4DFF', background = '#2F2F2F')

#style.theme_use('clam')


style1 = ttk.Style()
style1.configure("Treeview", fieldbackground = '#1C1C1C')

card_tree['columns'] = ('First name', 'Last name', 'Username', 'Account Number', 'Password', 'Zip Code', 'Income', 'Balance')

card_tree.column('#0', width= 60, anchor = 'w')
card_tree.column('First name', width= 180, anchor = CENTER)
card_tree.column('Last name', width= 180, anchor = CENTER)
card_tree.column('Username', width= 180, anchor = CENTER)
card_tree.column('Account Number', width= 190, anchor = CENTER)
card_tree.column('Zip Code', width= 160, anchor = CENTER)
card_tree.column('Password', width= 120, anchor = CENTER)
card_tree.column('Income', width= 170, anchor = CENTER)
card_tree.column('Balance', width= 170, anchor = CENTER)

card_tree.heading('#0', text = 'ID', anchor = CENTER)
card_tree.heading('First name', text = 'First name', anchor = CENTER)
card_tree.heading('Last name', text = 'Last name', anchor = CENTER)
card_tree.heading('Username', text = 'Username', anchor = CENTER)
card_tree.heading('Account Number', text = 'Account Number', anchor = CENTER)
card_tree.heading('Zip Code', text = 'Password', anchor = CENTER)
card_tree.heading('Password', text = 'Zip Code', anchor = CENTER)
card_tree.heading('Income', text = 'Income', anchor = CENTER)
card_tree.heading('Balance', text = 'Balance', anchor = CENTER)

#Configure ScrollBar
scrollbar.config(command = card_tree.yview)

#-----Tree stripe Color-----#
card_tree.tag_configure('odd', background = '#2F2F2F', foreground = 'white', font = ('Courier', 8, 'bold'))
card_tree.tag_configure('even', background = '#FFFDFA', foreground = '#2F2F2F', font = ('Courier', 8, 'bold'))

card_tree.bind("<ButtonRelease-1>", select_record)
card_tree.pack()



boxFrame = Frame(window, bg = '#2F2F2F')
boxFrame.grid(row = 3, column = 0, sticky = ('w', 'n'))

system_Frame = Frame(boxFrame, bg = '#2F2F2F')
system_Frame.grid(row = 0, column = 0, sticky = ('w', 'n'))

system_Frame.grid_rowconfigure(0, minsize = 20)
system_Frame.grid_rowconfigure(2, minsize = 20)

#-----Left Frame-----##57595D
record_Frame = LabelFrame(system_Frame, fg = 'whitesmoke', bg = '#2F2F2F', font = ('Courier', 13, 'bold'), bd = 5, text = 'Records')
record_Frame.grid(row = 1, column = 0, sticky = ('w', 'n'), padx = 5)

left_Frame = customtkinter.CTkFrame(record_Frame, fg_color = '#1C1C1C', width = 20, height = 20)
left_Frame.grid(row = 0, column = 0, sticky = ('w', 'n'))

left_Frame.grid_columnconfigure(0, minsize = 40)
left_Frame.grid_columnconfigure(1, minsize = 40)

left_Frame.grid_columnconfigure(7, minsize = 30)
left_Frame.grid_columnconfigure(8, minsize = 30)
left_Frame.grid_columnconfigure(9, minsize = 30)

left_Frame.grid_rowconfigure(0, minsize = 5)
left_Frame.grid_rowconfigure(4, minsize = 5)

Label(left_Frame, text = 'First name:', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 1, column = 1, pady = 10, padx = 2)
Label(left_Frame, text = 'Last name:', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 2, column = 1, pady = 10, padx = 2)
Label(left_Frame, text = 'Username:', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 1, column = 3, pady = 10, padx = 2)
Label(left_Frame, text = 'Acc number(6-digits):', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 2, column = 3, pady = 10, padx = 2)
Label(left_Frame, text = 'Password(4-digits):', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 3, column = 3, pady = 10, padx = 2)
Label(left_Frame, text = 'Zip Code(4-10-digits):', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 1, column = 5, pady = 10, padx = 2)
Label(left_Frame, text = 'Income:', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 2, column = 5, pady = 10, padx = 2)
Label(left_Frame, text = 'Balance:', bg = '#1C1C1C', font = ('Arial', 10, 'bold'), fg = 'white').grid(row = 3, column = 5, pady = 10, padx = 2)

f_name_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'))
f_name_entry.grid(row = 1, column = 2, padx = 5, pady = 10)

l_name_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'))
l_name_entry.grid(row = 2, column = 2, padx = 5, pady = 10)

username_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'), fg_color=("gray75", "gray30"))
username_entry.grid(row = 1, column = 4, padx = 5, pady = 10)

acc_num_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'), fg_color=("gray75", "gray30"))
acc_num_entry.grid(row = 2, column = 4, padx = 5, pady = 10)

password_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'), fg_color=("gray75", "gray30"))
password_entry.grid(row = 3, column = 4, padx = 5, pady = 10)

zip_code_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'), fg_color=("gray75", "gray30"))
zip_code_entry.grid(row = 1, column = 6, padx = 5, pady = 10)

income_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'), fg_color=("gray75", "gray30"))
income_entry.grid(row = 2, column = 6, padx = 5, pady = 10)

balance_entry = customtkinter.CTkEntry(left_Frame, width = 170, text_font = ('Courier', 10, 'bold'), fg_color=("gray75", "gray30"), state = DISABLED)
balance_entry.grid(row = 3, column = 6, padx = 5, pady = 10)




right_Frame = Frame(boxFrame, bg = '#2F2F2F', width = 60, height = 50, bd = 8)
right_Frame.grid(row = 0, column = 1, sticky = ('w', 'n', 'e'), padx = 10)

right_Frame.grid_rowconfigure(0, minsize = 30)

search_entry = customtkinter.CTkEntry(right_Frame, placeholder_text = "Search Account ID", width = 250, text_font = ('Courier', 13, 'bold'), height = 50)
search_entry.grid(row = 1, column = 0, sticky = ('w', 'e', 'n'))

calculator_Frame = Frame(right_Frame, bg = '#2F2F2F')
calculator_Frame.grid(row = 2, column = 0, sticky = ('w'))

button_1 = Button(calculator_Frame, text = '1', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('1'))
button_1.grid(row = 0, column = 0, sticky = ('e', 'w'), pady = 7, padx = 5)

button_2 = Button(calculator_Frame, text = '2', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('2'))
button_2.grid(row = 0, column = 1, sticky = ('e', 'w'), pady = 7, padx = 5)

button_3 = Button(calculator_Frame, text = '3', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('3'))
button_3.grid(row = 0, column = 2, sticky = ('e', 'w'), pady = 7, padx = 5)

button_4 = Button(calculator_Frame, text = '4', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('4'))
button_4.grid(row = 1, column = 0, sticky = ('e', 'w'), pady = 7, padx = 5)

button_5 = Button(calculator_Frame, text = '5', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('5'))
button_5.grid(row = 1, column = 1, sticky = ('e', 'w'), pady = 7, padx = 5)

button_6 = Button(calculator_Frame, text = '6', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('6'))
button_6.grid(row = 1, column = 2, sticky = ('e', 'w'), pady = 7, padx = 5)

button_7 = Button(calculator_Frame, text = '7', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('7'))
button_7.grid(row = 2, column = 0, sticky = ('e', 'w'), pady = 7, padx = 5)

button_8 = Button(calculator_Frame, text = '8', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('8'))
button_8.grid(row = 2, column = 1, sticky = ('e', 'w'), pady = 7, padx = 5)

button_9 = Button(calculator_Frame, text = '9', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('9'))
button_9.grid(row = 2, column = 2, sticky = ('e', 'w'), pady = 7, padx = 5)

button_ant = Button(calculator_Frame, text = '⌫', background = 'red', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = clear_digit)
button_ant.grid(row = 3, column = 0, sticky = ('e', 'w'), pady = 7, padx = 5)

button_0 = Button(calculator_Frame, text = '0', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('0'))
button_0.grid(row = 3, column = 1, sticky = ('e', 'w'), pady = 7, padx = 5)

button_00 = Button(calculator_Frame, text = '00', background = '#2F2F2F', fg = 'white', font = ('Arial', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = lambda: click('00'))
button_00.grid(row = 3, column = 2, sticky = ('e', 'w'), pady = 7, padx = 5)

search_button = Button(calculator_Frame, text = 'Search', background = '#009dff', fg = 'white', font = ('Courier', 10, 'bold'), bd = 8, relief = RAISED, activebackground = '#15F4EE', padx = 20, pady = 5, command = search_record)
search_button.grid(row = 4, columnspan = 3, sticky = ('e', 'w'), pady = 7, padx = 5)

#-----Logo Frame-----#
logo_Frame = Frame(system_Frame, bg = "#2F2F2F")
logo_Frame.grid(row = 3,column = 0, sticky = ('s', 'w'))

orion = Image.open("img/orion.png").resize((450, 230), Image.ANTIALIAS)

orion_logo = ImageTk.PhotoImage(orion)

Label(logo_Frame, image = orion_logo).grid(sticky = ('n'), row = 0, column= 0)


"""button_Frame.grid_columnconfigure(0, minsize = 15)
button_Frame.grid_columnconfigure(2, minsize = 30)
button_Frame.grid_columnconfigure(4, minsize = 30)
button_Frame.grid_columnconfigure(6, minsize = 30)
button_Frame.grid_rowconfigure(0, minsize = 20)"""

button_Frame =  LabelFrame(system_Frame, bg = "#2F2F2F", text = 'Commands', fg = 'whitesmoke', font = ('Courier', 13, 'bold'), bd = 5)
button_Frame.grid(row = 3,column = 0, sticky = ('e', 'n'), padx = 5)

button_Frame.grid_columnconfigure(0, minsize = 20)
button_Frame.grid_columnconfigure(1, minsize = 20)
button_Frame.grid_columnconfigure(2, minsize = 20)
button_Frame.grid_columnconfigure(4, minsize = 20)
button_Frame.grid_columnconfigure(6, minsize = 20)

button_Frame.grid_rowconfigure(1, minsize = 15)
button_Frame.grid_rowconfigure(3, minsize = 15)
button_Frame.grid_rowconfigure(5, minsize = 15)


create_button = Button(button_Frame, text = 'Create⎀', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 5, command = create_card)
create_button.grid(row = 0, column = 1, sticky = ('e', 'w', 'n', 's'))

update_button = Button(button_Frame, text = 'Update✲', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6, command = update_record)
update_button.grid(row = 0, column = 3, sticky = ('e', 'w', 'n', 's'))

move_up_button = Button(button_Frame, text = 'Move Up↑', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6)
move_up_button.grid(row = 0, column = 5, sticky = ('e', 'w', 'n', 's'))

refresh_button = Button(button_Frame, text = 'Refresh⎈', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6, command = display_all_records)
refresh_button.grid(row = 2, column = 1, sticky = ('e', 'w', 'n', 's'))

delete_button = Button(button_Frame, text = 'Delete⌘', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6, command = delete_account)
delete_button.grid(row = 2, column = 3, sticky = ('e', 'w', 'n', 's'))

move_down_button = Button(button_Frame, text = 'Move Down↓', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6)

move_down_button.grid(row = 2, column = 5, sticky = ('e', 'w', 'n', 's'))

clear_button_command = Button(button_Frame, text = 'Clear Entries', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6, command = clear_all_entries)
clear_button_command.grid(row = 4, column = 1, sticky = ('e', 'w', 'n', 's'))

receipt_button = Button(button_Frame, text = 'Receipt', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6)
receipt_button.grid(row = 4, column = 3, sticky = ('e', 'w', 'n', 's'))

paycheck_button = Button(button_Frame, text = 'Paycheck', font = ('Courier', 13, 'bold'), fg = 'white', bg = '#1C1C1C', bd = 6, command = commit_paycheck)
paycheck_button.grid(row = 4, column = 5, sticky = ('e', 'w', 'n', 's'))

bottomFrame =Frame(window, width = 1120, height = 120, bg = '#1C1C1C')
bottomFrame.grid(row = 4, column = 0, sticky = ('n', 'e', 'w', 's'))



Label(bottomFrame, text = "Launched by: Orion", font = ('Courier', 10, 'bold'), fg = "white", bg = "#1C1C1C").pack(side = RIGHT, pady = 7, padx = 7)

#-----Time display-----#
display_time()

#-----Display all records-----#
display_all_records()




window.resizable(False, False)
window.mainloop()