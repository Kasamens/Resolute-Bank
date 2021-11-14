from fastapi import FastAPI
from models import Transaction

app = FastAPI()


#This is the dictionary that holds user information
userDetails = {'kojo': 
                {'pin':'1234', 
                'balance' : {'GHS' : 35190,
                             'USD' : 5865}},
                'kofi': 
                {'pin':'1655', 
                'balance' : {'GHS' : 39000,
                             'USD' : 6500}},
                'kwabena': 
                {'pin':'0480', 
                'balance' : {'GHS' : 20814,
                             'USD' : 3469}},
                'matrevi': 
                {'pin':'1306', 
                'balance' : {'GHS' : 26856,
                             'USD' : 4476}},
               'justin':
               {'pin':'8743', 
                'balance' : {'GHS' : 35196,
                             'USD' : 5866}},
               'fernanda':
               {'pin':'5047',
                'balance' : {'GHS' : 33330,
                             'USD' : 5555}},
                'gifty':
                {'pin' : '6060',
                'balance' : {'GHS' : 34212,
                             'USD' : 5702}},
                'exorm':
                {'pin' : '4658',
                'balance': {'GHS' : 323154,
                            'USD' : 3859}},
                'sampson':
                {'pin' : '9390',
                'balance': {'GHS' : 26322,
                            'USD' : 4387}},
                'georgina':
                {'pin' : '7793',
                'balance': {'GHS' : 31974,
                            'USD' : 5329}},
               }    


transactions = []


#This function is for depositing money into your account

@app.put('/{username}/account/deposit/{currency}/{amount}/')
def deposit(username, currency, amount):

    if(int(amount) > 0):
        balance = userDetails[username]['balance'][currency]
        userDetails[username]['balance'][currency] = int(balance) + int(amount)
        return userDetails[username]['balance'][currency]
        
 #This function allows users to withdraw money from their accounts depending on their account balance
@app.put('/{username}/account/{currency}/{amount}/')
def withdraw(username, currency, amount):

    balance = int(get_balance(username,currency))
    
    if(balance - int(amount) >= 0):
        userDetails[username]['balance'][currency] = int(balance) - int(amount)


        return userDetails[username]['balance'][currency]

#This function enables the transfer of money between user accounts
#It recalls itself when the recipient is not found
@app.put('/{username}/account/{currency}/{amount}/{beneficiary}')
def transfer_money(username, currency, amount, beneficiary):

       

        if userDetails[username]['balance'][currency] - int(amount) >= 0:
            userDetails[username]['balance'][currency] -= int(amount)

            userDetails[beneficiary]['balance'][currency] += int(amount)

            return userDetails[username]['balance'][currency]

@app.get('/{username}/account/{currency}/')
def get_balance(username, currency):
    return userDetails[username]['balance'][currency]

#This function takes a list of transactions and prints details of each transaction
def generate_receipt(transactions): 
     pass