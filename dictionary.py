bank = {"Account_no" : {"Customer_name" : "Jason",
                        "Mobile_no" : 27948392,
                        "Email_id" : "jasontech@gmail.com",
                        "Address" : "U-47 A10 Street California",
                        "Account_type" : ['Saving', 'Current', 'Joint', 'NRI', 'Multi'],
                        "Transaction_details" : {"Deposit" :['Date','Time','Amount','Location']}

                        }
        }

print(bank)

print (bank ['Account_no']["Customer_name"])

print(bank ['Account_no']["Transaction_details"]["Deposit"])



