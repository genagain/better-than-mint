"""This module has functions that interact with the unofficial mint package"""

import os
import mintapi

def get_transactions():
    """
    Returns a pd.DataFrame of deduplicated transactions stored in
    your Mint account
    """
    email = os.environ['EMAIL']
    password = os.environ['PASSWORD']
    mint = mintapi.Mint(email, password)
    mint.initiate_account_refresh()
    transactions = mint.get_transactions()
    transactions.drop_duplicates(['date', 'original_description', 'amount'], inplace=True)
    return transactions
