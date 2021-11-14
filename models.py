import datetime
from pydantic import BaseModel
from typing import Optional







#This class describes the structure used to hold transactionary data
class Transaction(BaseModel):

    def __init__(self, username: str, transaction_type: str, amount: int, currency :str, recipient: str):
        self.username = username
        self.transaction_type = transaction_type
        self.amount = amount
        self.currency = currency
        self.recipient = recipient

        # dd/mm/YY H:M:S formats date in preferable style
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_username(self):
        return self.username
    
    def get_transaction_type(self):
        return self.transaction_type
    
    def get_amount(self):
        return self.amount
    
    def get_currency(self):
        return self.currency
    
    def get_recipient(self):
        return self.recipient

    def get_timestamp(self):
        return self.timestamp