from fastapi import FastAPI
from datetime import datetime
import random
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

#This variable is set to false by default but changed to true when a user is validated for a session
is_logged_in = False

username = None

currency = None

transactions = []


#This function is called to verify user credentials and returns a boolean value 
 #depending on the validity of credentials entered
def user_is_valid(username, pin):
    if username in userDetails:
        if pin == userDetails[username]['pin']:
            return True

    return False

#This function collects user credentials and validates the session or recalls itself
def login():

    #The global keyword enables global variables to be modified at runtime
    global username
    global is_logged_in

    username = input("Please type your username\n")
    pin = input("Please enter your pin\n")
    
    if(user_is_valid(username, pin)):
        is_logged_in = True

    else:
        print("Credentials not valid.\n" +
              'Please try again')
        login()

#This function is for depositing money into your account
def deposit(username):

    if (amount <= 0):
        print(f"You cannot deposit {amount} {get_currency()}")
    else:
        balance = userDetails[username]['balance'][get_currency()]
        newBalance = balance + amount
        userDetails[username]['balance'][get_currency()] = newBalance
        print(f"An amount of {amount} {get_currency()} has been deposited into your account" +
        f"\nYour new balance is {get_balance(username, get_currency())} {get_currency()}")

        transaction = Transaction(username, "Deposit", amount, get_currency(), username)
        transactions.append(transaction)

        answer = input("\nWould you like to make another transaction? \n1.Yes\n2.No\n")

        if(answer == '1'):
            welcome_user(username)

@app.put('/{username}/account/deposit/{currency}/{amount}/')
def deposit_money(username, currency, amount):

    if(int(amount) > 0):
        balance = userDetails[username]['balance'][currency]
        userDetails[username]['balance'][currency] = int(balance) + int(amount)
        return userDetails[username]['balance'][currency]
        


 #This function allows users to withdraw money from their accounts depending on their account balance
@app.put('/{username}/account/{currency}/{amount}/')
def withdraw_money(username, currency, amount):

    balance = int(get_balance(username,currency))
    
    if(balance - int(amount) >= 0):
        userDetails[username]['balance'][currency] = int(balance) - int(amount)


        return userDetails[username]['balance'][currency]

#This function enables the transfer of money between user accounts
#It recalls itself when the recipient is not found
def transfer_money(username):


        amount = float(input("\nHow much would you like to transfer?\n"))
        balance = userDetails[username]['balance'][get_currency()]
        if (balance - amount) < 0:
            print("You do not have enough funds to complete this transaction\n")
        else:
            balance = balance - amount
            userDetails[username]['balance'][get_currency()] = balance
            userDetails[user]['balance'][get_currency()] += amount
            print(f"You have successfully transferred {amount} {get_currency()} to {user}")
            print(f"Your new balance is {get_balance(username, get_currency())}")

            transaction = Transaction(username, "Transfer", amount, get_currency(), user)
            transactions.append(transaction)

            answer = input("\nWould you like to make another transaction? \n1.Yes\n2.No\n")

            if(answer == '1'):
                welcome_user(username)

@app.get('/{username}/account/{currency}/')
def get_balance(username, currency):
    return userDetails[username]['balance'][currency]

#This function takes a list of transactions and prints details of each transaction
def generate_receipt(transactions): 
     pass