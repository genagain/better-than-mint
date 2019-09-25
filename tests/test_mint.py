"""This module runs unit tests for the mint module"""

import numpy as np
import pandas as pd

from betterthanmint import mint

def test_get_transactions(monkeypatch):
    """
    This function ensures that the get_transactions function
    returns pd.DataFrame containing deduplicated transactions stored in Mint
    """
    def mock_get_transactions():
        transactions = pd.read_pickle('tests/transactions.pickle')
        return transactions

    monkeypatch.setattr(mint, 'get_transactions', mock_get_transactions)

    transactions = mint.get_transactions()

    assert type(transactions).__name__ == 'DataFrame'

    column_names = [
        'date',
        'description',
        'original_description',
        'amount',
        'transaction_type',
        'category',
        'account_name'
        ]
    expected_columns = np.array(column_names, dtype=object)
    assert np.all(transactions.columns.values == expected_columns)
    duplicate_check = transactions.duplicated(
        subset=[
            'date',
            'original_description',
            'amount'
            ]
        )
    assert not np.all(duplicate_check)
