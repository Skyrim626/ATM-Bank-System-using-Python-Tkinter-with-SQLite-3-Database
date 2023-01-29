from cardHolder_Database import search_card_details

id = 746902
password = 6410


try:
    [records] = search_card_details(id)
    if password == records[5]:
        print('Login')
        
    else:
        print('not login')
        
    print(records[5])

except:
    print('Not found')


#print(records)

