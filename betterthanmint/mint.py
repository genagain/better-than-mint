"""This module contains functions that interact with the unofficial mint package"""

import os
import mintapi

def get_transactions():
    """Returns a pd.DataFrame of deduplicated transactions stored in your Mint account"""
    mint = mintapi.Mint(os.environ['EMAIL'], os.environ['PASSWORD'])
    mint.initiate_account_refresh()
    transactions = mint.get_transactions()
    transactions.drop_duplicates(['date', 'original_description', 'amount'], inplace=True)
    return transactions
