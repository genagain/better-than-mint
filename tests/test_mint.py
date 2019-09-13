import numpy as np
import pandas as pd

from betterthanmint import mint

def test_get_transactions(monkeypatch):
    def mock_get_transactions():
        transactions = pd.read_pickle('tests/transactions.pickle')
        return transactions

    monkeypatch.setattr(mint,'get_transactions', mock_get_transactions)

    transactions = mint.get_transactions()

    assert type(transactions).__name__ == 'DataFrame'

    expected_columns = np.array(['date', 'description', 'original_description', 'amount', 'transaction_type', 'category', 'account_name'], dtype=object)
    assert np.all(transactions.columns.values == expected_columns)
    assert np.all(transactions.duplicated(subset=['date','original_description','amount']) == False)
